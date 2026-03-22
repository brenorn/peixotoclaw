import { ILlmProvider } from './IProvider.js';
import { GeminiProvider } from './GeminiProvider.js';
import { DeepSeekProvider } from './DeepSeekProvider.js';
import { OpenCodeProvider } from './OpenCodeProvider.js';
import dotenv from 'dotenv';

dotenv.config();

export class ProviderFactory {
    public static create(provider?: string): ILlmProvider {
        const type = provider || process.env.DEFAULT_PROVIDER || 'gemini';

        switch (type.toLowerCase()) {
            case 'gemini':
                if (!process.env.GEMINI_API_KEY) throw new Error('GEMINI_API_KEY not found');
                return new GeminiProvider(process.env.GEMINI_API_KEY);
            case 'deepseek':
                if (!process.env.DEEPSEEK_API_KEY) throw new Error('DEEPSEEK_API_KEY not found');
                return new DeepSeekProvider(process.env.DEEPSEEK_API_KEY);
            case 'opencode':
                return new OpenCodeProvider();
            default:
                throw new Error(`Provider ${type} not supported`);
        }
    }

    public static getProviderName(provider?: string): string {
        return provider || process.env.DEFAULT_PROVIDER || 'gemini';
    }
}
