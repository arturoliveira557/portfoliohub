# Relato de Experiência

O desenvolvimento do PortfolioHUB permitiu aplicar, em uma mesma atividade, especificação orientada a requisitos, implementação modular, testes automatizados, versionamento e documentação.

## Principais aprendizados
- transformar um problema amplo em requisitos e funções pequenas;
- manter rastreabilidade entre especificação, implementação e testes;
- utilizar branches e Pull Requests para reduzir alterações diretas na versão principal;
- registrar decisões técnicas em ADRs;
- usar IA como apoio, mantendo validação humana e testes como critérios de aceitação.

## Principais desafios
Um dos principais desafios foi garantir que a implementação permanecesse alinhada à especificação durante os refinamentos. A inclusão de validação de URL, casos de borda e ambiente reprodutível mostrou como testes e feedback podem exigir re-especificação.

Outro desafio foi organizar a governança do repositório. O fluxo com feature branch, Pull Request e revisão deixa o histórico mais compreensível e reduz o risco de alterações sem validação.

## Resultado
O test harness possui sete casos cobrindo validação de URL, campos obrigatórios, publicação, busca por categoria e caso sem resultado. A execução registrada apresenta sete testes aprovados.

## Uso de IA
A IA foi utilizada como apoio para especificação, decomposição, testes e documentação. As sugestões foram tratadas como propostas e não como respostas automaticamente corretas. A responsabilidade final permaneceu com a equipe por meio de testes, inspeção e revisão.
