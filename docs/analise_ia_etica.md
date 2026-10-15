# Análise Comparativa e Avaliação Crítica de IA

## Ferramentas consideradas
Foram comparadas três ferramentas de apoio ao desenvolvimento: **ChatGPT/Codex**, **Claude Code** e **Cursor**.

| Critério | ChatGPT/Codex | Claude Code | Cursor |
|---|---|---|---|
| Apoio à especificação | Forte para estruturar requisitos, SDD e documentação | Forte em leitura e revisão de bases maiores | Bom quando integrado diretamente ao editor |
| Geração/revisão de código | Boa para propor funções, testes e refatorações | Boa para análise contextual e alterações amplas | Muito ágil para edição no fluxo do IDE |
| Contexto do repositório | Depende do contexto e integrações fornecidas | Pode trabalhar bem com contexto amplo | Aproveita diretamente os arquivos abertos no editor |
| Risco principal | Respostas plausíveis porém incorretas se não houver validação | Alterações amplas podem introduzir efeitos não percebidos | Facilidade de aceitar mudanças rapidamente sem revisão |
| Uso recomendado | Especificação, testes, revisão e documentação | Revisões extensas e análise de arquitetura | Implementação assistida no editor |

## Aplicação no PortfolioHUB
No PortfolioHUB, o ChatGPT/Codex foi usado como apoio para transformar requisitos em especificação SDD, sugerir decomposição em unidades testáveis, criar casos de teste iniciais, revisar documentação e orientar o ambiente padronizado. O resultado gerado por IA não foi tratado como autoridade final: a validação foi feita pelos testes e pela revisão humana.

## Ética, limites e segurança

### 1. Alucinação e código incorreto
Modelos de IA podem produzir código sintaticamente plausível, porém logicamente errado, incompatível com dependências ou fora da especificação. Por isso, toda sugestão deve ser conferida contra a especificação e validada pelo test harness.

### 2. Segurança
Código gerado por IA pode introduzir validações fracas, dependências inadequadas ou comportamentos inseguros. No projeto foi adotada a regra de não inserir senhas, tokens, chaves privadas ou outros segredos no repositório.

### 3. Privacidade e confidencialidade
Não devem ser enviados aos modelos dados pessoais, segredos do projeto ou informações confidenciais sem autorização. O contexto compartilhado deve ser o mínimo necessário para a tarefa.

### 4. Propriedade intelectual e autoria
A IA atua como ferramenta de apoio. A equipe continua responsável pela autoria acadêmica, pela compreensão das decisões e pela compatibilidade do material entregue com as regras da disciplina e eventuais licenças de terceiros.

### 5. Homologação e revisão humana
A revisão humana é obrigatória no fluxo SDD. A IA pode sugerir especificação, código, testes e documentação, mas a decisão de aceitar uma mudança deve passar por testes, inspeção e Pull Request antes do merge.

## Conclusão
Agentes de IA aumentam produtividade, mas não substituem especificação clara, testes automatizados, governança de código e responsabilidade humana. O uso adequado combina assistência da IA com evidências verificáveis e revisão por pessoas.
