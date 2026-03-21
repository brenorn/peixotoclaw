import axios from 'axios';
import { ILlmProvider, ChatMessage, ToolDefinition, ProviderResponse } from './IProvider.js';

export class GeminiProvider implements ILlmProvider {
    private apiKey: string;
    private baseUrl = 'https://generativelanguage.googleapis.com/v1beta/models';
    private model = 'gemini-2.0-flash';

    constructor(apiKey: string) {
        this.apiKey = apiKey;
    }

    async chat(messages: ChatMessage[], tools?: ToolDefinition[]): Promise<ProviderResponse> {
        const url = `${this.baseUrl}/${this.model}:generateContent?key=${this.apiKey}`;
        
        const contents = messages
            .filter(m => m.role !== 'system')
            .map(m => {
                const role = m.role === 'assistant' ? 'model' : (m.role === 'tool' ? 'function' : 'user');
                const parts: any[] = [];

                if (m.tool_calls) {
                    m.tool_calls.forEach(tc => {
                        parts.push({
                            functionCall: {
                                name: tc.name,
                                args: tc.arguments
                            }
                        });
                    });
                } else if (m.role === 'tool') {
                    parts.push({
                        functionResponse: {
                            name: m.name,
                            response: { content: m.content }
                        }
                    });
                } else {
                    parts.push({ text: m.content || ' ' });
                }

                return { role, parts };
            });

        const systemMessage = messages.find(m => m.role === 'system');
        
        const body: any = {
            contents,
            generationConfig: {
                temperature: 0.7,
                topP: 0.95,
                topK: 40,
                maxOutputTokens: 2048,
            }
        };

        if (systemMessage) {
            // High priority: add as actual system_instruction
            body.system_instruction = {
                parts: [{ text: systemMessage.content }]
            };
            
            // Also inject as a "user" instruction at the beginning of the messages to ensure it's seen
            // especially if the model/API version treats system_instruction with lower weight than we need
            contents.unshift({
                role: 'user',
                parts: [{ text: `SYSTEM INSTRUCTION (CRITICAL): ${systemMessage.content}` }]
            });
            
            // Add a model acknowledgement to make the context "sturdier"
            contents.splice(1, 0, {
                role: 'model',
                parts: [{ text: 'Entendido. Seguirei as instruções do sistema rigorosamente, respondendo no idioma do usuário e mantendo a estrutura solicitada.' }]
            });
        }

        if (tools && tools.length > 0) {
            body.tools = [{
                function_declarations: tools.map(t => ({
                    name: t.name,
                    description: t.description,
                    parameters: t.parameters
                }))
            }];
        }

        try {
            const response = await axios.post(url, body);
            const candidate = response.data.candidates[0];
            const content = candidate.content.parts.find((p: any) => p.text)?.text || '';
            const functionCalls = candidate.content.parts.filter((p: any) => p.functionCall);
            
            const toolCalls = functionCalls.map((p: any) => ({
                id: Math.random().toString(36).substring(7),
                name: p.functionCall.name,
                arguments: p.functionCall.args
            }));

            return {
                content,
                toolCalls: toolCalls.length > 0 ? toolCalls : undefined
            };
        } catch (error: any) {
            const errorData = error.response?.data;
            console.error('Gemini API Error:', JSON.stringify(errorData, null, 2));
            
            if (errorData?.error?.code === 404) {
                console.warn(`[Gemini] Tip: Check if the model name '${this.model}' or the API version in baseUrl '${this.baseUrl}' is correct for your API key.`);
            }
            
            throw new Error(`Failed to fetch response from Gemini: ${errorData?.error?.message || error.message}`);
        }
    }
}
