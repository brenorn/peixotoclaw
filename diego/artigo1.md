Nos últimos dias estive estudando e me deparei com esse artigo sobre SDD do blog do Martin Fowler, na verdade um gestor de tecnologia que trabalha comigo me indicou especificamente esse artigo e resolvi adicionar aos itens que estou estudando.

Decidi aplicar na prática o uso de SDD e escolhi como ferramenta o Codex, devido a facilidade de já estar configurado.

A partir daqui vou dar um pouco de contexto e organizar em passos as minhas ações.

Mudanças na forma como produzimos código
Ferramentas como Codex, Devin, Github Copilot, Stackspot, Claude Code, e outras mudaram radicalmente a forma como escrevemos software. Hoje podemos pedir:

“crie uma API de pagamento”

E em pouco tempo recebermos algo funcional, esse padrão ficou conhecido como “vibe coding”, algo como gerar código baseado em prompts soltos.

Mas isso trouxe um novo tipo de problema, passamos a lidar com um volume maior de:

Código inconsistente
Decisões implícitas
Arquitetura frágil
Retrabalho constante
O problema não é a IA em si, mas trago como suspeito a falta de especificações. Dado esse cenário, surge uma abordagem para desenvolvimento de software: Spec Driven Development. Com essa abordagem podemos definir especificações como "fonte da verdade" e gerar código a partir disso.

Mas o que é uma especificação?

Segundo o próprio ChatGPT, uma especificação é:

Especificação é um artefato estruturado que descreve, de forma precisa, testável e não ambígua, o comportamento esperado de um sistema – servindo como fonte de verdade para implementação e validação.

Esse termo está bastante sobrecarregado no momento, uma outra definição idêntica está aqui:

Uma especificação é um artefato estruturado e orientado a comportamento – ou um conjunto de artefatos relacionados – escrito em linguagem natural que expressa a funcionalidade do software e serve como guia para agentes de codificação de IA

Bom, a partir daqui vou usar o Codex Web, da Open AI.

Criando especificações dentro dos repositórios, o Codex vai poder ler os arquivos, executar tarefas seguindo orientações estruturadas e criar testes.

Como usar na prática?
Listei as ações que fiz em alguns passos práticos, serão descritos a seguir.

A estrutura que estou utilizando nesse projeto ficou dessa forma:

/project
  /specs
    spec-1-v1.md
    spec-2-v2.md
  /src
  /tests
  AGENTS.md
1. Criar um arquivo AGENTS.md
O Codex suporta arquivos que guiem seu comportamento, para isso podemos criar um chamado AGENTS.md. Segue o exemplo que usei:

# AGENTS.md

## Regras gerais
- Sempre ler arquivos em /specs antes de implementar
- Nunca implementar sem critérios de aceitação
- Código deve ser simples e legível
- Evitar overengineering

## Fluxo obrigatório
1. Ler as especs do diretório /specs
2. Gerar tasks.md se não existir
3. Implementar baseado nas tasks
4. Criar testes automatizados
5. Garantir que todos os critérios de aceitação passam

## Testes
- Priorizar cobertura dos critérios de aceitação
- Testes devem ser claros e diretos

## Restrições
- Não inventar requisitos não descritos
- Não alterar comportamento sem atualizar spec
2. Criar especs
Neste caso, criei uma espec simples para criar um domínio:

# feature: criação de domínio
 
## requisitos
- um cliente deve ter seu nome, identificador de cliente, data de nascimento, documento que seja  cpf ou cnpj e endereço completo,
- o nome deve ter até 60 caracteres
- o endereço deve ter rua, número, um campo para complemento, bairro, cidade, estado
- a forma de criar um cliente deve ser usando o padrão factory

## regras de negócio
- cpf e cnpj devem seguir as regras de validação brasileira


## critérios de aceitação
- parametros devem ser final
- testes unitários para criação de usuários e validação de campos devem ser criados
3. Usar o Codex como executor
O prompt ficou muito simples:

Implemente a espec /specs/domain/feature-dominio-v1.md

O Codex trabalhou por 2 minutos e 4 segundos, gerando uma branch pra se tornar um PR:

Press enter or click to view image in full size

Após validar, cliquei em "Criar PR" e um PR foi aberto:

Press enter or click to view image in full size

Fiz o merge e após isso criei uma espec para construir uma API usando esse dominio:

# feature: criacao de api

Vamos usar mysql como banco de dados da aplicação, crie a configuração para uso em um servidor local.
Criar uma api que faça as operações de inclusão, exclusão, consulta e atualização de dados de clientes.
Deve seguir o padrão controller > service > domain > repository
Use um arquivo docker com uam imagem do mysql para que o desenvolvedor execeute a apliacação localmente.


