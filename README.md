# PortfolioHUB - Entrega 1: Ambiente, Especificação Técnica e Test Harness

## Visão geral
O **PortfolioHUB** é uma aplicação simples para organizar e validar projetos acadêmicos/profissionais em um portfólio digital. Nesta entrega, o foco é demonstrar ambiente padronizado, especificação técnica no fluxo SDD (Spec-Driven Development), uso documentado de agente de IA e um harness de testes automatizados.

## Governança do projeto
Fluxo de branches recomendado:

- `main`: branch principal, protegida, sem commits diretos.
- `develop`: branch de integração.
- `feature/*`: branches de desenvolvimento por tarefa.

Regras sugeridas:

1. Toda alteração deve sair de uma issue do GitHub Projects.
2. Cada tarefa deve ser feita em uma branch `feature/nome-da-tarefa`.
3. O merge deve acontecer por Pull Request, com revisão de pelo menos um integrante.
4. O pipeline de testes deve passar antes do merge.

## Estrutura do repositório

```text
app/                         Código principal da aplicação
  portfoliohub.py            Regras e funções de validação de projetos

tests/                       Testes automatizados
  test_portfoliohub.py       Casos principais e edge cases

docs/                        Documentação técnica
  especificacao_sdd.md       Especificação do problema, requisitos e contratos
  agentes_ia.md              Configuração e regras dos agentes de IA
  feedback_refinamento.md    Registro de ajustes por feedback
  adrs/                      Decisões arquiteturais
  logs/resultado_testes.txt  Evidência textual de execução dos testes

.github/workflows/tests.yml  Pipeline de testes no GitHub Actions
Dockerfile                   Ambiente padronizado

docker-compose.yml           Execução reprodutível dos testes
requirements-dev.txt         Dependências de desenvolvimento
AGENTS.md                    Diretrizes de contexto para agentes de IA
.cursorrules                 Regras para uso no Cursor/SDD
```

## Instalação local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Execução do test harness

```bash
pytest -v
```

## Execução com ambiente padronizado via Docker

```bash
docker compose up --build
```

## Evidência esperada
Ao executar os testes, o resultado esperado é semelhante a:

```text
7 passed
```

## Links da entrega

- Repositório GitHub: COLE_AQUI_O_LINK_DO_REPOSITORIO
- Integrantes e RA: PREENCHER_NO_RELATORIO_FINAL

  ## Atualização de documentação

Atualização realizada para demonstrar o fluxo de branch e Pull Request da Entrega 1.
