import { ILlmProvider } from './IProvider.js';
import { GeminiProvider } from './GeminiProvider.js';
import { DeepSeekProvider } from './DeepSeekProvider.js';
import { OpenCodeProvider } from './OpenCodeProvider.js';
import { FallbackProvider } from './FallbackProvider.js';
import dotenv from 'dotenv';

dotenv.config();

export class ProviderFactory {
    public static create(provider?: string): ILlmProvider {
        const type = provider || process.env.DEFAULT_PROVIDER || 'gemini';
        let primary: ILlmProvider;

        switch (type.toLowerCase()) {
            case 'gemini':
                if (!process.env.GEMINI_API_KEY) throw new Error('GEMINI_API_KEY not found');
                primary = new GeminiProvider(process.env.GEMINI_API_KEY);
                break;
            case 'deepseek':
                if (!process.env.DEEPSEEK_API_KEY) throw new Error('DEEPSEEK_API_KEY not found');
                primary = new DeepSeekProvider(process.env.DEEPSEEK_API_KEY);
                break;
            case 'opencode':
                return new OpenCodeProvider();
            default:
                throw new Error(`Provider ${type} not supported`);
        }

        // Implementação do Fallback Automático (Estilo Sandeco)
        if (type.toLowerCase() === 'gemini' && process.env.DEEPSEEK_API_KEY) {
            const secondary = new DeepSeekProvider(process.env.DEEPSEEK_API_KEY);
            return new FallbackProvider(primary, secondary);
        }

        return primary;
    }

    public static getProviderName(provider?: string): string {
        return provider || process.env.DEFAULT_PROVIDER || 'gemini';
    }
}
