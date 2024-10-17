## Teste Django - Controle de Tarefas e Registro de Tempo

Este projeto é uma aplicação web para o controle de tarefas e registro de tempo de trabalho. Foi desenvolvido utilizando o framework Django. O sistema permite o cadastro de tarefas, registro de tempo associado às tarefas e oferece funcionalidades de listagem e filtros sobre o tempo de trabalho cadastrado por cada usuário.

## Funcionalidades

- **Cadastro de Tarefas**: O usuário pode cadastrar novas tarefas, definindo título, descrição e horários de início e término.
- **Registro de Tempo**: Permite que o usuário registre o tempo gasto em uma tarefa.
- **Listagem e Filtros**: Possui uma listagem das tarefas e permite que o usuário filtre e pesquise pelas tarefas cadastradas.
- **Gerenciamento de Usuários**: O admin pode gerenciar os usuários, promovendo ou rebaixando sua permissão de admin, além de excluir usuários.
- **Sistema de Login e Registro**: Possui funcionalidades de login e registro de usuários.

## Estrutura do Projeto

```bash
.
├── tarefa_app                   # App principal da aplicação Django
│   ├── __pycache__              # Arquivos cache do Python
│   ├── asgi.py                  # Configuração do ASGI
│   ├── settings.py              # Configurações do projeto
│   ├── urls.py                  # Configurações de rotas do projeto
│   ├── wsgi.py                  # Configuração do WSGI
├── tarefas                      # App de gerenciamento de tarefas
│   ├── __pycache__              # Arquivos cache do Python
│   ├── migrations               # Migrações de banco de dados
│   │   ├── __pycache__
│   │   ├── 0001_initial.py      # Migração inicial do banco
│   │   ├── 0002_remove_task_fim_remove_task_inicio_timeentry.py
│   │   ├── 0003_task_fim_task_inicio.py
│   │   ├── 0004_task_titulo.py
│   ├── static                   # Arquivos estáticos (CSS)
│   │   ├── tarefas
│   │       └── css
│   │           └── style.css    # Estilos do projeto
│   ├── templates                # Templates HTML do projeto
│   │   ├── tarefas
│   │       ├── base.html        # Template base
│   │       ├── create_task.html # Template de criação de tarefa
│   │       ├── create_time_entry.html # Template de criação de registro de tempo
│   │       ├── delete_task.html # Template de exclusão de tarefa
│   │       ├── delete_user.html # Template de exclusão de usuário
│   │       ├── edit_task.html   # Template de edição de tarefa
│   │       ├── home.html        # Página inicial
│   │       ├── login.html       # Tela de login
│   │       ├── manage_users.html # Gerenciamento de usuários
│   │       ├── register.html    # Tela de registro de usuário
│   │       ├── tasks.html       # Listagem de tarefas
│   │       ├── time_entries.html # Listagem de registros de tempo
│   ├── admin.py                 # Configurações do admin Django
│   ├── apps.py                  # Configurações do app
│   ├── filters.py               # Filtros para as tarefas
│   ├── forms.py                 # Formulários do projeto
│   ├── models.py                # Modelos de banco de dados
│   ├── tests.py                 # Testes automatizados
│   ├── urls.py                  # Rotas do app de tarefas
│   ├── views.py                 # Lógica das views
├── db.sqlite3                   # Banco de dados SQLite
├── manage.py                    # Script de gerenciamento do Django
├── README.md                    # Documentação do projeto
├── requirements.txt             # Dependências do projeto
├── venv                         # Ambiente virtual Python
```

## Requisitos Técnicos

### Dependências do Projeto

As dependências estão listadas no arquivo `requirements.txt`. Utilize o comando abaixo para instalar:

```bash
pip install -r requirements.txt
```

### Tecnologias Utilizadas

- **Python 3.11.5**
- **Django 5.1.2**
- **SQLite**: Banco de dados padrão para desenvolvimento.
- **Django Filters**: Para filtros avançados de listagem.

## Configuração e Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/douglas-s29/teste_django.git
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

- No Windows:

```bash
venv\Scripts\activate
```

- No Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Crie um superusuário

```bash
python manage.py createsuperuser
```

Siga as instruções e crie o usuário admin.

### 7. Execute o servidor local

```bash
python manage.py runserver
```

Acesse a aplicação em [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Funcionalidades

### 1. **Cadastro de Tarefas**

O usuário pode cadastrar uma nova tarefa com os seguintes campos:
- Título
- Descrição
- Data e Hora de Início
- Data e Hora de Fim (Opcional)

### 2. **Registro de Tempo**

O usuário pode registrar o tempo gasto em cada tarefa e visualizar o tempo total na listagem de tarefas.

### 3. **Listagem de Tarefas**

Na página de tarefas, o usuário pode visualizar suas tarefas, pesquisar por tarefas específicas e ver o tempo gasto em cada tarefa. A listagem inclui:
- ID da Tarefa
- Título
- Descrição
- Usuário responsável
- Data de Criação
- Horários de Início e Fim
- Tempo Gasto

### 4. **Gerenciamento de Usuários (Admin)**

Usuários com permissões de administrador podem:
- Ver a listagem de todos os usuários
- Excluir usuários
- Promover ou rebaixar um usuário para admin

## Autenticação

A aplicação inclui um sistema de autenticação completo:
- Login
- Logout
- Registro de usuários
- Mensagens de erro e validação no formulário de login

## Filtros e Pesquisa

Os filtros permitem buscar tarefas por título, descrição, usuário, ou data de criação. A busca é feita diretamente no campo de pesquisa, retornando resultados filtrados com base nos critérios inseridos.

## Informações de Acesso

Ao iniciar o projeto, você pode utilizar o seguinte usuário para acessar a aplicação:

- **Login**: `admin`
- **Senha**: `admin`

Esse usuário tem permissões de administrador e pode gerenciar tarefas e usuários.