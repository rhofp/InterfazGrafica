from tkinter import *
#import serial
#from componentes.Led import*
#from componentes.ControlMotores import*
#from componentes.Musica import *
#ser = serial.Serial('/dev/ttyACM0',9600)
#from componentes.Ventilador import*
from tkinter import messagebox

class CasaInicio:
	
	def __init__(self, master):
		self.master = master
		self.ventanaBienvenida = Frame(self.master)

		self.ventanaBienvenida.pack()
		self.ventanaBienvenida.config(width = 800, height=800)
		self.etiqueta1 = Label(self.ventanaBienvenida,text="Bienvenido",font =(20))
		self.etiqueta1.place(x=200,y=200)
		#-------------------------------
		self.imagenLogin = PhotoImage(file="fondo1.png")
		self.etiquetaImagen = Label(self.ventanaBienvenida, image=self.imagenLogin)
		self.etiquetaImagen.place (x=0 , y =0)
		#IMAGEN FONDO---------------------------------------------------
		self.imagenFondo = PhotoImage(file = "bienvenida.png")
		self.etiquetaFondo= Label(self.ventanaBienvenida, image = self.imagenFondo)
		self.etiquetaFondo.place(x=0,y=130)
		#IMAGEN LOGIN---------------------
		self.imagenLogoUNAM = PhotoImage(file = "unam2.png")
		self.etiquetaLogoUNAM= Label(self.ventanaBienvenida, image = self.imagenLogoUNAM)
		self.etiquetaLogoUNAM.place(x=0,y=4)
		#IMAGEN UNAM FI-----------------------------------------------
		self.imagenLogoUNAMfi = PhotoImage(file = "unamFi.png")
		self.etiquetaLogoUNAMfi= Label(self.ventanaBienvenida, image = self.imagenLogoUNAMfi)
		self.etiquetaLogoUNAMfi.place(x=370,y=4)

		#COMPONENTES USUARIO-----------------------------------------------------
		self.usuario = Label(self.ventanaBienvenida, text="Usuario")
		self.usuario.place (x=165 , y =250)

		self.cajaDeTextoUsuario = Entry(self.ventanaBienvenida)
		self.cajaDeTextoUsuario.place(x=222,y=250)

		#COMPONENTES CONTRASENIA
		self.contrasenia = Label(self.ventanaBienvenida, text="Contraseña")
		self.contrasenia.place (x=150 , y =280)

		self.cajaDeTextoContrasenia = Entry(self.ventanaBienvenida)
		self.cajaDeTextoContrasenia.config(show='*')
		self.cajaDeTextoContrasenia.place(x=220,y=280)

		self.butonValidar = Button(self.ventanaBienvenida, text="Validar",command=self.validarDatos)
		self.butonValidar.place(x=200,y=330)

	def validarDatos(self):

		if (self.cajaDeTextoUsuario.get()=='' and self.cajaDeTextoContrasenia.get()==''):
				messagebox.showwarning("Warning", "Introduzca todo los datos")
		elif(self.cajaDeTextoUsuario.get()=='mike' and self.cajaDeTextoContrasenia.get()== 'chingon' ):
			self.master.withdraw()
			self.newWindow = Toplevel(self.master)
			bb = InterfazGrafica(self.newWindow)	
		elif(self.cajaDeTextoUsuario.get()=='chrystian' and self.cajaDeTextoContrasenia.get()== 'loquesea'):
			self.master.withdraw()
			self.newWindow = Toplevel(self.master)
			bb = InterfazGrafica(self.newWindow)	

		elif(self.cajaDeTextoUsuario.get()== 'diego' and self.cajaDeTextoContrasenia.get()=='confirmo'):
			self.master.withdraw()
			self.newWindow = Toplevel(self.master)
			bb = InterfazGrafica(self.newWindow)
			
		else:
			messagebox.showwarning("Acceso Denagado", "Contraseña incorrecta!")


