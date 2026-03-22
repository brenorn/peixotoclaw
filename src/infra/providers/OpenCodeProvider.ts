import axios from 'axios';
import { ILlmProvider, ChatMessage, ToolDefinition, ProviderResponse } from './IProvider.js';

/**
 * Provider for OpenCode (Local LLM via Port 27799)
 * Follows the OpenAI-compatible completion pattern.
 */
export class OpenCodeProvider implements ILlmProvider {
    private baseUrl = 'http://localhost:27799/v1';
    private model = 'local-model';

    constructor() {}

    setModel(model: string): void {
        console.log(`[OpenCodeProvider] Switching local model: ${model}`);
        this.model = model;
    }

    async chat(messages: ChatMessage[], tools?: ToolDefinition[]): Promise<ProviderResponse> {
        const url = `${this.baseUrl}/chat/completions`;
        
        // Convert to OpenAI standard format
        const body = {
            model: this.model,
            messages: messages.map(m => ({
                role: m.role === 'system' ? 'system' : (m.role === 'assistant' ? 'assistant' : 'user'),
                content: m.content
            })),
            temperature: 0.7,
            // local models often struggle with tools, so we pass them only if supported
            tools: tools?.map(t => ({
                type: 'function',
                function: {
                    name: t.name,
                    description: t.description,
                    parameters: t.parameters
                }
            }))
        };

        try {
            console.log(`[OpenCodeProvider] Sending request to local LLM...`);
            const response = await axios.post(url, body);
            const choice = response.data.choices[0];
            const content = choice.message.content || '';
            
            // Handle potential tool calls from local models
            const toolCallResults = choice.message.tool_calls?.map((tc: any) => ({
                id: tc.id,
                name: tc.function.name,
                arguments: JSON.parse(tc.function.arguments)
            }));

            return {
                content,
                toolCalls: toolCallResults
            };
        } catch (error: any) {
            console.error('[OpenCodeProvider] Error:', error.message);
            throw new Error(`Failed to communicate with OpenCode (Local): ${error.message}`);
        }
    }
}
