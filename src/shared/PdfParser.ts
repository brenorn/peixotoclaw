import fs from 'fs';
import { PDFParse } from 'pdf-parse';

export class PdfParser {
    public static async parse(filePath: string): Promise<string> {
        const dataBuffer = fs.readFileSync(filePath);
        try {
            const parser = new PDFParse({ data: dataBuffer });
            const data = await parser.getText();
            return data.text;
        } catch (error) {
            console.error('PDF Parse Error:', error);
            throw new Error('Failed to parse PDF');
        }
    }
}
