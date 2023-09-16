# Sistema de Controle de Ambulâncias e Paramédicos 🚑
*(en)*This project is an API built with Django and Django Rest Framework to manage ambulances and paramedics with endpoints to create, list, update and delete them.

*(pt-br)*Este projeto utiliza o Django e o Django Rest Framework para criar uma API para gerenciar ambulâncias e paramédicos em uma organização de serviços médicos de emergência.

## Recursos da API
Este sistema permite o gerenciamento eficiente de ambulâncias e paramédicos, incluindo as seguintes funcionalidades principais:

- Cadastro, atualização e exclusão de ambulâncias.
- Cadastro, atualização e exclusão de paramédicos.
- Associação de paramédicos a ambulâncias.
- Consulta de ambulâncias e paramédicos por meio de endpoints da API.

## Funcionamento 🪛
Quando o usuário acessa uma rota, o arquivo `urls.py`, localizado na pasta do projeto "core", recebe a requisição. Dentro do módulo, uma instância da classe `DefaultRoute` gerencia as rotas relacionando cada *endpoint* com seu respectivo *view*. Nesse projeto, a camada *view* é composta por classes que herdam a classe `ModelViewSet` da biblioteca Django, o que possibilita a utilização da implementação padrão do *Django rest-framework* para lidar com os verbos das requisições e realizar as operações CRUD com o banco de dados. A API possui dois *models*, sendo eles "ParamedicsEntity" e "AmbulanceEntity", sendo que ambas possuem uma relação *one to many*.
Quando necessário, as interação entre as camadas utilizam as classes *serializers* para serialização dos objetos Python para JSON.


## Documentação
A API está documentada em dois níveis
- **Nível de código**: através de comentários e Docstring
- **Collection**: implementada através da biblioteca drf-yasg. Rotas de acesso:
    - *"/swagger"* - collections
    - *"/redoc"* - documentação


## Requisitos

Antes de começar a utilizar este sistema, certifique-se de ter os seguintes requisitos instalados:
- Python 3.11
- Outras dependências do projeto (listadas no arquivo requirements.txt)


## Instruções de Execução

1- Clone este repositório em seu computador:  ```git clone https://github.com/AnaJuliaMM/ambulance_API.git``` </br>
2- Navegue ao diretótio do projeto: `cd ambulance_API`  </br>
3- Crie um ambiente virtual (opcional, mas recomendado): `python -m venv .env`  </br>
4- Ative o ambiente virtual: **window** - `venv\Scripts\activate` | **linux** - `source venv/bin/activate`  </br>
5- Instale as dependências do projeto:  `pip install -r requirements.txt` </br> 

### Configuração do Banco de Dados
1- Abra o arquivo `settings.py` localizado na pasta `SAMU` e configure as configurações do banco de dados de acordo com suas preferências. Por padrão, é usado o SQLite. <br>
2- Execute as migrações para criar as tabelas do banco de dados: `python manage.py migrate`

### Ativando o servidor
1- Inicie o servidor de desenvolvimento, a API Django estará disponível em http://localhost:8000/: `python manage.py runserver` </br>  

### Instrução de Desativação
1- Pare o servidor através do `ctrl+c` </br>
2 - Desative o ambiente virtual: `deactivate`

Isso é tudo! 😉
Se precisar de mais ajuda, consulte a documentação oficial do Django em [Django Documentation](https://docs.djangoproject.com/en/4.2/)





