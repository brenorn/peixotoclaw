import { ILlmProvider, ChatMessage } from '../../infra/providers/IProvider.js';
import { ToolRegistry } from './ToolRegistry.js';

export class AgentLoop {
    private maxIterations: number;

    constructor(
        private provider: ILlmProvider,
        private toolRegistry: ToolRegistry,
        maxIterations?: number
    ) {
        this.maxIterations = maxIterations || parseInt(process.env.MAX_ITERATIONS || '5');
    }

    async run(messages: ChatMessage[], systemPrompt: string): Promise<string> {
        let currentMessages: ChatMessage[] = [
            { role: 'system', content: systemPrompt },
            ...messages
        ];

        let iteration = 0;
        let finalResponse = '';

        while (iteration < this.maxIterations) {
            console.log(`[AgentLoop] Iteration ${iteration + 1}/${this.maxIterations}`);
            
            const response = await this.provider.chat(currentMessages, this.toolRegistry.getAllDefinitions());
            
            // Add assistant response to history
            const assistantMessage: ChatMessage = { 
                role: 'assistant', 
                content: response.content || '',
                tool_calls: response.toolCalls 
            };
            currentMessages.push(assistantMessage);

            if (response.content) {
                finalResponse = response.content;
            }

            if (response.toolCalls && response.toolCalls.length > 0) {
                for (const toolCall of response.toolCalls) {
                    console.log(`[AgentLoop] Calling tool: ${toolCall.name}`);
                    const tool = this.toolRegistry.getTool(toolCall.name);
                    let observation = '';

                    if (tool) {
                        try {
                            observation = await tool.execute(toolCall.arguments);
                        } catch (e: any) {
                            observation = `Error executing tool: ${e.message}`;
                        }
                    } else {
                        observation = `Error: Tool ${toolCall.name} not found.`;
                    }

                    console.log(`[AgentLoop] Observation: ${observation.substring(0, 100)}...`);
                    currentMessages.push({
                        role: 'tool',
                        content: observation,
                        tool_call_id: toolCall.id,
                        name: toolCall.name
                    });
                }
                iteration++;
            } else {
                // No tool calls, we finished
                break;
            }
        }

        if (iteration >= this.maxIterations) {
            console.warn('[AgentLoop] Max iterations reached');
            return finalResponse + (finalResponse ? "\n\n" : "") + "(Note: Reached maximum iterations, some tasks might be incomplete.)";
        }

        return finalResponse;
    }
}
