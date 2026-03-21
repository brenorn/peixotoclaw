import fs from 'fs';
import path from 'path';
import { BaseTool } from '../BaseTool.js';

export class CreateFileTool extends BaseTool {
    name = 'create_file';
    description = 'Creates a file with the given content at the specified path.';
    parameters = {
        type: 'object',
        properties: {
            filePath: { type: 'string', description: 'Absolute or relative path to the file.' },
            content: { type: 'string', description: 'The content to write to the file.' }
        },
        required: ['filePath', 'content']
    };

    async execute(args: { filePath: string, content: string }): Promise<string> {
        try {
            const absolutePath = path.isAbsolute(args.filePath) ? args.filePath : path.resolve(process.cwd(), args.filePath);
            const dir = path.dirname(absolutePath);
            if (!fs.existsSync(dir)) {
                fs.mkdirSync(dir, { recursive: true });
            }
            fs.writeFileSync(absolutePath, args.content);
            return `File created successfully at ${absolutePath}`;
        } catch (error: any) {
            return `Error creating file: ${error.message}`;
        }
    }
}

export class ReadFileTool extends BaseTool {
    name = 'read_file';
    description = 'Reads the content of a file at the specified path.';
    parameters = {
        type: 'object',
        properties: {
            filePath: { type: 'string', description: 'Absolute or relative path to the file.' }
        },
        required: ['filePath']
    };

    async execute(args: { filePath: string }): Promise<string> {
        try {
            const absolutePath = path.isAbsolute(args.filePath) ? args.filePath : path.resolve(process.cwd(), args.filePath);
            if (!fs.existsSync(absolutePath)) {
                return `Error: File not found at ${absolutePath}`;
            }
            const content = fs.readFileSync(absolutePath, 'utf8');
            return content;
        } catch (error: any) {
            return `Error reading file: ${error.message}`;
        }
    }
}

export class ListDirTool extends BaseTool {
    name = 'list_dir';
    description = 'Lists the contents of a directory.';
    parameters = {
        type: 'object',
        properties: {
            dirPath: { type: 'string', description: 'Absolute or relative path to the directory.' }
        },
        required: ['dirPath']
    };

    async execute(args: { dirPath: string }): Promise<string> {
        try {
            const absolutePath = path.isAbsolute(args.dirPath) ? args.dirPath : path.resolve(process.cwd(), args.dirPath);
            if (!fs.existsSync(absolutePath)) {
                return `Error: Directory not found at ${absolutePath}`;
            }
            const files = fs.readdirSync(absolutePath, { withFileTypes: true });
            const list = files.map(f => `${f.isDirectory() ? '[DIR]' : '[FILE]'} ${f.name}`).join('\n');
            return list || '(Empty directory)';
        } catch (error: any) {
            return `Error listing directory: ${error.message}`;
        }
    }
}
