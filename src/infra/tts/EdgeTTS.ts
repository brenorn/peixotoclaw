import { exec } from 'child_process';
import path from 'path';
import fs from 'fs';
import { promisify } from 'util';

const execPromise = promisify(exec);

export class EdgeTTS {
    private voice = 'pt-BR-ThalitaNeural';

    async synthesize(text: string): Promise<string> {
        const tmpDir = path.resolve(process.cwd(), 'tmp');
        if (!fs.existsSync(tmpDir)) {
            fs.mkdirSync(tmpDir, { recursive: true });
        }

        const fileName = `tts_${Date.now()}.mp3`;
        const filePath = path.join(tmpDir, fileName);

        try {
            // Requires edge-tts python package to be installed: pip install edge-tts
            await execPromise(`edge-tts --voice ${this.voice} --text "${text.replace(/"/g, '\\"')}" --write-media ${filePath}`);
            return filePath;
        } catch (error) {
            console.error('Edge-TTS Error:', error);
            throw new Error('Failed to synthesize speech');
        }
    }
}
