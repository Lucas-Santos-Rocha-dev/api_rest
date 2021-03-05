# Sobre o projeto

Projeto para demonstrar o funcionamento básico de uma API REST desenvolvida em Flask, todas as requisições implementadas na API, foram testadas através da ferramenta [postman](https://www.postman.com/)

# Como executar o projeto

### Pré-requisitos

Antes de começar, é necessário ter instalado as seguintes ferramentas: 
* python versão >= 3
* pacote de instalações python 3 (pip3)

### Dependências

 * Flask == 1.1.2
 * Flask-RESTful==0.3.8
 * Flask-SQLAlchemy==2.4.4

Para instalar as dependências basta ir até a raiz do projeto, abrir o terminal e digitar o seguinte comando:
> pip3 install -r requirements.txt

**Caso ocorra algum erro com o comando acima, tente instalar as dependências, separadamente:**
* pip3 install Flask
* pip3 install Flask-RESTful
* pip3 install Flask-SQLAlchemy

### Rodando o projeto
Após instalação das dependências, vá para a raiz do projeto, abra o terminal e execute o seguinte comando:

#### Linux
> python3 app.py

#### Windows
> py app.py

### Como utilizar a API

#### POST

Faça uma requisição do tipo POST para http://127.0.0.1:5000/estudantes/{id_estudante}
O id_estudante deve ser do tipo númerico, e **deve sempre** ser informado, ex:
> http://127.0.0.1:5000/estudantes/1
##### Os dados devem ter a seguinte estrutura:
``` 
    {
        "nome": "Lucas",
        "idade": 22,
        "sexo": "Masculino",
        "ano_letivo": "1 serie"
    }
```
##### Observações
* Todos os campos são obrigatórios
* Caso algum campo não seja informado, será retornado uma mensagem de erro, informando qual campo está ausente
* Caso o id_estudante informado, ja pertença a algum outro estudante cadastrado, será retornado uma mensagem de erro, informando que não será possível realizar o cadastro

#### PUT
Faça uma requisição do tipo PUT para http://127.0.0.1:5000/estudantes/{id_estudante}
O id_estudante deve ser do tipo númerico, e **deve sempre** ser informado, ex:
> http://127.0.0.1:5000/estudantes/1
##### Os dados devem ter a seguinte estrutura:
``` 
    {
        "nome": "Sabrina",
        "idade": 20,
        "sexo": "Feminino",
        "ano_letivo": "4 serie"
    }
```
##### Observações
* Todos os campos são obrigatórios
* Caso algum campo não seja informado, será retornado uma mensagem de erro, informando qual campo está ausente
* Caso o id_estudante informado não seja encontrado, esse registro será adicionado no banco
* Caso o id_estudante informado seja encontrado, esse registro será atualizado

#### DELETE
Faça uma requisição do tipo DELETE para http://127.0.0.1:5000/estudantes/{id_estudante}
O id_estudante deve ser do tipo númerico, e **deve sempre** ser informado, ex:
> http://127.0.0.1:5000/estudantes/1

##### Observações
* Caso o id_estudante informado não seja encontrado, será retornado uma mensagem informando que o estudante não foi encontrado
* Caso o id_estudante informado seja encontrado, esse registro será deletado

#### GET
* Para retornar todos os estudantes cadastrados, faça uma requisição do tipo GET para http://127.0.0.1:5000/estudantes
* Para retornar um estudante especifico, faça uma requisição do tipo GET para http://127.0.0.1:5000/estudantes/1

##### Observações
* Caso o id_estudante informado não seja encontrado, será retornado uma mensagem informando que o estudante não foi encontrado

### Tecnologias
As seguintes ferramentas foram utilizadas na construção do projeto:
* Python
* Flask
* SQLAlchemy
* Sqlite

### Considerações finais
Optei por desenvolver a API em Flask, pois no dia a dia, desenvolvo a maior parte do tempo em Django, quis demonstrar que apesar de não estar usando no dia a dia, consigo desenvolver em Flask, caso tenha a oportunidade, gostaria de conversar sobre outros projetos em Django e em python que faço parte :)





