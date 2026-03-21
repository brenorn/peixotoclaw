import { ILlmProvider } from '../../infra/providers/IProvider.js';
import { Skill, SkillMetadata } from './SkillLoader.js';

export class SkillRouter {
    constructor(private provider: ILlmProvider) {}

    async route(userInput: string, skills: Skill[]): Promise<string | null> {
        if (skills.length === 0) return null;

        const skillsSummary = skills.map(s => ({
            name: s.metadata.name,
            description: s.metadata.description
        }));

        const systemPrompt = `You are a skill router. Your job is to identify which skill fits the user's intent.
Available skills:
${JSON.stringify(skillsSummary, null, 2)}

Respond ONLY with a JSON object: {"skillName": "name_of_the_skill"} or {"skillName": null} if no skill matches.`;

        try {
            const response = await this.provider.chat([
                { role: 'system', content: systemPrompt },
                { role: 'user', content: userInput }
            ]);

            const result = JSON.parse(response.content.trim().replace(/```json|```/g, ''));
            return result.skillName;
        } catch (error) {
            console.error('Skill Router Error:', error);
            return null;
        }
    }
}
