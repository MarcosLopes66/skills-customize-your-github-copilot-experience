# 📘 Atividade: Construindo APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar tarefas usando o framework FastAPI. Pratique a criação de endpoints, validação de dados com modelos Pydantic e o uso de métodos e códigos de status HTTP.

## 📝 Tarefas

### 🛠️ Criar e Consultar Tarefas

#### Descrição

Complete o código inicial para criar uma API que liste tarefas, consulte uma tarefa pelo identificador e cadastre novas tarefas. Instale as dependências com `python -m pip install fastapi uvicorn`, inicie o servidor com `uvicorn starter-code:app --reload` e use a documentação interativa em `/docs` para testar os endpoints.

#### Requisitos

O programa concluído deve:

- Criar uma aplicação FastAPI e definir modelos Pydantic para os dados de entrada e saída.
- Implementar `GET /tasks` para listar as tarefas armazenadas.
- Implementar `GET /tasks/{task_id}` para consultar uma tarefa pelo identificador.
- Implementar `POST /tasks` para cadastrar uma tarefa com título não vazio e gerar seu identificador.
- Responder à criação com o código de status HTTP `201 Created`.

### 🛠️ Atualizar e Remover Tarefas

#### Descrição

Amplie a API para permitir atualizar parcialmente uma tarefa existente e removê-la. Mantenha os dados em memória durante a execução do servidor.

#### Requisitos

O programa concluído deve:

- Implementar `PATCH /tasks/{task_id}` para atualizar o título, o estado de conclusão ou ambos.
- Implementar `DELETE /tasks/{task_id}` para remover uma tarefa existente e responder com `204 No Content`.
- Responder com `404 Not Found` quando uma operação solicitar um identificador que não existe.
- Validar as requisições e retornar as tarefas no formato definido pelos modelos Pydantic.
- Permitir testar e inspecionar os endpoints pela documentação interativa em `/docs`.
