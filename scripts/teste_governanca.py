import re
import os

def test_governance():
    print("🦞 [TESTE DE GOVERNANÇA] Iniciando validação...")
    
    # Simulando um código com erro de nomenclatura
    codigo_sujo = """
    def cadastrar_perfil(user_id, bio):
        query = f"INSERT INTO user_profile (user_id, bio) VALUES ({user_id}, '{bio}')"
        return query
    """
    
    # Lendo o SSOT
    with open("d:/OneDrive/aiproj/PeixotoClaw/METADATA_MASTER.md", "r", encoding="utf-8") as f:
        ssot = f.read()
    
    erros = []
    
    # Regra 1: Tabela deve ser 'perfis_usuarios', não 'user_profile'
    if "user_profile" in codigo_sujo and "perfis_usuarios" in ssot:
        erros.append("❌ ERRO: Nome de tabela 'user_profile' não consta no SSOT. Use 'perfis_usuarios'.")
    
    # Regra 2: Coluna deve ser 'id_usuario', não 'user_id'
    if "user_id" in codigo_sujo and "id_usuario" in ssot:
        erros.append("❌ ERRO: Atributo 'user_id' é inválido. O SSOT define 'id_usuario'.")

    if erros:
        for erro in erros:
            print(erro)
        print("\n🛡️ GOVERNANÇA: Bloqueando implementação por inconsistência de dados.")
    else:
        print("✅ Sucesso: O código respeita o METADATA_MASTER.")

if __name__ == "__main__":
    test_governance()
