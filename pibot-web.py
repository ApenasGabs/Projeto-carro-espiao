'''
Este codigo foi desenvolvido para fins educativos,
sendo assim vetado o uso comercial ou qualquer outro uso se não o educativo.
Desenvolvido para o projeto de conclusão de curso
© Copyright Gabriel Rodrigues 2019. Todos os Direitos Reservados.
'''
from flask import Flask
from flask import render_template
from flask import request
from threading import Thread

from distancia import setup_sensor, roda_medicao, get_distancia
from control import motor_seteup, movefrente, movetras, esquerda, direita
app = Flask(__name__)   



@app.before_first_request
def _run_on_start():
    setup_sensor()
    motor_seteup()
    t = Thread(target=roda_medicao)
    t.start()

@app.route('/',methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def submit():
    comando=request.form['comando']
    if(comando == 'w'):
        movefrente()
    if(comando == 's'):
        movetras()
    if(comando == 'a'):
        esquerda()
    if(comando == 'd'):
        direita()
    return ('test',204) 

@app.route('/distancia', methods=['GET'])
def distancia():
    return str(get_distancia())



#export FLASK_DEBUG=1
if __name__ == "__main__":
    app.run(host='0.0.0.0') 
