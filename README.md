# PortfolioHUB — Entrega Final

## Visão geral
O **PortfolioHUB** é uma aplicação em Python para organizar e validar projetos acadêmicos/profissionais em um portfólio digital. A solução foi desenvolvida seguindo princípios de SDD (Spec-Driven Development), testes automatizados, documentação de decisões e uso responsável de agentes de IA.

## Funcionalidades
- cadastro lógico de projetos por título, categoria, URL e status;
- validação de URL com HTTP/HTTPS e domínio;
- validação dos campos obrigatórios;
- listagem apenas de projetos válidos e publicados;
- busca por categoria ignorando maiúsculas/minúsculas;
- totalização de projetos publicados por categoria.

## Arquitetura
A aplicação é modular e concentrada em `app/portfoliohub.py`:
- `Projeto`: estrutura de dados;
- `validar_url`: valida links;
- `validar_projeto`: valida os dados de um projeto;
- `listar_projetos_publicados`: filtra projetos publicados e válidos;
- `buscar_por_categoria`: pesquisa por categoria;
- `total_por_categoria`: calcula quantidade por categoria.

As decisões arquiteturais estão registradas em `docs/adrs/`.

## Instalação
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Execução dos testes
```bash
pytest -v
```

Também é possível executar em ambiente padronizado:
```bash
docker compose up --build
```

## Test harness
O projeto possui 7 testes automatizados cobrindo cenários normais e de borda. A evidência registrada em `docs/logs/resultado_testes.txt` mostra **7 passed**, equivalente a 100% dos testes executados com sucesso.

## Governança de código
Fluxo adotado:
1. registrar o trabalho em issue;
2. criar branch `feature/*`;
3. realizar commits objetivos;
4. abrir Pull Request;
5. revisar antes do merge;
6. manter a branch `main` como versão estável.

## Documentação
- `docs/especificacao_sdd.md`: requisitos, regras de negócio e contratos;
- `docs/feedback_refinamento.md`: refinamentos realizados;
- `docs/agentes_ia.md`: uso e regras para agentes de IA;
- `docs/adrs/`: decisões de arquitetura e testes;
- `docs/analise_ia_etica.md`: análise comparativa e técnico-ética;
- `docs/relato_experiencia.md`: aprendizados e desafios;
- `docs/logs/resultado_testes.txt`: evidência de testes.

## Publicação
- Repositório: https://github.com/arturoliveira557/portfoliohub
- GitHub Pages: https://arturoliveira557.github.io/portfoliohub/

## Entrega final
A submissão deve ser feita em **um PDF consolidado** na Sala Online contendo:
- link do repositório público;
- identificação dos integrantes (nome completo e RA);
- relatório de execução dos testes com 100% de passagem;
- seção de análise comparativa e técnico-ética sobre agentes de IA;
- links de Pull Requests relevantes.

> Esta entrega está sendo realizada individualmente. Como não há outro integrante disponível para revisão entre pares, o PR final registra uma auto-revisão transparente e a validação automática pelo GitHub Actions antes do merge.
