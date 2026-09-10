# Refinamento por Feedback

## Versão inicial
Na especificação inicial, o sistema apenas armazenaria links de projetos.

## Ajuste 1 - Validação de URL
Após revisão, foi adicionada a regra de que a URL deve possuir protocolo `http://` ou `https://` e um domínio válido.

## Ajuste 2 - Testabilidade
As funções foram separadas em unidades menores para facilitar testes automatizados.

## Ajuste 3 - Casos de borda
Foram incluídos testes para URL sem protocolo, projeto sem título e busca por categoria inexistente.

## Ajuste 4 - Ambiente reprodutível
Foram adicionados Dockerfile e docker-compose.yml para permitir execução padronizada dos testes.
