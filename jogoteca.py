from flask import Flask
#chamar a função Flask
app = Flask(__name__)

#criar uma rota
@app.route('/home')
def ola():
    return '<h1>Bem vindo ao site Jogoteca</h1>'     

#rodar a aplicação
app.run()