class InterfazGrafica():
	
	def __init__(self, master):
		self.master = master
		self.ventana = Frame(self.master)
		self.led = Led()
		self.motores = ControlMotores()
		self.ventilador = Ventilador()
		#self.musica = Musica()
		
		self.ventana.pack()
		self.ventana.config(width=480,height= 800)

		self.imagenPlano = PhotoImage(file="plano.png")
		self.etiquetaPlano = Label(self.ventana, image=self.imagenPlano)
		self.etiquetaPlano.image = self.imagenPlano
		self.etiquetaPlano.place(x=10,y=50)
		
		self.etiqueta = Label(self.ventana, text="Bienvenido a casa!",font=(18))
		self.etiqueta.place(x=185,y=20)
		

		#def crearBotones():
		#CUARTO 1---------------------------------------------------------------------
		self.botonPrenderCuarto1=Button(self.ventana, text="Prender", command=self.led.prenderLedCuarto1)
		self.botonPrenderCuarto1.place(x=50,y=90)

		self.botonApagarCuarto1=Button(self.ventana, text="apagar", command=self.led.apagarLedCuarto1)
		self.botonApagarCuarto1.place(x=53,y=140)

		self.botonAbrirPuerta1=Button(self.ventana, text="abrir", command=self.motores.abrirPuertaCuarto1)
		self.botonAbrirPuerta1.place(x=120,y=210)

		self.botonCerrarPuerta1=Button(self.ventana, text="cerrar", command=self.motores.cerrarPuertaCuarto1)
		self.botonCerrarPuerta1.place(x=10, y=210)
		#CUARTO 2------------------------------------------------------------------
		self.botonPrenderCuarto2=Button(self.ventana, text="Prender", command=self.led.prenderLedOrange)
		self.botonPrenderCuarto2.place(x=70,y=300)

		self.botonApagarCuarto2=Button(self.ventana, text="apagar", command=self.led.apagarLedOrange)
		self.botonApagarCuarto2.place(x=70,y=350)

		self.botonAbrirPuerta2=Button(self.ventana, text="abrir", command=self.motores.abrirPuerta2)
		self.botonAbrirPuerta2.place(x=160,y=500)

		self.botonCerrarPuerta2=Button(self.ventana, text="cerrar", command=self.motores.cerrarPuerta2)
		self.botonCerrarPuerta2.place(x=10,y=500)

		self.botonAbrirPuerta2Trasera=Button(self.ventana, text="abrir", command=self.motores.abrirPuerta2Trasera)
		self.botonAbrirPuerta2Trasera.place(x=160,y=250)

		self.botonCerrarPuerta2Trasera=Button(self.ventana, text="cerrar", command=self.motores.cerrarPuerta2Trasera)
		self.botonCerrarPuerta2Trasera.place(x=10,y=250)
		#BAÑO------------------------------------------------------------------------
		self.botonPrenderBanio=Button(self.ventana, text="prender", command=self.led.prenderBanio)
		self.botonPrenderBanio.place(x=220,y=90)

		self.botonApagarBanio=Button(self.ventana, text="apagar", command=self.led.apagarBanio)
		self.botonApagarBanio.place(x=220,y=140)
		#SALA LUCES ------------------------------------------------------------------------
		self.botonPrenderSala1=Button(self.ventana, text="prender", command=self.led.prenderSala1)
		self.botonPrenderSala1.place(x=350,y=100)

		self.botonApagarSala1=Button(self.ventana, text="apagar", command=self.led.apagarSala1)
		self.botonApagarSala1.place(x=350,y=150)

		self.botonPrenderSala2=Button(self.ventana, text="prender", command=self.led.prenderSala2)
		self.botonPrenderSala2.place(x=320,y=300)

		self.botonApagarSala2=Button(self.ventana, text="apagar", command=self.led.apagarSala2)
		self.botonApagarSala2.place(x=320,y=340)
		#SALA VENTANA-----------------------------------------------------------

		self.botonAbrirVentana=Button(self.ventana, text="ventana ON", command=self.motores.abrirVentana)
		self.botonAbrirVentana.place(x=220,y=440)

		self.botonCerrarVentana=Button(self.ventana, text="Ventana OFF", command=self.motores.cerrarVentana)
		self.botonCerrarVentana.place(x=360,y=440)




		#SALA COMPONENTE VENTILADOR----------------------------------------------------------------
		self.botonPrenderVentilador=Button(self.ventana, text="ventilador ON", command=self.ventilador.prenderVentilador)
		self.botonPrenderVentilador.place(x=220,y=400)

		self.botonApagarVentilador=Button(self.ventana, text="Ventilador OFF", command=self.ventilador.apagarVentilador)
		self.botonApagarVentilador.place(x=360,y=400)
		#SALA PUERTAS-----------------------------------------------------------------------
		self.botonAbrirPuertaSala=Button(self.ventana, text="abrir", command=self.motores.abrirPuertaSala)
		self.botonAbrirPuertaSala.place(x=220,y=470)

		self.botonCerrarPuertaSala=Button(self.ventana, text="cerrar", command=self.motores.cerrarPuertaSala)
		self.botonCerrarPuertaSala.place(x=400,y=470)
		#SALA MUSICA----------------------------------------------------------------------------------
		self.botonReproducirMusica=Button(self.ventana, text="Musica", command=self.ventanaMusicax)
		self.botonReproducirMusica.place(x=220,y=250)

		#GARAGE----------------------------------------------------------------------------
		self.botonPrenderGarage=Button(self.ventana, text="prender", command=self.led.prenderGarage)
		self.botonPrenderGarage.place(x=240,y=580)

		self.botonApagarGarage=Button(self.ventana, text="apagar", command=self.led.apagarGarage)
		self.botonApagarGarage.place(x=360,y=580)
		#CERRAR PUERTAS GARAGE----------------------------------------------------------------
		self.botonAbrirGarage=Button(self.ventana, text="abrir puerta", command=self.motores.abrirPuertaGarage)
		self.botonAbrirGarage.place(x=20,y=630)

		self.botonCerrarPuertaGarage=Button(self.ventana, text="cerrar puerta", command=self.motores.cerrarPuertaGarage)
		self.botonCerrarPuertaGarage.place(x=200,y=630)

		#DETENER PROCESO ------------------------------------------------------------
		self.botonParar=Button(self.ventana, text="detener proceso", command=self.motores.detenerProceso, bg="red")
		self.botonParar.place(x=350,y=20)
	def ventanaMusicax(self):
		self.master.withdraw()
		self.nuevaVentanaMusica=Toplevel(self.master)
		ss= Musica(self.nuevaVentanaMusica)


class Musica:

	def __init__(self,master):
		self.master=master
		self.ventanaMusica= Frame(self.master)
		self.ventanaMusica.pack()
		self.ventanaMusica.config(width=480,height= 800)

		self.imagenMusica2 = PhotoImage(file="musicaa.png")
		self.etiquetaMusica2 = Label(self.ventanaMusica, image=self.imagenMusica2)
		self.etiquetaMusica2.image = self.imagenMusica2
		self.etiquetaMusica2.place(x=0,y=0)


		self.imagenMusica = PhotoImage(file="musica.png")
		self.etiquetaMusica = Label(self.ventanaMusica, image=self.imagenMusica)
		self.etiquetaMusica.image = self.imagenMusica
		self.etiquetaMusica.place(x=0,y=150)

		self.etiquetaMusica = Label(self.ventanaMusica, text= "Reproductor de musica")
		self.etiquetaMusica.place(x=185, y =160)

			
	
if __name__ == '__main__':
	root = Tk()
	root.title('Casa Inteligente')
	root.geometry("480x700")
	b = CasaInicio(root)
	
	root.mainloop()