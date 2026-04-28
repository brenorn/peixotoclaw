import axios from 'axios';
import { ILlmProvider, ChatMessage, ToolDefinition, ProviderResponse } from './IProvider.js';

type AnthropicContentBlock = Record<string, any>;

export class ClaudeProvider implements ILlmProvider {
    private baseUrl = 'https://api.anthropic.com/v1/messages';
    private model: string;
    private advisorEnabled: boolean;
    private advisorModel: string;
    private advisorMaxUses: number;
    private advisorCacheTtl?: '5m' | '1h';

    constructor(private apiKey: string) {
        this.model = process.env.CLAUDE_EXECUTOR_MODEL || 'claude-sonnet-4-6';
        this.advisorEnabled = (process.env.CLAUDE_ADVISOR_ENABLED || 'true').toLowerCase() !== 'false';
        this.advisorModel = process.env.CLAUDE_ADVISOR_MODEL || 'claude-opus-4-7';
        this.advisorMaxUses = parseInt(process.env.CLAUDE_ADVISOR_MAX_USES || '2', 10);

        const ttl = process.env.CLAUDE_ADVISOR_CACHE_TTL;
        if (ttl === '5m' || ttl === '1h') {
            this.advisorCacheTtl = ttl;
        }
    }

    setModel(model: string): void {
        if (!model || model.startsWith('gemini-')) return;
        console.log(`[ClaudeProvider] Switching executor model: ${model}`);
        this.model = model;
    }

    async chat(messages: ChatMessage[], tools?: ToolDefinition[]): Promise<ProviderResponse> {
        const systemMessages = messages.filter(m => m.role === 'system').map(m => m.content).filter(Boolean);
        const apiMessages = messages.filter(m => m.role !== 'system').map(m => this.toAnthropicMessage(m));
        const apiTools = this.buildTools(tools);

        const body: any = {
            model: this.model,
            max_tokens: parseInt(process.env.CLAUDE_MAX_TOKENS || '4096', 10),
            messages: apiMessages
        };

        if (systemMessages.length > 0) {
            body.system = this.withAdvisorGuidance(systemMessages.join('\n\n'));
        }

        if (apiTools.length > 0) {
            body.tools = apiTools;
        }

        try {
            const headers: Record<string, string> = {
                    'x-api-key': this.apiKey,
                    'anthropic-version': '2023-06-01',
                    'content-type': 'application/json'
            };

            if (this.advisorEnabled) {
                headers['anthropic-beta'] = 'advisor-tool-2026-03-01';
            }

            const response = await axios.post(this.baseUrl, body, {
                headers
            });

            const contentBlocks = response.data.content || [];
            const text = this.extractText(contentBlocks);
            const toolCalls = contentBlocks
                .filter((block: AnthropicContentBlock) => block.type === 'tool_use')
                .map((block: AnthropicContentBlock) => ({
                    id: block.id,
                    name: block.name,
                    arguments: block.input || {}
                }));

            return {
                content: text,
                rawContent: contentBlocks,
                usage: response.data.usage,
                toolCalls: toolCalls.length > 0 ? toolCalls : undefined
            };
        } catch (error: any) {
            const errorData = error.response?.data;
            console.error('Claude API Error:', JSON.stringify(errorData || error.message, null, 2));
            throw new Error(`Failed to fetch response from Claude: ${errorData?.error?.message || error.message}`);
        }
    }

    private toAnthropicMessage(message: ChatMessage): any {
        if (message.rawContent && message.role === 'assistant') {
            return {
                role: 'assistant',
                content: message.rawContent
            };
        }

        if (message.role === 'tool') {
            return {
                role: 'user',
                content: [
                    {
                        type: 'tool_result',
                        tool_use_id: message.tool_call_id,
                        content: message.content || ''
                    }
                ]
            };
        }

        if (message.tool_calls && message.tool_calls.length > 0) {
            return {
                role: 'assistant',
                content: [
                    ...(message.content ? [{ type: 'text', text: message.content }] : []),
                    ...message.tool_calls.map(toolCall => ({
                        type: 'tool_use',
                        id: toolCall.id,
                        name: toolCall.name,
                        input: toolCall.arguments || {}
                    }))
                ]
            };
        }

        return {
            role: message.role === 'assistant' ? 'assistant' : 'user',
            content: message.content || ' '
        };
    }

    private buildTools(tools?: ToolDefinition[]): any[] {
        const apiTools: any[] = [];

        if (this.advisorEnabled) {
            const advisorTool: any = {
                type: 'advisor_20260301',
                name: 'advisor',
                model: this.advisorModel,
                max_uses: this.advisorMaxUses
            };

            if (this.advisorCacheTtl) {
                advisorTool.caching = { type: 'ephemeral', ttl: this.advisorCacheTtl };
            }

            apiTools.push(advisorTool);
        }

        if (tools && tools.length > 0) {
            apiTools.push(...tools.map(tool => ({
                name: tool.name,
                description: tool.description,
                input_schema: tool.parameters
            })));
        }

        return apiTools;
    }

    private extractText(contentBlocks: AnthropicContentBlock[]): string {
        return contentBlocks
            .filter(block => block.type === 'text' && typeof block.text === 'string')
            .map(block => block.text)
            .join('\n')
            .trim();
    }

    private withAdvisorGuidance(systemPrompt: string): string {
        if (!this.advisorEnabled) return systemPrompt;

        return `The advisor should respond in under 100 words and use enumerated steps, not explanations.
You have access to an advisor tool backed by a stronger reviewer model. It takes no parameters; when called, the full conversation history is forwarded automatically.
For complex coding or agent tasks, call advisor after initial orientation and before substantive implementation. Also call advisor when stuck, when changing approach, and before declaring a substantial task complete.
Give the advice serious weight, but adapt if tool output or source files contradict it.

${systemPrompt}`;
    }
}
