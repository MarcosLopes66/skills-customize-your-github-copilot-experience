---
description: "Instruções para usar sempre que criar ou editar arquivos markdown de assignment, garantindo consistência e clareza para os alunos."
applyTo: "assignments/**/*.md"
---

# Diretrizes de Estrutura para Markdowns de Tarefas

Use estas diretrizes ao criar ou editar tarefas em `assignments/`:

## 1. Uso do Template

- Siga a estrutura de [`templates/assignment-template.md`](../../templates/assignment-template.md).
- Salve o conteúdo da tarefa como `README.md` na pasta da atividade.
- Mantenha todas as seções do template; adicione tarefas repetindo a estrutura de tarefa existente.

## 2. Orientação das Seções

Use exatamente os títulos e cabeçalhos do template, incluindo os emojis. Não os traduza nem altere sua capitalização:

- `# 📘 Atividade: [Título da Atividade]` — Use um título curto e descritivo.
- `## 🎯 Objetivo` — Resuma em uma ou duas frases o que o aluno vai construir, praticar ou aprender.
- `## 📝 Tarefas` — Para cada tarefa, use a estrutura abaixo:
   - `### 🛠️ [Título da Tarefa]` — Dê um nome específico e orientado à ação.
   - `#### Descrição` — Explique claramente o que o aluno deve fazer.
   - `#### Requisitos` — Liste em tópicos os resultados esperados, de forma específica e verificável.

Inclua exemplos de entrada e saída em blocos de código quando ajudarem a esclarecer os requisitos. Não acrescente outras seções além das previstas no template, salvo solicitação explícita.