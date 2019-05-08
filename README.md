# Stop Down

Repositório para o desenvolvimento de sistema de gerenciamento para escola de aviação. Projeto proposto pela disciplina PCS3216 - Laboratório de Engenharia de Software da Escola Politécnica da USP

# Setup

## Flask + PostgreSQL

Entrar na pasta `api` utilizando o comando `cd api` estando na pasta raíz do repositório e seguir os passos a seguir para fazer o setup do ambiente virtual e do PostgreSQL (requer *python 3.6* e *PostgreSQL 11* instalados).

### Venv

Para fazer o setup do virtualenv, instalar o módulo com `pip install virtualenv`, então criar um ambiente virtual com um dos comandos abaixo (usar o segundo caso o primeiro não funcione):

```{bash}
virtualenv .env
python -m venv .env
```

por fim, é necessário entrar no ambiente criado e instalar as dependências:

```{bash}
source .env/bin/activate (linux)
.env/Scripts/activate (windows)
pip install -r requirements.txt
```

**NOTAS** 

- Para sair do ambiente virtual, bastar rodar o comando `deactivate`.

- Quando for rodar a **API** é importante observar se está dentro do ambiente virtual ou não (se tem um .env entre parenteses)

### PostgreSQL

- Criar um usuário e um banco de dados ambos chamados *stopdown*

- Modificar a senha do usuário *stopdown* para *semtempoirmao*

**NOTA** Os passos acima são necessários para que as credenciais utilizadas para a conexão da API com o banco de dados funcionem

### Rodando a API

- Para rodar a API, basta entrar no ambiente virtual e executar o comando `python manage.py run`. Assim, a API estará rodando em seu localhost, na porta 5000 (localhost:5000)

### Observações

- Pode ser necessário atualizar as dependências da **API** (rodando `pip install -r requirements.txt`) caso novos módulos sejam adicionados ao projeto

## React

Entrar na pasta `web` utilizando o comando `cd web` estando na pasta raíz do repositório e seguir os passos a seguir para fazer o setup do Node.js e React (requer *Node.js 10* e *yarn 1.15* instalados).

- Instalar as dependências usando `yarn install`

- Rodar o servidor do front-end executando o comando `yarn start`. Assim, o servidor estará rodando em localhost:3000