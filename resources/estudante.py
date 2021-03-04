from flask_restful import Resource, reqparse
from models.estudante import EstudanteModel

# querys para todos os estudantes
class Estudantes(Resource):
    def get(self):
        # retornando todos os estudantes com list comprehension
        return {'estudantes': [estudante.json() for estudante in EstudanteModel.query.all()]}

# querys para um unico estudante
class Estudante(Resource):
    def __init__(self):
        # instanciando reqparse
        self.argumentos = reqparse.RequestParser()

        # importante especificar exatamente o nome esperado como argumento
        self.argumentos.add_argument("nome", type=str, required=True, help="The field 'nome' cannot be left blank")
        self.argumentos.add_argument("idade", type=int, required=True, help="The field 'idade' cannot be left blank")
        self.argumentos.add_argument("sexo", type=str, required=True, help="The field 'sexo' cannot be left blank")
        self.argumentos.add_argument("ano_letivo", type=str, required=True, help="The field 'ano_letivo' cannot be left blank")
    
    def get(self, estudante_id):
        estudante = EstudanteModel.find_estudante(estudante_id)

        if estudante:
            return estudante.json()
        
        return {'message': 'estudante not found'}, 404 # not found

    def post(self, estudante_id):
        # Verificando se o estudante ja existe no banco de dados
        if EstudanteModel.find_estudante(estudante_id):
            return {"message": "Estudante id '{0}' already exists".format(estudante_id)}

        # dicionario de todos os argumentos passados
        dados = self.argumentos.parse_args()

        # descompactando dicionario utilizando **kwargs
        estudante = EstudanteModel(estudante_id, **dados)

        try:
            estudante.save_estudante()
        except:
            return {"message": "An internal error ocurred trying to save estudante"}, 500 # internal server error
        return estudante.json()
        

    def put(self, estudante_id):
        # dicionario de todos os argumentos passados
        dados = self.argumentos.parse_args()

        # procura estudante por id
        estudante_encontrado = EstudanteModel.find_estudante(estudante_id)

        # caso ja exista o estudante, é realizado o update
        if estudante_encontrado:
            # atualizando o objeto
            estudante_encontrado.update_estudante(**dados)

            try:
                estudante_encontrado.save_estudante()
            except:
                return {"message": "An internal error ocurred trying to save estudante"}, 500 # internal server error
            return estudante_encontrado.json(), 200 # success

        # caso não exista o estudante, é realizado a inserção
        # descompactando dicionario utilizando **kwargs
        estudante = EstudanteModel(estudante_id, **dados)
        
        try:
            estudante.save_estudante()
        except:
            return {"message": "An internal error ocurred trying to save estudante"}, 500 # internal server error
        
        return estudante.json(), 201 # created

    def delete(self, estudante_id):
        estudante = EstudanteModel.find_estudante(estudante_id)
        if estudante:
            try:
                estudante.delete_hotel()
            except:
                return {"message": "An internal error ocurred trying to delete estudante"}, 500 # internal server error
            return {"message": "estudante deleted"}

        return {"message": "estudante not found"}, 404