from flask_restful import Resource, reqparse
from models.estudante import EstudanteModel

estudantes = [
    {
        'estudante_id': 1,
        'nome': 'Lucas',
        'idade': 22
    },
    {
        'estudante_id': 2,
        'nome': 'Mateus',
        'idade': 25
    }
]

# querys para todos os estudantes
class Estudantes(Resource):
    def get(self):
        return {'estudantes': estudantes}

# querys para um unico estudante
class Estudante(Resource):
    def __init__(self):
        # instanciando reqparse
        self.argumentos = reqparse.RequestParser()

        # importante especificar exatamente o nome esperado como argumento
        self.argumentos.add_argument("nome")
        self.argumentos.add_argument("idade")

    def find_estudante(self, estudante_id):
        for estudante in estudantes:
            if estudante['estudante_id'] == estudante_id:
                return estudante
        return None

    def get(self, estudante_id):
        estudante = self.find_estudante(estudante_id)

        if estudante:
            return estudante
        
        return {'message': 'estudante not found'}, 404 #nto found

    def post(self, estudante_id):
        # dicionario de todos os argumentos passados
        dados = self.argumentos.parse_args()

        # descompactando dicionario utilizando **kwargs
        estudante_objeto = EstudanteModel(estudante_id, **dados)
        novo_estudante = estudante_objeto.json()

        estudantes.append(novo_estudante)
        return novo_estudante, 200 # success

    def put(self, estudante_id):
        # dicionario de todos os argumentos passados
        dados = self.argumentos.parse_args()

        # descompactando dicionario utilizando **kwargs
        estudante_objeto = EstudanteModel(estudante_id, **dados)
        novo_estudante = estudante_objeto.json()

        # procura estudante por id
        estudante = self.find_estudante(estudante_id)

        # caso ja exista o estudante, é realizado o update
        if estudante:
            estudante.update(novo_estudante)
            return novo_estudante, 200 # success

        # caso não exista o estudante, é realizado a inserção
        estudantes.append(novo_estudante)
        return novo_estudante, 201 # created

    def delete(self, estudante_id):
        global estudantes

        estudantes = [estudante for estudante in estudantes if estudante['estudante_id'] != estudante_id]

        return {"message": "estudante deleted"}