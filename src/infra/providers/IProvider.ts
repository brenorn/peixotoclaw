export interface ChatMessage {
    role: 'user' | 'assistant' | 'system' | 'tool';
    content: string;
    name?: string;
    tool_call_id?: string;
    tool_calls?: ToolCall[];
}

export interface ToolDefinition {
    name: string;
    description: string;
    parameters: any;
}

export interface ProviderResponse {
    content: string;
    toolCalls?: ToolCall[];
}

export interface ToolCall {
    id: string;
    name: string;
    arguments: any;
}

export interface ILlmProvider {
    chat(messages: ChatMessage[], tools?: ToolDefinition[]): Promise<ProviderResponse>;
}
