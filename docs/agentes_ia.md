# Configuração de Agentes de IA e Ambiente Padronizado

## Ferramenta de IA utilizada
Ferramenta documentada: **ChatGPT / Codex como apoio ao desenvolvimento**. Também é possível adaptar as regras para Cursor, Claude Code, Codex CLI ou outra ferramenta aceita pelo professor.

## Papel do agente
O agente de IA foi usado como apoio para:

- transformar requisitos em especificação SDD;
- sugerir decomposição em unidades testáveis;
- gerar casos de teste iniciais;
- revisar README, documentação e instruções de execução;
- auxiliar na criação de scripts de ambiente padronizado.

## Regras de contexto para o agente

- Seguir a especificação antes de gerar código.
- Não criar funcionalidades fora do escopo definido.
- Priorizar funções pequenas, modulares e testáveis.
- Escrever testes antes ou junto com a implementação.
- Não incluir senhas, tokens ou dados sensíveis no repositório.
- Explicar decisões técnicas no README ou em ADRs.

## Arquivos de agente no repositório

- `AGENTS.md`: instruções gerais para agentes de IA.
- `.cursorrules`: regras equivalentes para uso no Cursor.

## Ambiente padronizado
O ambiente foi padronizado com:

- `requirements-dev.txt` para dependências de teste;
- `Dockerfile` para criar uma imagem reprodutível;
- `docker-compose.yml` para executar o harness com um comando;
- `.github/workflows/tests.yml` para pipeline de testes no GitHub Actions.
