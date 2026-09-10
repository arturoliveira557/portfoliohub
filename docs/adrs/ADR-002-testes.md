# ADR-002 - Pytest como test harness

## Contexto
A entrega exige um harness funcional de testes automatizados.

## Decisão
Foi escolhido o `pytest` por ser simples, amplamente utilizado e fácil de executar localmente ou em pipeline.

## Consequências
Os testes podem ser executados com `pytest -v` localmente, no Docker ou no GitHub Actions.
