export abstract class BaseTool {
    abstract name: string;
    abstract description: string;
    abstract parameters: any;

    abstract execute(args: any): Promise<string>;

    get definition() {
        return {
            name: this.name,
            description: this.description,
            parameters: this.parameters
        };
    }
}
