from flask import Flask, render_template
#chamar a função Flask
app = Flask(__name__)

#criar uma rota
@app.route('/home')
def ola():
    lista_de_jogos = ['God of War', 'Skyrim', 'Valorant']
    return render_template('lista.html', titulo_home='Jogos',jogos = lista_de_jogos)     

#rodar a aplicação
app.run()