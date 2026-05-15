import csv
import os
from flask import Blueprint, render_template

computer_bp = Blueprint('computer-architecture', __name__)

@computer_bp.route('/arquitetura-cisc-x-risc')
def arquitetura_cisc_x_risc():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DIR = os.path.join(BASE_DIR, "file", "Arquitetura de Computadores")

    FILE_PATH = os.path.join(DIR, "Arquitetura CISC X RISC.csv")
    
    list_quest = []
    with open(FILE_PATH, newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/arquitetura-cisc-x-risc.html', quest=list_quest)

@computer_bp.route('/base-computacional')
def base_computacional():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DIR = os.path.join(BASE_DIR, "file", "Arquitetura de Computadores")

    FILE_PATH = os.path.join(DIR, "Base Computacional.csv")
    
    list_quest = []
    with open(FILE_PATH, newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/base-computacional.html', quest=list_quest)

@computer_bp.route('/componentes-de-hardware')
def componentes_de_hardware():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DIR = os.path.join(BASE_DIR, "file", "Arquitetura de Computadores")

    FILE_PATH = os.path.join(DIR, "Componentes de hardware.csv")
    
    list_quest = []
    with open(FILE_PATH, newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/componentes-de-hardware.html', quest=list_quest)

@computer_bp.route('/logica-digital-e-algebra-booleana')
def logica_digital_e_algebra_booleana():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DIR = os.path.join(BASE_DIR, "file", "Arquitetura de Computadores")

    FILE_PATH = os.path.join(DIR, "Lógica Digital e Álgebra Booleana.csv")
    
    list_quest = []
    with open(FILE_PATH, newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/logica-digital-e-algebra-booleana.html', quest=list_quest)

@computer_bp.route('/processamento-em-paralelo')
def processamento_em_paralelo():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DIR = os.path.join(BASE_DIR, "file", "Arquitetura de Computadores")

    FILE_PATH = os.path.join(DIR, "Processamento em Paralelo.csv")
    
    list_quest = []
    with open(FILE_PATH, newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/processamento-em-paralelo.html', quest=list_quest)

@computer_bp.route('/representacao-de-dados')
def representacao_de_dados():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DIR = os.path.join(BASE_DIR, "file", "Arquitetura de Computadores")

    FILE_PATH = os.path.join(DIR, "Representação de dados.csv")
    
    list_quest = []
    with open(FILE_PATH, newline='', encoding="utf-8") as f:
        file = csv.reader(f)
        for row in file:
            list_quest.append(row)
    return render_template('computer-architecture/representacao-de-dados.html', quest=list_quest)