class EstudanteModel:
    def __init__(self, estudante_id, nome, idade):
        self.estudante_id = estudante_id
        self.nome = nome
        self.idade = idade

    def json(self):
        return {
            'estudante_id': self.estudante_id,
            'nome': self.nome,
            'idade': self.idade
        }