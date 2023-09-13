# Sistema de Controle de Ambulâncias e Paramédicos
Este projeto utiliza o Django e o Django Rest Framework para criar uma API para gerenciar ambulâncias e paramédicos em uma organização de serviços médicos de emergência.

## Recursos da API
Este sistema permite o gerenciamento eficiente de ambulâncias e paramédicos, incluindo as seguintes funcionalidades principais:

- Cadastro, atualização e exclusão de ambulâncias.
- Cadastro, atualização e exclusão de paramédicos.
- Associação de paramédicos a ambulâncias.
- Consulta de ambulâncias e paramédicos por meio de endpoints da API.

## Funcionamento
Quando o usuário acessa uma rota, o arquivo `urls.py`, localizado na pasta do projeto "core", recebe a requisição. Dentro do módulo, uma instância da classe `DefaultRoute` gerencia as rotas relacionando cada *endpoint* com seu respectivo *view*. Nesse projeto, a camada *view* é composta por classes que herdam a classe `ModelViewSet` da biblioteca Django, o que possibilita a utilização da implementação padrão do *Django rest-framework* para lidar com os verbos das requisições e realizar as operações CRUD com o banco de dados. A API possui dois *models*, sendo eles "ParamedicsEntity" e "AmbulanceEntity", sendo que ambas possuem uma relação *one to many*.
Quando necessário, as interação entre as camadas utilizam as classes *serializers* para serialização dos objetos Python para JSON.


## Documentação
A API está documentada em dois níveis
- Nível de código: através de comentários e Docstring
- Collection: implementada através da biblioteca drf-yasg. Rotas de acesso:
    - *"url/swagger"* - collections
    - *"url/redoc"* - documentação


## Requisitos

Antes de começar a utilizar este sistema, certifique-se de ter os seguintes requisitos instalados:
- Python 3.11
- Outras dependências do projeto (listadas no arquivo requirements.txt)





