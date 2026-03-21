import os
import json
from google import genai
from .datasets import Datasets

class AgenticAcademicRAG:
    """
    Implementação baseada no 'AgenticRAG' do Sandeco.
    Utiliza um roteador inteligente para decidir qual base de conhecimento acadêmico consultar.
    """
    def __init__(self):
        self.datasets = Datasets()
        self.model = "gemini-2.0-flash" # Versão rápida para roteamento
        self.api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY or GOOGLE_API_KEY not found in environment.")
        self.client = genai.Client(api_key=self.api_key)

    def create_router_prompt(self, query):
        prompt = f'''
        🎯 Missão: Roteamento de Conhecimento Acadêmico (Nível Ph.D.)
        Com base na solicitação do pesquisador: "{query}"
        Escolha o dataset mais apropriado da lista abaixo:
        '''
        
        for ds in self.datasets.datasets:
            prompt += f"- {ds['description']} -> Use: {ds['dataset']} (Locale: {ds['locale']})\n"

        prompt += """\n
        Retorne APENAS um JSON:
        {
          "dataset_name": "nome_do_dataset",
          "locale": "pt-BR ou en-US",
          "query": "Sua pergunta refinada e traduzida para o locale do dataset"
        }
        """
        return prompt

    def route_query(self, query):
        prompt = self.create_router_prompt(query)
        response = self.client.models.generate_content(
            model=f"models/{self.model}",
            contents=[prompt]
        )
        
        # Limpeza básica do JSON se necessário (removendo markdown)
        text = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(text)

    def search_in_dataset(self, routed_info):
        """
        Simula a busca vetorial (RAG) no dataset escolhido.
        No futuro, isso integrará com ChromaDB ou similar.
        """
        dataset = routed_info['dataset_name']
        refined_query = routed_info['query']
        
        print(f"📡 [RAG Routing] Direcionando para: {dataset}")
        
        # Simulação de retorno de conhecimento
        results = {
            "construction_norms": "De acordo com a NBR 12721, o controle de custos deve ser atômico.",
            "ai_frameworks": "LangGraph permite a implementação de estados cíclicos persistentes.",
            "phd_writing_standards": "ASCE exige uma seção dedicada a 'Practical Applications'.",
            "simulation_results": "LangGraph demonstrou latência de 3.5s vs 4.2s do PydanticAI."
        }
        
        return results.get(dataset, "Dados não encontrados para este contexto.")

if __name__ == "__main__":
    # Teste rápido
    rag = AgenticAcademicRAG()
    test_query = "Como o LangGraph ajuda no planejamento de obras segundo as normas?"
    routing = rag.route_query(test_query)
    print(f"✅ Roteamento: {routing}")
    result = rag.search_in_dataset(routing)
    print(f"📖 Conhecimento Extraído: {result}")