## requisitos
- devemos criar a capacidade de salvar, alterar, apagar e consultar os clientes
- não deve existir clientes com o mesmo documento
- retornar 404 para clientes não encontrados, usando ExceptionHandler
- a entrada de dados deve validar campos nulos e em branco

## regras de negócio
- cpf e cnpj devem seguir as regras de validação brasileira

## critérios de aceitação
- parametros devem ser final
- testes unitários para criação de usuários e validação de campos devem ser criados
- testes unitários das controllers
- testes unitários das services
- testes unitários dos repositories
- dockerfile com imagem de mysql para uso local
O Codex trabalhou 3 minutos e 37 segundos para gerar mais um PR:

Press enter or click to view image in full size

Fiz um pequeno ajuste no prompt para que a implementação usasse a classe ClienteFactory que criei na primeira espec de domínio.

Percepções até o momento
O código gerado é bom, deve passar por ajustes, mas no geral usou itens das versões mais novas do java
Gerou os dockerfiles corretamente
Testes unitários fazem sentido
O tempo de execução é pequeno, além da possibilidade de paralelizar tarefas
Uma vez feita a organização de diretórios, fica fácil organizar as especificações
Trabalhar com especificações dá contexto, instruções e principalmente restrições para o Codex, mostrando o que não fazer. Esse ponto é extremamente importante quando estamos falando de consumo de tokens por exemplo.

Insights
AGENTS.md

O arquivo AGENTS.md é o game changer, pois define o comportamento do agente e dá restrições.

Isso transforma o codex em um agente disciplinado.

Loop SDD na prática

Escrevemos spec
Codex gera código
Codex gera testes
Revisamos
Ajustamos a spec (não o código)
Esse é o ponto chave: no SDD, editamos a especificação ao invés da implementação.

Get Marcos’s stories in your inbox
Join Medium for free to get updates from this writer.

Enter your email
Subscribe

Remember me for faster sign in

O agente e as espera devem ter contexto de organização do projeto, como design pattens, arquitetura etc. Percebi isso quando não coloquei e veio uma estrutura de diretórios default. Para corrigir isso, alterei o AGENTS.md e inclui essa definição:

# AGENTS.md

## Regras gerais
- Sempre ler arquivos em /specs antes de implementar
- Nunca implementar sem critérios de aceitação
- Código deve ser simples e legível
- Evitar overengineering
- O projeto segue a arquitetura hexagonal

## Fluxo obrigatório
1. Ler as especs do diretório /specs
2. Gerar tasks.md se não existir
3. Implementar baseado nas tasks
4. Criar testes automatizados
5. Garantir que todos os critérios de aceitação passam

## Testes
- Priorizar cobertura dos critérios de aceitação
- Testes devem ser claros e diretos

## Restrições
- Não inventar requisitos não descritos
- Não alterar comportamento sem atualizar spec
Armadilhas

Spec vaga ou com instruções muito abstratas: "crie um sistema de pagamento" pode fazer com que um projeto frágil seja gerado.
Pular critérios de aceitação: sem isso não existe validação.
Editar código manualmente: esse ato quebra o modelo de SDD.
Usar apenas prompts: SDD exige arquivos de especificação com contexto e definições.
Evoluções
No arquivo AGENTS.md, vou adicionar mais alguns pontos gerais do projeto que devem ser aplicados:

# AGENTS.md

## Stack
- Java 17+
- Spring Boot
- JUnit 5
- Mockito

## Regras gerais
- Sempre ler arquivos em /specs antes de implementar
- Nunca implementar sem critérios de aceitação
- Código deve ser simples e legível
- Evitar overengineering
- O projeto segue a arquitetura hexagonal

## Fluxo obrigatório
1. Ler as especs do diretório /specs
2. Gerar tasks.md se não existir
3. Implementar baseado nas tasks
4. Criar testes automatizados
5. Validar critérios de aceitação

## Testes
- Cobrir todos critérios de aceitação
- Testes devem ser claros e diretos
- O código gerado deve ter 90% de cobertura de testes unitários

## Restrições
- Não inventar requisitos não descritos
- Não alterar comportamento sem atualizar spec
Note que eu adicionei a definição da stack, % de cobertura de testes unitários e arquitetura hexagonal como padrão do projeto.

Ao pedir para que o projeto fosse organizado seguindo arquitetura hexagonal, o projeto foi reorganizado, gerando mais um PR.

Mas fiquei pensando e decidi que seria útil que as especificações fossem geradas por alguma ferramenta de IA generativa, o própriok chatgpt por exemplo. Mas me aprofundando no assunto, percebi que o fluxo ideal seriao seguinte:

