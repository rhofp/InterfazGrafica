from tkinter import*
from InterfazGrafica import *

class CasaInicio:

	def __init__(self,master):		
		contenedorBienvenida = Tk()
		contenedorBienvenida.title("Casa Inteligente")
		contenedorBienvenida.geometry("480x700")
		ventanaBienvenida = Frame()
		ventanaBienvenida.pack()
		ventanaBienvenida.config(width = 800, height=800)
		#ventanaBienvenida.config(bg="white")
		etiqueta1 = Label(ventanaBienvenida,text="Bienvenido",font =(20))
		etiqueta1.place(x=200,y=200)
		imagenLogin = PhotoImage(file="user.png")
		etiquetaImagen = Label(ventanaBienvenida, image=imagenLogin)
		etiquetaImagen.place (x=180 , y =50)

		usuario = Label(ventanaBienvenida, text="Usuario")
		usuario.place (x=150 , y =250)

		contrasenia = Label(ventanaBienvenida, text="Contraseña")
		contrasenia.place (x=150 , y =280)

		butonValidar = Button(ventanaBienvenida, text="Validar",command=self.validarDatos)
		butonValidar.place(x=200,y=330)

		contenedorBienvenida.mainloop()

	def validarDatos(self):
		InterfazGrafica()


def main():
	CasaInicio()

if __name__ == '__main__':
	main()