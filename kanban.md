# 📝 Kanban Board – Sistema de Gerenciamento de Tarefas  

## 📌 Backlog (Requisitos levantados)  
- Usuários criam contas e fazem login com JWT  
- Autenticação e autorização com roles (usuário/admin)  
- CRUD completo de tarefas (criar, ler, atualizar, deletar)  
- Admin pode visualizar todas as tarefas  
- Campos da tarefa: título, descrição, status, prioridade, data de vencimento  
- Filtros e buscas via query params  
- Logs de atividades (criação, edição, exclusão)  
- Validação de dados (tarefas e usuários)  
- Documentação com Swagger/OpenAPI  
- Deploy (Heroku ou AWS)  

---

## ✅ To Do (Próximas tarefas a iniciar)  

### 🔧 Configuração inicial  
- [ ] Criar estrutura de projeto (FastAPI + banco de dados)  
- [ ] Configurar banco de dados (SQLAlchemy ou Prisma + SQLite/Postgres)  
- [ ] Criar models: **User** e **Task**  
- [ ] Configurar autenticação JWT (login/register)  
- [ ] Definir roles (usuário/admin) no model User  

### 📂 Usuários  
- [ ] Criar endpoints de **registro e login**  
- [ ] Proteger rotas com JWT (dependências)  
- [ ] Implementar roles: admin vs. user  

### 🗂️ Tarefas  
- [ ] Criar endpoints CRUD de tarefas  
- [ ] Restringir tarefas por usuário (cada um só vê as suas)  
- [ ] Permitir que admin veja todas  

### 🔍 Funcionalidades extras  
- [ ] Implementar filtros e busca (query params: status, prioridade, data de vencimento)  
- [ ] Adicionar logs de atividades no banco (tabela Logs)  
- [ ] Criar validações com Pydantic (ex: título obrigatório, datas válidas)  

### 📖 Documentação e Deploy  
- [ ] Configurar Swagger automático do FastAPI  
- [ ] Escrever exemplos de requisições e respostas nos endpoints  
- [ ] Preparar Dockerfile e docker-compose (opcional)  
- [ ] Fazer deploy em Heroku ou AWS  

---

## 🚧 In Progress (O que está em andamento)  
- [ ] Estrutura inicial do projeto criada  
- [ ] Banco de dados configurado com SQLAlchemy  

---

## 🏁 Done (Concluído)  
- [x] Requisitos do projeto definidos  
