# card\bin\activate

from email.policy import default
import os
import csv
from flask import render_template, Flask
#from main import app

app = Flask(__name__)

conteudo = os.listdir("./file")

@app.route('/', defaults={'pages':conteudo})
@app.route('/home/<user>')
def home(pages):
    return render_template('home.html', pages=pages)


@app.route('/componentes-de-hardware/')
def componentes_de_hardware():
    list_quest = []
    with open("./file/Componentes de hardware.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('componentes-de-hardware.html', quest=list_quest)

@app.route('/computacao-em-nuvem/')
def computacao_em_nuvem():
    list_quest = []
    with open("./file/Computação em Nuvem.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computacao-em-nuvem.html', quest=list_quest)

@app.route('/fundamentos-de-redes-de-computadores/')
def fundamentos_de_redes_de_computadores():
    list_quest = []
    with open("./file/Fundamentos de Redes de Computadores.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('fundamentos-de-redes-de-computadores.html', quest=list_quest)

@app.route('/introducao-a-programacao-de-computadores-com-c/')
def introducao_a_programacao_de_computadores_com_c():
    list_quest = []
    with open("./file/Introdução à Programação de Computadores com C.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('introducao-a-programacao-de-computadores-com-c.html', quest=list_quest)

@app.route('/introducao-a-seguranca-da-informacao/')
def introducao_a_seguranca_da_informacao():
    list_quest = []
    with open("./file/Introdução à Segurança da Informação.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('introducao-a-seguranca-da-informacao.html', quest=list_quest)

@app.route('/pensamento-computacional/')
def pensamento_computacional():
    list_quest = []
    with open("./file/Pensamento Computacional.csv", newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('pensamento-computacional.html', quest=list_quest)





if __name__ == '__main__':
    app.run(debug=True)