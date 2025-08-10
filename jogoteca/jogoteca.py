from flask import Flask, render_template, request, redirect, session,flash
#mudar a estrutura para orientação a objetos
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Super Mario Bros', 'Plataforma', 'SNES')
jogo2 = Jogo('Castlevania', 'RPG', 'SNES')
jogo3 = Jogo('Final Fantasy', 'RPG', 'SNES')
jogo4 = Jogo('Mortal Kombat', 'Luta', 'SNES')
lista_de_jogos = [jogo1, jogo2, jogo3, jogo4]


app = Flask(__name__)
app.secret_key = 'alura'

@app.route('/')
def index():
    return render_template('lista.html', titulo_home='Jogos',jogos = lista_de_jogos)     

@app.route('/novos-jogos')
def novos_jogos():
    return render_template('novos-jogos.html', titulo='Novos Jogos')


@app.route('/criar', methods=['POST',])
def criar():
    """Recebe dados do formul rio e cria um novo jogo, apos isso renderiza a lista de jogos"""
    nome = request.form['nome']
    categoria = request.form['categoria']    
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(jogo)
    return redirect('/')

#criar uma rota para uma nova página de login
@app.route('/login')
def login():
    return render_template('login.html')

#criar uma rota para autenticar o login
@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'olamundo' == request.form['senha']:
        session['usuario'] = request.form['usuario']
        flash(session['usuario'] + ' logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário ou senha inválidos!')   
        return redirect('/login')

app.run(debug=True)