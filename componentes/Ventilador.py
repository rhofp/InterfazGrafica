import serial
from tkinter import*
#from componentes.controlMotores import*
ser = serial.Serial('/dev/ttyACM0',9600)

class Ventilador:

	def prenderVentilador(self):
		print("Ventilador prendido")
		valor = 'q'
		ser.write(valor.encode())

	def apagarVentilador(self):
		print("Ventilador apagado")
		valor = 'r'
		ser.write(valor.encode())

	

