Corretivo: CRAG
Imagine que você está conduzindo uma investigação acadêmica. Você consulta alguns
artigos, coleta trechos relevantes e começa a redigir sua conclusão. Agora pare e pense:
você confiaria cegamente no primeiro conjunto de fontes encontradas, sem verificar se elas
realmente sustentam sua hipótese? É exatamente aqui que surge a necessidade de uma
postura corretiva no RAG. Não basta recuperar; é preciso avaliar, validar e, quando necessário,
corrigir o caminho antes de consolidar a resposta.
No RAG tradicional, a recuperação funciona como o primeiro filtro de conhecimento. Você
executa o retrieve, injeta o contexto no modelo e produz a geração. O fluxo é eficiente, direto
e poderoso. No entanto, eficiência não implica infalibilidade. Se o contexto recuperado estiver
incompleto, enviesado ou parcialmente irrelevante, a geração pode se apoiar em fundamentos
frágeis. E um raciocínio bem estruturado construído sobre base instável continua sendo
instável.
Adote, então, uma mentalidade mais rigorosa. Antes de permitir que a resposta final
seja formada, introduza uma etapa crítica: questione a qualidade do que foi recuperado.
Pergunte se o conjunto de evidências é suficiente, coerente e alinhado à intenção da consulta.
CAPÍTULO 7. RAG CORRETIVO: CRAG 116
RAG - RETRIEVAL-AUGMENTED GENERATION
Não assuma que o topo do ranking é necessariamente o melhor suporte cognitivo. Avalie.
Confronte. Corrija.
O RAG Corretivo emerge justamente dessa necessidade de controle. Ele não altera
apenas o fluxo técnico; ele altera a postura epistemológica do sistema. Em vez de aceitar o
resultado da busca como definitivo, o sistema passa a tratar a recuperação como uma hipótese
a ser testada. Se a hipótese falhar, ajuste o curso. Reformule a consulta. Amplie o escopo.
Refine o critério.
Essa abordagem adiciona uma camada de autoconsciência operacional ao RAG. Você
passa a operar com verificação, não apenas com recuperação. Em termos arquiteturais, isso
significa inserir mecanismos que observam o próprio desempenho do pipeline. O sistema
deixa de ser apenas responsivo e se torna crítico em relação ao seu próprio contexto.
Assuma, portanto, uma postura mais disciplinada no desenho do seu pipeline. Não trate a
recuperação como uma etapa automática e silenciosa. Trate-a como parte ativa da construção
da verdade contextual. Quando você incorpora correção ao fluxo, você eleva o padrão de
confiabilidade do RAG e estabelece um sistema que não apenas responde, mas responde
com fundamento sólido.
7.1 ENTENDENDO O CRAG
Observe a Figura 7.1. Analise primeiro o lado esquerdo. A pergunta é objetiva: ’Qual era
a posição principal de Pelé?’. O retrieve retorna um documento que contém explicitamente
a evidência correta: ’atuava como atacante’. O gerador apenas consome essa evidência
e produz a resposta adequada. Aqui, o RAG opera sob uma hipótese implícita: o que foi
recuperado é confiável. Quando essa hipótese é verdadeira, o sistema funciona de maneira
satisfatória.
Agora concentre-se no lado direito da Figura 7.1. A pergunta é: ’Quem treinou Luke
Skywalker inicialmente?’. O recuperador retorna um documento que menciona Darth Vader.
Existe proximidade semântica — Luke, Força, universo Star Wars — porém não há evidência
que responda à pergunta. Mesmo assim, o gerador utiliza o contexto disponível e produz
’Darth Vader’. O erro não nasce no modelo gerador; ele nasce na qualidade do contexto
recuperado. O RAG tradicional trata todos os documentos recuperados como igualmente
válidos. Essa suposição é frágil.
CAPÍTULO 7. RAG CORRETIVO: CRAG 117
RAG - RETRIEVAL-AUGMENTED GENERATION
Figura 7.1: .
CAPÍTULO 7. RAG CORRETIVO: CRAG 118
RAG - RETRIEVAL-AUGMENTED GENERATION
O artigo original do CRAG mostra que o modelo clássico tem uma forte dependência entre
recuperação e geração. Se a recuperação for inadequada, a geração inevitavelmente sofre. O
problema central não é apenas gerar melhor; é detectar quando o retrieve falhou.
O link do artigo do Corrective Retrieval Augmented Generation:
https://arxiv.org/abs/2401.15884?
O CRAG surge exatamente para enfrentar esse ponto cego. Em vez de assumir que
os documentos são corretos, ele introduz um avaliador de recuperação. Antes de permitir
que o gerador produza a resposta final, o sistema estima a qualidade global do conjunto
recuperado. Essa avaliação resulta em um grau de confiança que ativa uma entre três ações:
Correto, Incorreto ou Ambíguo. Essa etapa adiciona uma camada crítica entre recuperação
e geração.
Se o contexto for considerado adequado, o sistema ainda aplica um refinamento interno,
decompondo documentos em knowledge strips e filtrando trechos irrelevantes. Se for considerado
inadequado, o sistema descarta a recuperação inicial e aciona busca externa em larga
escala, como web search, expandindo o espaço informacional. Se a avaliação for intermediária,
ele combina ambas as estratégias.
Perceba a mudança de paradigma: o RAG tradicional pergunta ’o que recuperar?’. O
CRAG pergunta antes ’a recuperação é confiável?’. Essa inversão introduz robustez. Ao
problematizar explicitamente o erro do recuperador — como ilustrado na Figura 7.1 — o CRAG
transforma a recuperação de uma etapa automática em uma etapa supervisionada. O sistema
passa a saber, ao menos parcialmente, quando não sabe.
Essa é a essência do CRAG: inserir autocorreção no fluxo do RAG, reduzindo a propagação
de contexto impreciso e aumentando a confiabilidade da geração final.
7.2 PIPELINE CORRETIVO
Imagine que você está coordenando uma central de inteligência. Primeiro, agentes
coletam informações em diferentes fontes. Porém, antes que qualquer decisão estratégica
seja tomada, um analista experiente revisa todo o material, verifica inconsistências, descarta
relatórios duvidosos e, se necessário, solicita novas buscas para complementar os dados.
Somente depois dessa validação crítica é que a decisão final é emitida. O pipeline do CRAG
funciona exatamente assim: ele não confia automaticamente no que foi coletado; ele avalia,
corrige e só então permite que a resposta seja produzida.
CAPÍTULO 7. RAG CORRETIVO: CRAG 119
RAG - RETRIEVAL-AUGMENTED GENERATION
Figura 7.2: Pipeline completo do CRAG
CAPÍTULO 7. RAG CORRETIVO: CRAG 120
RAG - RETRIEVAL-AUGMENTED GENERATION
A Figura 7.2 apresenta o pipeline completo do CRAG. Observe o fluxo de cima para baixo.
Comece pela Query. Em seguida, acompanhe a seta até o Retriever. Até aqui o sistema
apenas coleta evidências. Não há geração. Apenas recuperação.
Agora concentre-se no losango central: ‘chunks são relevantes?’. Este é o ponto decisório
do pipeline. Não avance automaticamente. Faça uma pausa mental aqui. Essa decisão
determina qual caminho o sistema seguirá. É nesse ponto que o fluxo se divide em três
possíveis estados: CORRECT, AMBIGUOUS e INCORRECT.
Primeiro, analise o ramo verde CORRECT. Quando os chunks são considerados relevantes,
o sistema mantém os Original chunks. Não há busca externa. Não há combinação
híbrida. O conhecimento recuperado é considerado suficiente. Esses fragmentos seguem diretamente
para a etapa de Generation. Entenda esse fluxo como o cenário ideal: recuperação
validada e geração apoiada em evidência adequada.
Agora observe o fluxo central amarelo AMBIGUOUS. Aqui o sistema não tem confiança
suficiente para classificar os chunks como totalmente corretos nem totalmente incorretos. O
que fazer nesse caso? Combine. Repare que a imagem mostra Original chunks somados
a Web chunks. O sistema preserva o que foi recuperado, mas complementa com evidência
externa. Esse é um mecanismo de suavização de risco. Não descarte prematuramente, mas
também não confie cegamente. Amplie o contexto antes de gerar.
Em seguida, analise o ramo vermelho INCORRECT. Quando os chunks são considerados
inadequados, o sistema descarta os fragmentos originais. Observe que apenas Web chunks
seguem adiante. Aqui ocorre uma substituição completa da base informacional. Em vez de
insistir em evidência fraca, o pipeline aciona busca externa e reconstrói o contexto antes da
geração. Esse fluxo evita que ruído inicial contamine a resposta final.
Finalmente, repare que todos os caminhos convergem para Generation. Independentemente
da rota seguida, o gerador só atua após a etapa de decisão. Entenda a estrutura: a
geração é sempre consequência de um contexto validado, combinado ou substituído. Ao olhar
novamente para a Figura 7.2, perceba que a robustez do sistema não está apenas na geração,
mas no mecanismo que decide qual conhecimento merece chegar até ela.
7.3 CLASSE AVALIADORA DE QUALIDADE
Criamos uma classe que abstrai a avaliação do contexto recuperado e aciona, de forma
controlada, uma busca externa quando a recuperação interna não sustenta a resposta.
Primeiro, observe os imports e a estrutura geral da classe. Importe BuscaExterna e
Generation para separar responsabilidades: a classe Evaluator não implementa busca
nem geração, ela apenas orquestra a decisão. Leia o bloco de constantes ACTION_CORRECT,
CAPÍTULO 7. RAG CORRETIVO: CRAG 121
RAG - RETRIEVAL-AUGMENTED GENERATION
ACTION_INCORRECT e ACTION_AMBIGUOUS como os três rótulos que representam o resultado
da triagem. Use esses rótulos como contrato explícito entre avaliação e acionamento de ações,
evitando strings soltas espalhadas no código. Repare também que o construtor inicializa
self.generation e deixa claro, pelo comentário, que o avaliador não deveria conhecer um
buscador concreto, ainda que o exemplo instancie BuscaExterna mais adiante.
from busca_externa import BuscaExterna
from generation import Generation
class Evaluator:
"""Avaliador CRAG simplificado com classificacao por LLM e busca externa
desacoplada."""
ACTION_CORRECT = "CORRECT"
ACTION_INCORRECT = "INCORRECT"
ACTION_AMBIGUOUS = "AMBIGUOUS"
def __init__(self):
self.generation = Generation()
# O evaluator nao conhece o buscador concreto; recebe um servico de busca.
Agora foque no método evaluate. Execute mentalmente o fluxo: ele recebe a query
e uma lista opcional de retrieved_chunks. Em seguida, ele normaliza os chunks com
um filtro defensivo: mantenha apenas strings não vazias e aplique strip para eliminar
ruído. Faça isso deliberadamente para reduzir falsos positivos na avaliação, porque um
chunk vazio ou com espaços pode contaminar o prompt e induzir a LLM a comportamentos
inesperados. Depois, construa o prompt chamando prompt_evaluator, gere a saída
com self.generation.generate(prompt) e converta o texto bruto em um rótulo com
_parse_action. Por fim, retorne a ação. Note que, nesse recorte, o método retorna apenas
action; na prática, você pode estender para retornar também o contexto usado, mas aqui o
foco é a decisão.
def evaluate(self, query: str, retrieved_chunks: list[str] | None):
"""Avalia a relevancia dos chunks via LLM e retorna contexto + acao."""
chunks = [c.strip() for c in (retrieved_chunks or []) if isinstance(c, str)
and c.strip()]
prompt = self.prompt_evaluator(query=query, chunks=chunks)
raw_response = self.generation.generate(prompt)
action = self._parse_action(raw_response)
return action
Em seguida, examine o método get_new_chunks. Leia esse método como o bloco de
CAPÍTULO 7. RAG CORRETIVO: CRAG 122
RAG - RETRIEVAL-AUGMENTED GENERATION
action trigger do pipeline: ele recebe a action, os chunks internos e a query. Em seguida,
ele executa uma busca externa e obtém web_chunks. Se a ação for INCORRECT, descarte o
interno e retorne apenas web_chunks, reproduzindo o fluxo de substituição total do contexto.
Se a ação for AMBIGUOUS, mescle os dois conjuntos e retorne chunks + web_chunks, reproduzindo
o fluxo de complementação. Note que, do jeito que está, não há um ramo explícito
para CORRECT: o código cai no fallback e retorna lista vazia. Corrija isso no seu projeto: quando
a ação for CORRECT, retorne chunks para preservar o contexto interno validado. Além disso,
respeite o comentário do construtor: se você quer desacoplamento real, injete BuscaExterna
no __init__ em vez de instanciar aqui. Mesmo assim, para o entendimento do fluxo, o
essencial é enxergar que esse método traduz o rótulo em política de contexto.
def get_new_chunks(self, action: str, chunks: list[str] | None, query: str | None
= None):
"""Aplica os gatilhos de acao e retorna sempre uma lista de strings (chunks).
"""
busca_externa = BuscaExterna(max_results=5)
web_chunks = busca_externa.buscar_chunks(query)
if action == self.ACTION_INCORRECT:
# Fluxo [INCORRECT]: descarta o interno e busca fontes externas.
return web_chunks
if action == self.ACTION_AMBIGUOUS:
# Fluxo [AMBIGUOUS]: mescla interno com busca externa.
return chunks + web_chunks
# Fallback conservador para rotulos inesperados.
return []
Agora concentre-se no método prompt_evaluator. Entenda que aqui você está especificando
o comportamento do classificador. Primeiro, ele monta o contexto concatenando
os chunks com quebras duplas. Se não houver chunks, ele usa um marcador textual. Em
seguida, ele retorna um prompt em que a instrução força uma saída em conjunto fechado:
CORRECT, INCORRECT ou AMBIGUOUS. Foque no critério: o texto exige informação exata e
suficiente, e reforça que não basta menção temática. Esse detalhe operacionaliza o mesmo
ponto problematizado no artigo: contexto parcialmente relacionado pode induzir a resposta
errada. Garanta que a LLM responda apenas com o rótulo, porque isso simplifica o parsing e
reduz variância. Por fim, injete query e contexto no corpo do prompt.
CAPÍTULO 7. RAG CORRETIVO: CRAG 123
RAG - RETRIEVAL-AUGMENTED GENERATION
def prompt_evaluator(self, query: str, chunks: list[str]) -> str:
"""Monta o prompt para a LLM responder apenas com o rotulo de classificacao."
""
contexto = "\n\n".join(chunks) if chunks else "(sem chunks recuperados)"
return f"""Você é um avaliador rigoroso de precisão factual em um pipeline
CRAG (Corrective Retrieval-Augmented Generation).
Sua função é analisar se os <chunks> fornecem informação EXATA e SUFICIENTE para
responder completamente à <query>, sem depender de conhecimento externo, inferê
ncia adicional ou suposições.
Critério central: SUFICIÊNCIA INFORMATIVA.
Não basta que os <chunks> mencionem o tema ou termos semelhantes à <query>.
Eles devem conter explicitamente os dados necessários para responder à pergunta.
Pense passo a passo antes de decidir:
1. Identifique exatamente o que a <query> exige como resposta.
2. Verifique se os <chunks> contêm essa informação específica.
3. Confirme se a resposta pode ser construída integralmente usando apenas os <chunks
>.
4. Se faltar a informação central, classifique como INCORRECT.
5. Se houver apenas pistas ou contexto parcial, classifique como AMBIGUOUS.
Classificação possível:
- CORRECT:
Os <chunks> contêm a informação exata e suficiente para responder à <query>.
Não é necessário inferência externa.
A resposta pode ser construída diretamente.
- INCORRECT:
Os <chunks> NÃO contêm dados suficientes para responder à <query>,
mesmo que mencionem termos relacionados ou o mesmo assunto.
- AMBIGUOUS:
Os <chunks> são parcialmente relevantes.
Contêm pistas ou contexto relacionado,
mas não informação suficiente para responder completamente à <query>.
Agora avalie:
<query>
{query}
</query>
CAPÍTULO 7. RAG CORRETIVO: CRAG 124
RAG - RETRIEVAL-AUGMENTED GENERATION
<chunks>
{contexto}
</chunks>
Responda somente com UMA das palavras abaixo (sem explicação adicional):
CORRECT
INCORRECT
AMBIGUOUS
"""
7.4 INTEGRANDO A BUSCA EXTERNA
Para realizar uma busca externa por informações usaremos o serviço ’Duck Duck Go’
como mecanismo de expansão de contexto no pipeline. Instancie a classe BuscaExterna
sempre que precisar complementar ou substituir o contexto interno. Defina no construtor
__init__(max_results: int = 5) o número máximo de resultados que deverão ser
considerados. Ajuste esse parâmetro conforme a necessidade de cobertura ou controle de
latência. Esse método público estabelece o limite superior de fontes externas que serão
processadas a cada consulta.
Em seguida, utilize o método público buscar_chunks(query: str) -> list[str].
Passe a consulta original como argumento. Execute esse método sempre que o pipeline exigir
busca externa. Ele retorna uma lista de strings, cada uma representando um chunk textual
extraído da web. Se a consulta estiver vazia ou inválida, o método retorna lista vazia. Caso
contrário, ele realiza a consulta no mecanismo de busca, percorre os resultados e consolida
os conteúdos extraídos.
Durante a execução de buscar_chunks, o fluxo interno consulta o endpoint HTML do
DuckDuckGo, filtra redirecionamentos do próprio domínio, normaliza URLs e realiza leitura
textual básica das páginas encontradas. Em seguida, o conteúdo HTML é limpo, scripts e
estilos são removidos e o texto é normalizado. O tamanho do conteúdo é limitado para manter
controle de contexto e latência. Execute esse método com consciência de que o retorno já
vem pré-processado para consumo posterior.
Por fim, o texto recuperado é segmentado em partes menores por meio da quebra
em chunks semânticos. As sentenças são agrupadas respeitando um tamanho máximo
configurável, garantindo que cada elemento da lista final seja curto, coerente e reutilizável no
contexto do modelo. Ao chamar buscar_chunks, você recebe diretamente essa lista pronta
para ser combinada com o contexto interno do pipeline, sem necessidade de tratamento
CAPÍTULO 7. RAG CORRETIVO: CRAG 125
RAG - RETRIEVAL-AUGMENTED GENERATION
adicional.
import html
import re
from urllib.parse import parse_qs, quote_plus, unquote, urlparse
from urllib.request import Request, urlopen
class BuscaExterna:
"""Serviço de busca externa via DuckDuckGo que retorna chunks textuais."""
def __init__(self, max_results: int = 5):
self.max_results = max_results
def buscar_chunks(self, query: str) -> list[str]:
"""Busca na web com a query original e retorna novos chunks externos."""
if not query.strip():
return []
resultados = self._duckduckgo_search(query, max_results=self.max_results)
chunks_externos = []
for item in resultados:
url = (item.get("url") or "").strip()
if not url:
continue
if self._eh_dominio_duckduckgo(url):
continue
conteudo_site = self._ler_site(url)
if conteudo_site:
chunks_externos.extend(self._quebrar_em_chunks(conteudo_site))
return chunks_externos
def _duckduckgo_search(self, query: str, max_results: int = 5) -> list[dict]:
"""Consulta a web usando DuckDuckGo (endpoint HTML) e retorna resultados
resumidos."""
if not query.strip():
return []
url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
request = Request(
url,
headers={
"User-Agent": (
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari
CAPÍTULO 7. RAG CORRETIVO: CRAG 126
RAG - RETRIEVAL-AUGMENTED GENERATION
/537.36"
)
},
)
try:
with urlopen(request, timeout=10) as response:
pagina = response.read().decode("utf-8", errors="ignore")
except Exception:
return []
links = re.findall(
r’<a[^>]*class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>’,
pagina,
flags=re.IGNORECASE | re.DOTALL,
)
resultados = []
for i, (url_resultado, titulo_html) in enumerate(links[:max_results]):
url_limpa = self._normalizar_url_resultado(html.unescape(url_resultado))
if self._eh_dominio_duckduckgo(url_limpa):
continue
resultados.append(
{
"title": self._limpar_html(titulo_html),
"url": url_limpa,
}
)
return resultados
def _limpar_html(self, texto: str) -> str:
"""Remove tags HTML e normaliza espacos."""
sem_tags = re.sub(r"<[^>]+>", " ", texto or "")
sem_tags = html.unescape(sem_tags)
return re.sub(r"\s+", " ", sem_tags).strip()
def _normalizar_url_resultado(self, url: str) -> str:
"""Converte links de redirecionamento do DuckDuckGo na URL real do site."""
url = (url or "").strip().strip("’\"")
if not url:
return ""
# DuckDuckGo pode retornar URL sem esquema (ex.: //duckduckgo.com/l/?uddg
=...)
if url.startswith("//"):
url = "https:" + url
parsed = urlparse(url)
CAPÍTULO 7. RAG CORRETIVO: CRAG 127
RAG - RETRIEVAL-AUGMENTED GENERATION
# Extrai a URL real quando vier no parametro ‘uddg‘.
if "duckduckgo.com" in (parsed.netloc or "").lower():
params = parse_qs(parsed.query)
uddg = params.get("uddg", [])
if uddg:
destino = unquote(uddg[0]).strip().strip("’\"")
if destino.startswith("//"):
destino = "https:" + destino
return destino
return url
def _eh_dominio_duckduckgo(self, url: str) -> bool:
"""Verifica se a URL ainda aponta para dominio do DuckDuckGo."""
try:
netloc = (urlparse((url or "").strip()).netloc or "").lower()
except Exception:
return False
return "duckduckgo.com" in netloc
def _ler_site(self, url: str) -> str:
"""Lê o conteúdo textual básico de um site e retorna um chunk resumido."""
try:
request = Request(
url,
headers={
"User-Agent": (
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0 Safari
/537.36"
)
},
)
with urlopen(request, timeout=10) as response:
html_site = response.read().decode("utf-8", errors="ignore")
except Exception:
return ""
# Remove blocos que geralmente adicionam ruido.
html_site = re.sub(r"(?is)<script.*?>.*?</script>", " ", html_site)
html_site = re.sub(r"(?is)<style.*?>.*?</style>", " ", html_site)
html_site = re.sub(r"(?is)<noscript.*?>.*?</noscript>", " ", html_site)
texto = self._limpar_html(html_site)
if not texto:
return ""
CAPÍTULO 7. RAG CORRETIVO: CRAG 128
RAG - RETRIEVAL-AUGMENTED GENERATION
# Limita o tamanho para manter latencia/contexto sob controle.
return texto[:2000].strip()
def _quebrar_em_chunks(self, texto: str, tamanho_maximo: int = 300) -> list[str]:
"""Quebra um texto grande em lista de chunks curtos (strings)."""
texto = (texto or "").strip()
if not texto:
return []
# Tenta quebrar por sentencas para manter chunks semanticos.
sentencas = [s.strip() for s in re.split(r"(?<=[.!?])\s+", texto) if s.strip
()]
if not sentencas:
return [texto[:tamanho_maximo]]
chunks = []
atual = ""
for sentenca in sentencas:
if len(sentenca) > tamanho_maximo:
if atual:
chunks.append(atual.strip())
atual = ""
for i in range(0, len(sentenca), tamanho_maximo):
parte = sentenca[i:i + tamanho_maximo].strip()
if parte:
chunks.append(parte)
continue
candidato = f"{atual} {sentenca}".strip() if atual else sentenca
if len(candidato) <= tamanho_maximo:
atual = candidato
else:
if atual:
chunks.append(atual.strip())
atual = sentenca
if atual:
chunks.append(atual.strip())
return chunks
CAPÍTULO 7. RAG CORRETIVO: CRAG 129
RAG - RETRIEVAL-AUGMENTED GENERATION
7.5 EXECUTANDO O CRAG
Agora vamos montar o pipeline completo do CRAG integrando avaliação, decisão e
geração em um fluxo único e controlado. Conecte o recuperador, o avaliador e o mecanismo
de busca externa de forma sequencial, respeitando os gatilhos de ação definidos anteriormente.
Instancie cada componente, passe a query, capture os chunks internos, avalie a suficiência
informativa e, somente então, construa o contexto final que será enviado ao gerador. Siga o
fluxo passo a passo e observe como cada decisão altera o conjunto de evidências antes da
geração da resposta.
Nosso pipeline CRAG completo agora aparece em um script único que orquestra recuperação,
decisão e geração. Comece lendo os imports e entenda que cada classe representa uma
etapa do fluxo: Retriever fornece os chunks iniciais, Augmentation monta o prompt final
com base na query e nos chunks, Generation executa a chamada ao modelo configurado e
Evaluator introduz o mecanismo corretivo. Faça a leitura com a mentalidade de pipeline: o
dado flui de um bloco para o outro, e cada bloco altera o estado do contexto que será usado
na geração.
Em seguida, observe as instanciações. Crie augmentation e retriever como serviços
de longa vida no script. Configure generation com o modelo gemini-3-flash-preview e
mantenha esse valor explícito para facilitar reprodutibilidade. Defina collection_name="starwars"
no Retriever para deixar claro qual índice está sendo consultado. Depois disso, escreva a
query e execute retriever.search(query) para obter os chunks internos. Até aqui, você
está no comportamento clássico: recuperar primeiro, gerar depois, sem qualquer garantia de
que a recuperação sustenta a resposta.
Agora aplique a etapa corretiva. Instancie Evaluator e execute evaluate(query,
chunk) para produzir uma action. Aqui há um detalhe que você precisa corrigir no script
para ele rodar: você recupera a variável chunks, mas chama evaluate passando chunk. Troque
chunk por chunks para que o avaliador receba a lista correta. Em seguida, implemente o
gatilho: se a ação não for ACTION_CORRECT, substitua ou complemente o contexto chamando
get_new_chunks(action=action, chunks=chunks, query=query). Execute essa condição
como o ponto de controle do pipeline: ela evita que a geração seja alimentada por
contexto que não passa no critério de suficiência informativa.
Por fim, gere o prompt final e execute a geração. Chame
augmentation.generate_prompt(query, chunks) to assemble the prompt with the context
already decided by the CRAG. Depois, execute generation.generate(prompt) para
obter a resposta e faça print(response) para inspecionar o output. Leia essa última parte
como a convergência do pipeline: independentemente do fluxo ter sido CORRECT, AMBIGUOUS
CAPÍTULO 7. RAG CORRETIVO: CRAG 130
RAG - RETRIEVAL-AUGMENTED GENERATION
ou INCORRECT, a geração ocorre sempre após a etapa de decisão, e isso mantém a resposta
condicionada ao melhor contexto disponível naquele momento.
#main_busca.py
from retriever import Retriever
from augmentation import Augmentation
from generation import Generation
from evaluator import Evaluator
augmentation = Augmentation()
generation = Generation(model="gemini-3-flash-preview")
retriever = Retriever(collection_name="starwars")
query = "Quem treinou Luke Skywalker inicialmente?"
chunks = retriever.search(query)
# APLIQUE AQUI AVALIADOR CRAG
evaluator = Evaluator()
action = evaluator.evaluate(query, chunk)
if action != evaluator.ACTION_CORRECT:
chunks = evaluator.get_new_chunks(action=action, chunks=chunks, query=query)
prompt = augmentation.generate_prompt(query, chunks)
response = generation.generate(prompt)
print(response)
CAPÍTULO 7.