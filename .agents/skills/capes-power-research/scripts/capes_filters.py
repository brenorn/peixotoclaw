import os
import json
from pydantic import BaseModel, Field
from typing import Optional, List
from google import genai
from dotenv import load_dotenv

load_dotenv()

class SearchRow(BaseModel):
    term: str = Field(description="Termo de busca (em inglês).")
    field: str = Field(default="Any", description="Tipo de campo: 'Any', 'Title', 'Author', 'Subject'.")
    operator: str = Field(default="AND", description="Operador lógico com a linha anterior: 'AND', 'OR', 'NOT'.")

class CapesFilters(BaseModel):
    search_rows: List[SearchRow] = Field(description="Lista de linhas de busca avançada.")
    start_year: Optional[int] = Field(description="Ano inicial da busca.")
    end_year: Optional[int] = Field(description="Ano final da busca.")
    open_access: bool = Field(default=False, description="Filtrar por acesso aberto.")
    peer_reviewed: bool = Field(default=True, description="Filtrar por revisado por pares.")

class FilterExtractor:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY non-existent.")
        self.client = genai.Client(api_key=self.api_key)
        self.model = "gemini-2.0-flash"

    def extract(self, user_input: str) -> CapesFilters:
        current_year = 2026 # Contexto do sistema
        prompt = f"""
        Você é um assistente de pesquisa especializado em extração de metadados para busca no Portal CAPES.
        Entrada do usuário: "{user_input}"
        Ano atual: {current_year}

        Extraia os filtros de busca no formato JSON seguindo estas regras:
        1. Decomponha o pedido em múltiplas `search_rows` se necessário (ex: "IA na construção mas não em madeira" -> Linha 1: 'AI Construction', Linha 2: 'Wood' com operador 'NOT').
        2. Campos suportados: 'Any' (Padrão), 'Title', 'Author', 'Subject'.
        3. Operadores: 'AND', 'OR', 'NOT'.
        4. Converta os termos para INGLÊS.
        5. Se o usuário pedir 'últimos X anos', calcule o `start_year` corretamente.

        Retorne APENAS o JSON puro.
        """
        
        response = self.client.models.generate_content(
            model=f"models/{self.model}",
            contents=[prompt],
            config={
                'response_mime_type': 'application/json',
                'response_schema': CapesFilters.model_json_schema()
            }
        )
        
        return CapesFilters.model_validate_json(response.text)

if __name__ == "__main__":
    extractor = FilterExtractor()
    test_input = "Quero artigos sobre 'Multi-Agent Systems na construção civil' dos últimos 5 anos, apenas Q1 e com acesso aberto."
    filters = extractor.extract(test_input)
    print(filters.model_dump_json(indent=2))
