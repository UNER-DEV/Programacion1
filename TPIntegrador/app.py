# ========================================================== #
#  IMPORTS                                                   #
# ========================================================== #
from flask import Flask, render_template,request
from werkzeug.exceptions import HTTPException
import json
import os
import random as rdm
from datetime import datetime
#import time

# ========================================================== #
#  VARIABLES                                                 #
# ========================================================== #
app = Flask(__name__)
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "db", "db.json")
dataLocal = json.load(open(json_url))
step = 1
user = ''
start = ''
end = ''
life = 3
score = 0
datos = ["Usuario", "Puntaje", "Tiempo_Inicio", "Tiempo_Fin"]
file_name = 'db\savedScores.json'
pregunta = ["pregunta","a","b","c","d","respuesta"]

# ========================================================== #
#  FUNCIONES                                                 #
# ========================================================== #
def refresh_all():
    global step 
    global user 
    global start 
    global end 
    global life 
    global score 
    step = 1
    user = ''
    start = ''
    end = ''
    life = 3
    score = 0

def refresh_game():
    global step 
    global start 
    global life 
    global score 
    step = 1
    start = datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    life = 3
    score = 0

def pregEscalones(data):
    global step
    if step <= 8:
        escalon = data[str(step)]
        choice = escalon[rdm.randint(0, len(data[str(step)]) - 1 )]
    return choice

def saveScore():
    global user
    global score
    global life
    global start
    global end
    global file_name 
    print(start)
    date = datetime.now()
    end = date.strftime("%H:%M:%S %d/%m/%Y")
    entry = {datos[0]: user, datos[1]: score + life, datos[2]: start, datos[3]: end,}
    data = []
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("JSON Vacio")
    except FileNotFoundError:
        print("No existe el JSON")
    data.append(entry)
    with open(file_name, "w") as file:
        json.dump(data, file, indent = 4)

# ========================================================== #
#  RUTAS Y RENDERIZADO                                       #
# ========================================================== #

def settingsGame():
    reloadGame = request.form('reloadGame')
    if(reloadGame):
        refresh_game()
        return render_template('question.html', data = pregEscalones(dataLocal), step = step, user = user, life = life)

@app.route('/')
def index():
    return render_template('index.html') #Flask busca, por defecto la ruta de las plantillas.

@app.route('/home', methods=['POST'])
def handle_user():
    global user
    global start
    user =  request.form['inputUser']
    if(len(user) > 10):
        return render_template('index.html', error= "El usuario es muy largo. Ingrese 10 carácteres como máximo.")
    elif(user != ''):
        return render_template('home.html',  user = user )
    date = datetime.now()
    start = date.strftime("%H:%M:%S %d/%m/%Y")
    return render_template('index.html', error= "No se ingresó un usuario")

@app.route('/exit', methods=['POST'])
def exit():
    exit = request.form['exit']
    if(exit):
        refresh_all()
        return render_template('index.html')

@app.route('/añadirPregunta', methods=['POST'])
def addQuestion():
    try:
        question=request.form['questionInput']
        optionA=request.form['questionOptionA'] 
        optionB=request.form['questionOptionB'] 
        optionC=request.form['questionOptionC'] 
        optionD=request.form['questionOptionD']
        respCorrecta=request.form[str(request.form['respuestaSelector'])]  
        escalon=request.form['escalonSelector'] 
        entry={pregunta[0]: question, pregunta[1]: optionA, pregunta[2]: optionB, pregunta[3]: optionC,pregunta[4]: optionD,pregunta[5]: respCorrecta }
        try:
            with open("db/db.json", "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            print("JSON Vacio")
        data[escalon].append(entry)
        with open("db/db.json", "w") as file:
            json.dump(data, file, indent = 4)   
    except:
        return render_template('addQuestion.html', error="*Recuerde que debe llenar todos los campos para continuar")
    return render_template('addQuestion.html')

@app.route('/consultaPuntajes', methods=['POST'])
def queryScores():
    data = []
    print(file_name)
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except:
        print("JSON Vacio")
    return render_template('queryGame.html', data = data, len = len(data))

@app.route('/resultado')
def finalResult():
    saveScore()
    return render_template('result.html')

@app.route('/preguntas', methods=['POST'])
def handle_data():
    global step
    global user
    global life
    global score
    try:
        value = request.form['option']
        correcto = request.form['correcto']
        if(value == correcto):
            score += 1
            step = int(request.form['btnNext']) + 1
            if(step <= 8):
                return render_template('question.html', data = pregEscalones(dataLocal), step = str(step), user = user, life = life)
            return render_template('result.html')
        else:
            print(life)
            if(life > 1):
                life -= 1
                return render_template('question.html', data = pregEscalones(dataLocal), step = str(step), user = user, life = life)
            else:
                return finalResult()
    except HTTPException:
        print('Saca la mano de ahi carajo')
        return render_template('question.html', data = pregEscalones(dataLocal), step = str(step), user = user, life = life)

@app.route('/reload', methods=['POST'])
def settings_game():
    reloadGame = request.form['reloadGame']
    if(reloadGame):
        refresh_game()
        global step
        global user
        return render_template('question.html', data = pregEscalones(dataLocal), step = step, user = user, life = life)

@app.route('/reloadGames', methods=['POST'])
def settings_home():
    reloadHome = request.form['reloadHome']    
    if(reloadHome):
        refresh_game()
        global user
        if(user != ''):
            return render_template('home.html', user = user)
        return render_template('index.html')


# ========================================================== #
#  EJECUCION DEL SERVIDOR                                    #
# ========================================================== #
if __name__ == '__main__':
    app.run(debug=True) #app.run() ==> Debo quitar luego para no reiniciar server