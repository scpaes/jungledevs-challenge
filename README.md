# jungledevs-challenge
Jungle Devs - Django Challenge #001

#### Postman Collection

#### Documentação com swagger `/swagger/`


### Instruções para execução do projeto usando o Docker compose.
Requisitos:
- Python3
- Docker

#### Ambiente de desenvolvimento

Utilizando o servidor padrão de desenvolvimento do django.
- Verificar as variaveis de ambiente, contidas no arquivo `.env.dev`
- Fazer o build da imagem e executar o container.
`$ docker-compose up -d --build`

#### Ambiente de produção
Utilizando o gunicorn e o nginx
- Verificar as variaveis de ambiente, contidas no arquivo `.env.prod`
- Fazer o build da imagem e executar o container.

    ```sh
    $ docker-compose up -d --build
    ```
#### Secret key
- Gerar as chaves e informar nos arquivos .env.dev e .env.prod 
