# ========================================================== #
#  IMPORTS                                                   #
# ========================================================== #
from flask import Flask, render_template,request
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
score = 0
datos = ["Usuario", "Puntaje", "Tiempo_Inicio", "Tiempo_Fin"]
file_name = 'savedScores.json'

# ========================================================== #
#  FUNCIONES                                                 #
# ========================================================== #
def pregEscalones(data):
    global step
    if step <=8:
        escalon = data[str(step)]
        choice = escalon[rdm.randint(0, len(data[str(step)])-1 )]
    return choice

def settingsGame():
    reloadGame=request.form('reloadGame')
    if(reloadGame):
        global step
        step = 1
        return render_template('question.html', data=pregEscalones(dataLocal),step=step, user=user )


# ========================================================== #
#  RUTAS Y RENDERIZADO                                       #
# ========================================================== #
@app.route('/')
def index():
    return render_template('index.html') #Flask busca, por defecto la ruta de las plantillas.

@app.route('/home', methods=['POST'])
def handle_user():
    global user
    user =  request.form['inputUser']
    if(len(user)>10):
        return render_template('index.html' , error= "El usuario es muy largo. Ingrese 10 carácteres como máximo.")
    elif(user!=''):
        return render_template('home.html',  user=user )
    global start
    date = datetime.now()
    start = date.strftime("%H:%M:%S %d/%m/%Y")
    return render_template('index.html' , error= "No se ingresó un usuario")

@app.route('/exit', methods=['POST'])
def exit():
    exit=request.form['exit']
    if(exit):
        global step
        global user
        user=''
        step=1
        return render_template('index.html',  user=user )

@app.route('/añadirPregunta')
def addQuestion():
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
    return render_template('queryGame.html', data=data, len = len(data))

@app.route('/resultado')
def finalResult():
    date = datetime.now()
    global end
    global start
    end = date.strftime("%H:%M:%S %d/%m/%Y")
    entry ={datos[0]: user, datos[1]: score, datos[2]: start, datos[3]: end, }
    data = []
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("JSON Vacio")
    data.append(entry)
    with open(file_name, "w") as file:
        json.dump(data, file, indent = 4)
    return render_template('result.html')

@app.route('/preguntas', methods=['POST'])
def handle_data():
    global step
    try:
        value = request.form['option']
        correcto = request.form['correcto']
        if(value==correcto):
            step = int(request.form['btnNext']) + 1
            if(step<=8):
                return render_template('question.html', data=pregEscalones(dataLocal),step=str(step),user=user )
            return render_template('result.html')
        else:
            return render_template('question.html', data=pregEscalones(dataLocal),step=str(step),user=user )
    except:
        print('Saca la mano de ahi carajo')
        return render_template('question.html', data=pregEscalones(dataLocal),step=str(step),user=user )

@app.route('/reload', methods=['POST'])
def settings_game():
    reloadGame=request.form['reloadGame']
    if(reloadGame):
        global step
        step = 1
        return render_template('question.html', data=pregEscalones(dataLocal),step=step,user=user )

@app.route('/reloadGames', methods=['POST'])
def settings_home():
    reloadHome=request.form['reloadHome']    
    if(reloadHome):
        global step
        step = 1
        if(user!=''):
            return render_template('home.html' , user=user)
        return render_template('index.html')


# ========================================================== #
#  EJECUCION DEL SERVIDOR                                    #
# ========================================================== #
if __name__ == '__main__':
    app.run(debug=True) #app.run() ==> Debo quitar luego para no reiniciar server