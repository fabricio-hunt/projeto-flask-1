from flask import Flask, render_template
#mudar a estrutura para orientação a objetos
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console



#chamar a função Flask
app = Flask(__name__)

#criar uma rota
@app.route('/home')
def ola():

    #instanciar os jogos
    jogo1 = Jogo('Super Mario Bros', 'Plataforma', 'SNES')
    jogo2 = Jogo('Castlevania', 'RPG', 'SNES')
    jogo3 = Jogo('Final Fantasy', 'RPG', 'SNES')
    jogo4 = Jogo('Mortal Kombat', 'Luta', 'SNES')

    #criar uma lista de jogos
    lista_de_jogos = [jogo1, jogo2, jogo3, jogo4]
   
    return render_template('lista.html', titulo_home='Jogos',jogos = lista_de_jogos)     

#rodar a aplicação
app.run()