from flask import Flask
from flask_restful import Api
from resources.estudante import Estudantes, Estudante

app = Flask(__name__)
api = Api(app)

api.add_resource(Estudantes, '/estudantes')
api.add_resource(Estudante, '/estudantes/<int:estudante_id>')

if __name__ == "__main__":
    app.run(debug=True)