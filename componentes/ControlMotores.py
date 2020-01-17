import serial
from tkinter import*
import time

ser = serial.Serial('/dev/ttyACM0',9600)

class ControlMotores:

	def abrirPuertaCuarto1(self):
			#ser = serial.Serial('/dev/ttyACM0',9600)
		valor = 'c'
		ser.write(valor.encode())
		valor='e'
		ser.write(valor.encode())

	def cerrarPuertaCuarto1(self):
			#ser = serial.Serial('/dev/ttyACM0',9600)
			valor = 'd'
			ser.write(valor.encode())
			valor='e'
			ser.write(valor.encode())

	def abrirPuerta2(self):
			#ser = serial.Serial('/dev/ttyACM0',9600)
			valor = 'g'
			ser.write(valor.encode())	

	def cerrarPuerta2(self):
			#ser = serial.Serial('/dev/ttyACM0',9600)
			valor = 'f'
			ser.write(valor.encode())
			

	def abrirPuerta2Trasera(self):
			#ser = serial.Serial('/dev/ttyACM0',9600)
			valor = 'o'
			ser.write(valor.encode())	

	def cerrarPuerta2Trasera(self):
			#ser = serial.Serial('/dev/ttyACM0',9600)
			valor = 'p'
			ser.write(valor.encode())

	def detenerProceso(self):
			#ser = serial.Serial('/dev/ttyACM0',9600)
			valor = 'e'
			ser.write(valor.encode())
			

	def abrirPuertaSala(self):
		valor = 'b'
		ser.write(valor.encode())
		print("Se abrio la puerta Sala")
		valor='e'
		ser.write(valor.encode())

	def cerrarPuertaSala(self):
		print("Se cerro la puerta prro")
		valor = 'a'
		ser.write(valor.encode())
		valor='e'
		ser.write(valor.encode())

	def abrirPuertaGarage(self):
		print("Se abrieron las puertas del garage")
		valor = 'i'
		ser.write(valor.encode())
	def cerrarPuertaGarage(self):
		print("Se cerraron las puertas del garage")
		valor = 'h'
		ser.write(valor.encode())

	def abrirVentana(self):
		print("Se abrieron las ventanas")
		valor = 'z'
		ser.write(valor.encode())

	def cerrarVentana(self):
		print("Se cerraron las ventanas")
		valor = 'y'
		ser.write(valor.encode())

