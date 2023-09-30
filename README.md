# Sistema de Controle de Ambulâncias e Paramédicos 🚑
*(en)* This project is an API built with Django and Django Rest Framework to manage ambulances and paramedics with endpoints to create, list, update, and delete them.

*(pt-br)* Este projeto utiliza o Django e o Django Rest Framework para criar uma API para gerenciar ambulâncias e paramédicos em uma organização de serviços médicos de emergência.

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
- **Postman collections**
- **Swagger**: implementada através da biblioteca drf-yasg. Rotas de acesso:
    - *"/swagger"* - collections
    - *"/redoc"* - documentação



## Requisitos
Antes de começar a utilizar este sistema, certifique-se de ter os seguintes requisitos instalados:
- Docker engine e Docker-compose


## Instruções de Execução

1. Clone este repositório em seu computador:  
```
    git clone https://github.com/AnaJuliaMM/ambulance_API.git
```
</br>

2. Navegue ao diretótio do projeto: 
``` 
    cd ambulance_API
``` 
</br>
</br>


No sistema operacional onde você possui o docker engine e o docker compose, aplique os seguintes comandos:
</br>

3. Construa e inicie os contêineres com Docker Compose: 
```
    docker-compose up -d
```
</br>

4. Crie e aplique migrações no banco de dados: 
```
    docker-compose exec ambulance_api python manage.py makemigrations
    docker-compose exec ambulance_api python manage.py migrate
```
<br>

**Visualize a API em *http://localhost:8000/*** <br>

5. Para desativar, execute o comando a seguir:
```
    docker-compose stop
```

## Opção de Teste
1. Abra seu *postman*
2. Importe o arquivo *API.postman_collection.json*
3. Execute as requisições com os bodies já estruturados


Isso é tudo! 😉





