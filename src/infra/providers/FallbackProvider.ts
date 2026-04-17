import { ILlmProvider, ChatMessage, ToolDefinition, ProviderResponse } from './IProvider.js';

export class FallbackProvider implements ILlmProvider {
    private primary: ILlmProvider;
    private secondary: ILlmProvider;

    constructor(primary: ILlmProvider, secondary: ILlmProvider) {
        this.primary = primary;
        this.secondary = secondary;
    }

    async chat(messages: ChatMessage[], tools?: ToolDefinition[]): Promise<ProviderResponse> {
        try {
            console.log(`[Fallback] Tentando provedor primário...`);
            return await this.primary.chat(messages, tools);
        } catch (error: any) {
            console.error(`[Fallback] Erro no provedor primário: ${error.message}`);
            console.log(`[Fallback] Acionando provedor secundário de reserva...`);
            try {
                return await this.secondary.chat(messages, tools);
            } catch (secError: any) {
                console.error(`[Fallback] Erro fatal: Todos os provedores falharam. ${secError.message}`);
                throw secError;
            }
        }
    }

    setModel(model: string): void {
        this.primary.setModel(model);
        // O secundário geralmente usa o modelo default do provider de fallback
    }
}
