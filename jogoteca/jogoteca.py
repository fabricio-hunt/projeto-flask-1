from flask import Flask, render_template, request, redirect, session, flash, url_for
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
    if 'usuario'not in session or session['usuario'] == None:
        return redirect('/login?proxima=novos-jogos')
    return render_template('novos-jogos.html', titulo='Novos Jogos')


@app.route('/criar', methods=['POST',])
def criar():
    """Recebe dados do formulário e cria um novo jogo, apos isso renderiza a lista de jogos"""
    nome = request.form['nome']
    categoria = request.form['categoria']    
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(jogo)
    return redirect(url_for('index'))
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'olamundo' == request.form['senha']:
        session['usuario'] = request.form['usuario']
        flash(session['usuario'] + ' logado com sucesso!')
        
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Usuário ou senha inválidos!')   
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['usuario'] = None
    flash('Usuário deslogado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True)