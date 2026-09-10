# Especificação Técnica do Problema - SDD

## Problema selecionado
Estudantes frequentemente possuem vários projetos acadêmicos espalhados em pastas, links, documentos e repositórios diferentes. Isso dificulta a apresentação dos trabalhos para professores, avaliadores e oportunidades profissionais.

## Solução proposta
Criar o **PortfolioHUB**, uma aplicação simples para organizar projetos em um portfólio digital, validando se cada projeto possui título, categoria, URL e status válido.

## Requisitos funcionais

- **RF01** - Cadastrar informações básicas de um projeto: título, categoria, URL e status.
- **RF02** - Validar se a URL do projeto possui protocolo HTTP ou HTTPS e domínio válido.
- **RF03** - Listar apenas projetos publicados e válidos.
- **RF04** - Permitir busca de projetos por categoria.
- **RF05** - Calcular a quantidade de projetos publicados em uma categoria.

## Requisitos não funcionais

- **RNF01** - O código deve ser simples, modular e testável.
- **RNF02** - O projeto deve possuir testes automatizados.
- **RNF03** - O ambiente deve ser reprodutível com Docker.
- **RNF04** - O repositório deve conter documentação de instalação, execução e decisões técnicas.
- **RNF05** - O fluxo de desenvolvimento deve evitar commits diretos na branch principal.

## Regras de negócio

- **RN01** - Um projeto sem título não pode ser considerado válido.
- **RN02** - Um projeto sem categoria não pode ser considerado válido.
- **RN03** - Um projeto sem URL válida não pode ser publicado.
- **RN04** - Apenas projetos com status `publicado` devem aparecer na listagem pública.
- **RN05** - A busca por categoria deve ignorar diferenças entre letras maiúsculas e minúsculas.

## Contratos de entrada e saída

### validar_url(url)

Entrada:

```text
url: string
```

Saída:

```text
True se a URL for válida; False caso contrário.
```

### validar_projeto(projeto)

Entrada:

```text
Projeto(titulo, categoria, url, status)
```

Saída:

```text
True se todos os campos obrigatórios forem válidos; False caso contrário.
```

### buscar_por_categoria(projetos, categoria)

Entrada:

```text
lista de projetos e categoria desejada
```

Saída:

```text
lista de projetos publicados pertencentes à categoria informada
```

## Decomposição em unidades

- `Projeto`: estrutura de dados principal.
- `validar_url`: unidade responsável por validar links.
- `validar_projeto`: unidade responsável por validar dados de projeto.
- `listar_projetos_publicados`: unidade responsável por filtrar projetos publicados.
- `buscar_por_categoria`: unidade responsável por localizar projetos por categoria.
- `total_por_categoria`: unidade responsável por agregar a quantidade de projetos por categoria.
