import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

export interface SkillMetadata {
    name: string;
    description: string;
    [key: string]: any;
}

export interface Skill {
    metadata: SkillMetadata;
    content: string;
    path: string;
}

export class SkillLoader {
    private static skillsPath = path.resolve(process.cwd(), '.agents/skills');

    public static loadAll(): Skill[] {
        if (!fs.existsSync(this.skillsPath)) {
            fs.mkdirSync(this.skillsPath, { recursive: true });
            return [];
        }

        const skillDirs = fs.readdirSync(this.skillsPath, { withFileTypes: true })
            .filter(dirent => dirent.isDirectory())
            .map(dirent => dirent.name);

        const skills: Skill[] = [];

        for (const dir of skillDirs) {
            const skillFilePath = path.join(this.skillsPath, dir, 'SKILL.md');
            if (fs.existsSync(skillFilePath)) {
                try {
                    const fileContent = fs.readFileSync(skillFilePath, 'utf8');
                    const skill = this.parseSkill(fileContent, skillFilePath);
                    if (skill) {
                        skills.push(skill);
                    }
                } catch (error) {
                    console.error(`Error loading skill from ${dir}:`, error);
                }
            }
        }

        return skills;
    }

    private static parseSkill(content: string, filePath: string): Skill | null {
        const frontmatterRegex = /^---\r?\n([\s\S]*?)\r?\n---/;
        const match = content.match(frontmatterRegex);

        if (!match) return null;

        try {
            const metadata = yaml.load(match[1]) as SkillMetadata;
            const body = content.replace(frontmatterRegex, '').trim();

            return {
                metadata,
                content: body,
                path: filePath
            };
        } catch (e) {
            console.error('Error parsing YAML frontmatter:', e);
            return null;
        }
    }
}
