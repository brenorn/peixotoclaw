import { ChatMessage } from '../../infra/providers/IProvider.js';

/**
 * LessTokens: Semantic Context Compression Layer
 * Designed to minimize token waste and maximize LLM precision.
 */
export class LessTokens {
    /**
     * Prunes a long content string by keeping the most relevant "Anchors".
     * (e.g., Headers, Top rules, and the tail of the file).
     */
    public static prune(content: string, maxLines: number = 80): string {
        const lines = content.split('\n');
        if (lines.length <= maxLines) return content;

        console.log(`[LessTokens] Pruning content from ${lines.length} to ${maxLines} lines.`);
        
        // Keep the first 40 lines (usually contains rules and headers)
        const head = lines.slice(0, Math.floor(maxLines / 2));
        // Keep the last 40 lines (usually contains the latest tasks/changes)
        const tail = lines.slice(-Math.floor(maxLines / 2));

        return [
            ...head,
            `\n\n... [LessTokens: ${lines.length - maxLines} lines compressed for efficiency] ...\n\n`,
            ...tail
        ].join('\n');
    }

    /**
     * Compacts the conversation history by keeping only the last N messages
     * or summarizing the earlier ones.
     */
    public static compactHistory(history: ChatMessage[], keepLast: number = 5): ChatMessage[] {
        if (history.length <= keepLast) return history;

        console.log(`[LessTokens] Compacting history from ${history.length} to ${keepLast} messages.`);
        
        const summaryMsg: ChatMessage = {
            role: 'system',
            content: `[Context Summary]: Discussed ${history.length - keepLast} previous messages regarding project architecture and previous tasks.`
        };

        return [summaryMsg, ...history.slice(-keepLast)];
    }
}
