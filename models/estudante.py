from sql_alchemy import banco

class EstudanteModel(banco.Model):
    __tablename__ = 'estudantes'

    estudante_id = banco.Column(banco.Integer, primary_key=True, autoincrement=True)
    nome = banco.Column(banco.String)
    idade = banco.Column(banco.Integer)

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

    # metodo de classe
    @classmethod
    def find_estudante(cls, estudante_id):
        # select * from estudantes where estudante_id = {estudante_id} limit 1
        estudante = cls.query.filter_by(estudante_id=estudante_id).first()
        if estudante:
            return estudante
        return None

    def save_estudante(self):
        # adiciona o proprio objeto
        banco.session.add(self)
        banco.session.commit()
