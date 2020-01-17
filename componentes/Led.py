import serial
from tkinter import*
#from componentes.ControlMotores import*
ser = serial.Serial('/dev/ttyACM0',9600)

class Led:

	def prenderLedCuarto1(self):
			#ser = serial.Serial('/dev/ttyACM0',9600)
			valor = '0'
			ser.write(valor.encode())	

	def apagarLedCuarto1(self):
			#ser = serial.Serial('/dev/ttyACM0',9600)
			valor = '1'
			ser.write(valor.encode())

	def prenderLedOrange(self):
			#ser = serial.Serial('/dev/ttyACM0',9600)
			valor = '2'
			ser.write(valor.encode())	

	def apagarLedOrange(self):
			#ser = serial.Serial('/dev/ttyACM0',9600)
			valor = '3'
			ser.write(valor.encode())

	def prenderBanio(self):
		valor = '8'
		ser.write(valor.encode())
		print("Se prendieron luces del banio")

	def apagarBanio(self):
		print("Se apagaron luces del banio")
		valor = '9'
		ser.write(valor.encode())
	def prenderSala1(self):
		print("Luz prendida")
		valor = '4'
		ser.write(valor.encode())

	def apagarSala1(self):
		print("Luz Apagada")
		valor = '5'
		ser.write(valor.encode())

	def prenderSala2(self):
		print("Luz prendida 2")
		valor = '6'
		ser.write(valor.encode())

	def apagarSala2(self):
		print("Luz apagada 2")
		valor = '7'
		ser.write(valor.encode())

	def prenderGarage(self):
		print("se prendiero luces del garage")
		valor = 'x'
		ser.write(valor.encode())


	def apagarGarage(self):
		print("Se apagaron luces del garage")
		valor = 'w'
		ser.write(valor.encode())



