from flask import Flask, render_template
#chamar a função Flask
app = Flask(__name__)

#criar uma rota
@app.route('/home')
def ola():
    return render_template('lista.html')

#rodar a aplicação
app.run()