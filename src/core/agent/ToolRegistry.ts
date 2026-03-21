import { BaseTool } from './BaseTool.js';

export class ToolRegistry {
    private tools: Map<string, BaseTool> = new Map();

    public register(tool: BaseTool): void {
        this.tools.set(tool.name, tool);
    }

    public getTool(name: string): BaseTool | undefined {
        return this.tools.get(name);
    }

    public getAllDefinitions() {
        return Array.from(this.tools.values()).map(t => t.definition);
    }
}
