# Meu Dia

Plataforma web de organização pessoal: ajuda o usuário a planejar, priorizar e cumprir o dia de acordo com o tempo que realmente possui.

## Onde o projeto está
- **Etapa 01 - Fundação técnica:** FastAPI + MySQL `agenda` + `/health` + `/health/database` + testes.
- **Etapa 02 - Modelagem do banco:** tabelas `usuarios` e `tarefas` (scripts na pasta `sql/`).
- **Etapa 03 - Backend de usuários (em andamento):** cadastro pronto (`POST /usuarios`). Faltam login e perfil.

## Como rodar (PowerShell, dentro da pasta do projeto)

1. Crie o banco e as tabelas no MySQL (phpMyAdmin ou Workbench), rodando nesta ordem:
   - `sql/01_criar_database.sql`
   - `sql/02_criar_tabelas.sql`

2. Copie `.env.example` para `.env` e preencha usuário/senha do seu MySQL:

       copy .env.example .env

3. Instale as dependências:

       pip install -r requirements.txt

4. Inicie o servidor:

       python -m uvicorn app.main:app --reload

5. Abra no navegador:
   - http://localhost:8000/health
   - http://localhost:8000/health/database
   - http://localhost:8000/docs  (aqui dá para testar o `POST /usuarios`)

## Testes

    python -m pytest

## Segurança
- O arquivo `.env` nunca deve ir para o Git.
- A senha nunca é guardada em texto puro: só o hash (`senha_hash`).
- A API nunca devolve senha.

## Site (frontend)
Com o servidor rodando, abra http://localhost:8000 : cadastro/login, Meu Dia, Minhas tarefas.
Adicione `SECRET_KEY=` (um texto longo e aleatório) no seu `.env`.
