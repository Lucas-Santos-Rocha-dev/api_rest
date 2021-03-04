from sql_alchemy import banco

class EstudanteModel(banco.Model):
    __tablename__ = 'estudantes'

    estudante_id = banco.Column(banco.Integer, primary_key=True)
    nome = banco.Column(banco.String)
    idade = banco.Column(banco.Integer)
    sexo = banco.Column(banco.String)
    ano_letivo = banco.Column(banco.String)

    def __init__(self, estudante_id, nome, idade, sexo, ano_letivo):
        self.estudante_id = estudante_id
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.ano_letivo = ano_letivo

    def json(self):
        return {
            'estudante_id': self.estudante_id,
            'nome': self.nome,
            'idade': self.idade,
            'sexo': self.sexo,
            'ano_letivo': self.ano_letivo
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

    def update_estudante(self, nome, idade, sexo, ano_letivo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.ano_letivo = ano_letivo

    def delete_hotel(self):
        # deletando o proprio objeto
        banco.session.delete(self)
        banco.session.commit()
