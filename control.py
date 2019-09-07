'''
Este codigo foi desenvolvido para fins educativos,
sendo assim vetado o uso comercial ou qualquer outro uso se não o educativo.
Desenvolvido para o projeto de conclusão de curso
© Copyright Gabriel Rodrigues 2019. Todos os Direitos Reservados.
'''
import RPi.GPIO as GPIO
import time
import getch

GPIO.setmode(GPIO.BOARD)  # usando num dos pinos ao invez dos gpios
GPIO.setwarnings(False)

FRENTE = 31  # Mapeamento dos motores
TRAS = 29
ESQUERDA = 35
DIREITA = 33


def motor_seteup():
    GPIO.setup(FRENTE, GPIO.OUT)
    GPIO.setup(TRAS, GPIO.OUT)
    GPIO.setup(ESQUERDA, GPIO.OUT)
    GPIO.setup(DIREITA, GPIO.OUT)


def movefrente():  # fazendo ele ir para frente
    GPIO.output(FRENTE, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(FRENTE, GPIO.LOW)

def movetras():  # fazendo ele ir para tras
    GPIO.output(TRAS, GPIO.HIGH)
    time.sleep(0.04)
    GPIO.output(TRAS, GPIO.LOW)

def esquerda():  # somente motor dianteiro para curvas
    GPIO.output(ESQUERDA, GPIO.HIGH)
    time.sleep(0.04)
    GPIO.output(ESQUERDA, GPIO.LOW)
      


def direita():  # somente motor dianteiro para curvas
    GPIO.output(DIREITA, GPIO.HIGH)
    time.sleep(0.04)
    GPIO.output(DIREITA, GPIO.LOW)

def ler_tecla():  # leitura da interface de interação humana
    while True:
     tecla_comando = getch.getch()
     if tecla_comando == 'w':  # informações das teclas
        movefrente()
     elif tecla_comando == 's':
        movetras()
     elif tecla_comando == 'a':
        esquerda()
     elif tecla_comando == 'd':
        direita()


#motor_seteup()  # chamando as funções para execução
#ler_tecla()