Thinking agent → doing agent

Indo mais além, podemos ter

Thinking agent → doing agent → reviewer agent

A partir daqui vou começar a falar sobre a implementação desse fluxo.

Trabalhando com multi agentes
Buscando amadurecer meu uso da abordagem SDD que estou estudando, me aprofundei e vi que podemos usar mais de um agente, e para isso escolhi usar três:

Spec Architect (Thinking Agent) → cria especificações
Software Engineer (Doing Agent) → implementa código
Review Agent (Reviewer Agent) → valida spec, código e testes
A forma prática de fazer isso é definir esses três agentes no arquivo AGENTS.md, e a boa notícia é que o Codex suporta esse modo de trabalho. Sendo assim, segue como organizei os agentes:

# AGENTS.md

Este repositório utiliza desenvolvimento orientado por especificação (Spec-Driven Development - SDD).

Existem dois agentes principais:

1. Spec Architect → responsável pelas especificações
2. Software Engineer → responsável pela implementação

Cada agente possui responsabilidades claras e não deve ultrapassar seu papel.

---

# Agente: Spec Architect

## Missão
Criar e manter especificações claras para cada feature do sistema.

As especificações são a fonte de verdade para o desenvolvimento.

## Responsabilidades

- Criar arquivos dentro do diretório `/specs`
- Definir regras de negócio
- Definir critérios de aceitação
- Definir requisitos funcionais e não funcionais
- Atualizar especificações quando comportamento mudar
- Criar ou atualizar `tasks.md` quando necessário

## Estrutura esperada da spec

Cada feature deve conter:

- Objetivo
- Contexto
- Regras de negócio
- Requisitos funcionais
- Requisitos não funcionais
- Critérios de aceitação
- Casos de erro
- Fora de escopo

## Restrições

- Não escrever código
- Não modificar arquivos em `/src`
- Não modificar arquivos em `/tests`

---

# Agente: Software Engineer

## Missão
Implementar código baseado nas especificações presentes no diretório `/specs`.

Este agente transforma especificações em código funcional e testado.

## Regras gerais

- Sempre ler arquivos em `/specs` antes de implementar
- Nunca implementar sem critérios de aceitação
- Código deve ser simples e legível
- Evitar overengineering

## Fluxo obrigatório

1. Ler as especificações do diretório `/specs`
2. Gerar `tasks.md` se não existir
3. Implementar baseado nas tasks
4. Criar testes automatizados
5. Garantir que todos os critérios de aceitação passam

## Testes

- Priorizar cobertura dos critérios de aceitação
- Testes devem ser claros e diretos
- Cada critério de aceitação deve possuir pelo menos um teste correspondente
- Cada código implementado deve ter 90% de cobertura de testes unitários no mínimo

## Restrições

- Não inventar requisitos não descritos
- Não alterar comportamento sem atualizar spec
- Não modificar arquivos dentro de `/specs`
- Não implementar funcionalidades fora da especificação

## Estrutura esperada do projeto

/specs  
/src  
/tests  

## Critérios de conclusão

Uma feature é considerada concluída quando:

- todos os critérios de aceitação da spec foram implementados
- todos os testes automatizados passam
- o código está simples e legível
- nenhum requisito fora da spec foi adicionado


# Agente: Review Agent

## Missão
Validar que a implementação segue fielmente a especificação.

Este agente atua como revisor técnico e garante qualidade antes da conclusão da feature.

## Responsabilidades

- Comparar código com as especificações em `/specs`
- Validar que todos os critérios de aceitação foram implementados
- Verificar se os testes cobrem os critérios de aceitação
- Identificar inconsistências entre spec e implementação
- Sugerir melhorias de clareza ou simplificação

## Verificações obrigatórias

O Review Agent deve verificar:

1. Se a implementação corresponde à especificação
2. Se todos os critérios de aceitação possuem testes
3. Se não existem funcionalidades fora da spec
4. Se o código segue boas práticas de legibilidade
5. Se não existe complexidade desnecessária

## Resultado da revisão

A revisão deve produzir um relatório contendo:

- Conformidade com a spec
- Critérios de aceitação atendidos
- Gaps encontrados
- Sugestões de melhoria

Se problemas forem encontrados, o agente deve solicitar correção antes da conclusão da feature.

## Estrutura esperada do projeto

/specs  
/src  
/tests  

## Fluxo completo de desenvolvimento

1. Spec Architect cria ou atualiza a especificação
2. Software Engineer implementa a feature
3. Software Engineer cria testes automatizados
4. Review Agent valida aderência à spec
5. Correções são feitas se necessário
6. Feature é considerada concluída após aprovação do Review Agent

