import axios from 'axios';
import { ILlmProvider, ChatMessage, ToolDefinition, ProviderResponse } from './IProvider.js';

export class DeepSeekProvider implements ILlmProvider {
    private apiKey: string;
    private baseUrl = 'https://api.deepseek.com/v1/chat/completions';
    private model = 'deepseek-chat';

    constructor(apiKey: string) {
        this.apiKey = apiKey;
    }

    setModel(model: string): void {
        console.log(`[DeepSeekProvider] Switching model: ${model}`);
        this.model = model;
    }

    async chat(messages: ChatMessage[], tools?: ToolDefinition[]): Promise<ProviderResponse> {
        const body: any = {
            model: this.model,
            messages: messages.map(m => {
                const msg: any = {
                    role: m.role,
                    content: m.content || null
                };

                if (m.tool_calls) {
                    msg.tool_calls = m.tool_calls.map(tc => ({
                        id: tc.id,
                        type: 'function',
                        function: {
                            name: tc.name,
                            arguments: JSON.stringify(tc.arguments)
                        }
                    }));
                }

                if (m.role === 'tool') {
                    msg.tool_call_id = m.tool_call_id;
                    msg.name = m.name;
                }

                return msg;
            }),
            stream: false
        };

        if (tools && tools.length > 0) {
            body.tools = tools.map(t => ({
                type: 'function',
                function: {
                    name: t.name,
                    description: t.description,
                    parameters: t.parameters
                }
            }));
            body.tool_choice = 'auto';
        }

        try {
            const response = await axios.post(this.baseUrl, body, {
                headers: {
                    'Authorization': `Bearer ${this.apiKey}`,
                    'Content-Type': 'application/json'
                }
            });

            const choice = response.data.choices[0];
            const content = choice.message.content || '';
            const toolCalls = choice.message.tool_calls?.map((tc: any) => ({
                id: tc.id,
                name: tc.function.name,
                arguments: JSON.parse(tc.function.arguments)
            }));

            return {
                content,
                toolCalls
            };
        } catch (error: any) {
            console.error('DeepSeek API Error:', error.response?.data || error.message);
            throw new Error('Failed to fetch response from DeepSeek');
        }
    }
}
