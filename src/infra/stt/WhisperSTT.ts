import { exec } from 'child_process';
import { promisify } from 'util';

const execPromise = promisify(exec);

export class WhisperSTT {
    async transcribe(filePath: string): Promise<string> {
        try {
            // Requires whisper-openai or similar python package: pip install openai-whisper
            // Using a simple command line call as an example
            const { stdout } = await execPromise(`whisper "${filePath}" --model base --language pt --output_format txt`);
            // whisper outputs files, so we might need to read the generated .txt file
            // For simplicity, we assume we can get the text from stdout or the generated file
            return stdout.trim();
        } catch (error) {
            console.error('Whisper STT Error:', error);
            throw new Error('Failed to transcribe audio');
        }
    }
}