## Critérios de conclusão

Uma feature é considerada concluída quando:

- Todos os critérios de aceitação foram implementados
- Todos os testes automatizados passam
- Não existem divergências entre código e spec
- O Review Agent aprovou a implementação
Após isso, fui ao prompt do Codex e iniciei meu fluxo de trabalho, pedindo a inclusão de mais um campo em uma classe de domínio:

Atue como Spec Architect e crie a especificação para a feature 
"adicionar estado civil a entidade cliente"
O resultado esperado é ter uma spec gerada, o que de fato aconteceu aqui:

Press enter or click to view image in full size

Depois de ler a especificação, concordei com ela e pedi a implementação:

Atue como Software Engineer e implemente a feature-estado-civil-cliente-v1 
baseado nas especificações em /specs.
Observei o conteúdo gerado, primeiro tivemos as tasks:

Press enter or click to view image in full size

Logo depois a implementação:

Press enter or click to view image in full size

Agora vou pedir a validação disso para o nosso terceiro agente:

Atue como Review Agent e valide se o código segue a especificação em /specs.
Gostei do resultado, pois mostrou gaps e trouxe sugestões:

Press enter or click to view image in full size

Baixei o código em minha máquina e está compilando, vou fazer mais alguns ajustes nas especificações futuramente, mas quero falar de outra coisa: eu separei em três passos explícitos, mas podemos usar apenas um prompt para ter esse fluxo rodando, exemplo:

Execute Spec Architect para criar especs, depois Software Engineer para implementar, depois Review Agent para revisar e corrija qualquer problema encontrado para entregar os seguintes itens:

- configurar o jaConfigurar JaCoCo no Maven e gerar relatório para comprovar o critério de cobertura mínima. 
- Complementar testes para cobrir explicitamente fluxos de update/delete no controller/service
- atualizar as especs para colocar estado civil como requisito nas especs já criadas
- adicionar nome da mãe ao cadastro de cliente
O esperado é que executemos o Spec Architect, Software Engineer e por fim o Reviewer Agent.

Aqui podemos ver as tasks que foram criadas:

## feature-nome-mae-cliente-v1
- [x] Adicionar nome da mãe ao domínio de Cliente com validação de obrigatoriedade e limite de 60 caracteres.
- [x] Persistir nome da mãe na entidade JPA de cliente.
- [x] Expor nome da mãe nos contratos da API (request/response).
- [x] Atualizar service/factory para mapear nome da mãe na criação e atualização.
- [x] Criar testes automatizados cobrindo cenário válido e inválido para nome da mãe.

## feature-arquitetura-hexagonal-e-cobertura
- [x] Configurar JaCoCo no Maven para geração de relatório e validação de cobertura mínima de 90%.
- [x] Complementar testes para fluxos de update e delete no controller.
- [x] Complementar testes para fluxos de update e delete no service.
- [x] Atualizar especificações para explicitar estado civil como requisito.
Testes unitários também foram criados e atualizados para a nova modifição:

Press enter or click to view image in full size

Press enter or click to view image in full size

Feito isso, temos um workflow de agentes criados e tive mais um insight:

No Codex Web você não cria agentes como serviços separados. O modelo é:

AGENTS.md = definição de papéis
Prompt = agente ativo
Ou seja:

o arquivo define como os agentes trabalham
o prompt define qual agente está ativo naquele momento
Por isso a importância de estruturar um prompt parecido com esse (pelo menos nas primeiras instruções):

Execute Spec Architect para criar especs, depois Software Engineer 
para implementar, depois Review Agent para revisar e corrija qualquer 
problema encontrado para entregar os seguintes itens:

- configurar o jaConfigurar JaCoCo no Maven e gerar relatório para comprovar 
  o critério de cobertura mínima. 
- Complementar testes para cobrir explicitamente fluxos de update/delete 
no controller/service
- atualizar as especs para colocar estado civil como requisito nas especs 
já criadas
- adicionar nome da mãe ao cadastro de cliente
Assim teremos os agentes sendo executados e trabalhando em conjunto para entregar as tarefas solicitadas.

Aqui paramos num nível avançado de uso de Spec Driven Development, mas será que é o mais completo? Ainda temos a possibilidade de fazer os Pull Requests serem criados automaticamente e adicionar mais dois agentes, ficando com o seguinte fluxo:

Product Agent → Spec Architect → Software Engineer → Review Agent → Refactor Agent

Confesso que me interessei pelo assunto e continuarei a evoluir essa abordagem de desenvolvimento de software usando ferramentas de Inteligência Artificial.

Até o próximo texto com a inclusão de mais agentes.

Valeu!