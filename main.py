
import tkinter

from tkinter import messagebox
from tkinter import *

from tkinter import ttk








class FrmLogin(tkinter.Frame):#CLASE FORMULARIO PRINCIPAL

    def __init__(self):
        global obj_ventana#OBJETO GLOBAL VENTA
        obj_ventana = tkinter.Tk()#OBJETO DE LA VENTANA
        super().__init__(obj_ventana)
        obj_ventana.title("REGISTRO DE ESTUDIANTES: !!!!")#TITULO DEL PRIMER VENTANA
        obj_ventana.geometry("500x300")#DIMENCION
        obj_ventana.configure(background="blue")#COLOR VENTANA
        self.iniciarComponentes()#INICIALIZA COMPONENTES

    def iniciarComponentes(self):#INICIALIZA LOS BOTONES DE LA PRIMER VENTANA
        btnregistrar =tkinter.Button(obj_ventana ,text="REGISTRO" ,command=self.registrar)#REGISTRA LOS ESTUDIANTE
        btnregistrar.place(x=100, y=100)#COORDENADA DEL BOTOS
        btnsalir = tkinter.Button(obj_ventana, text="SALIR", command=self.destroy)#SALE DE LA VENTANA
        btnsalir.place(x=100, y=200)

    def registrar(self):

        nuevaventana = FrmRegistrar()
        nuevaventana = mainloop()





#SEGUNDA VENTANA REGISTRO ESTUDIANTES
class FrmRegistrar(tkinter.Frame):#SEGUNDA VENTANA FORMULARIO CON DATOS DEL ESTUDIANTE

    def __init__(self):
        global nombre1#VARIABLES GLOBALES
        global apellido1
        global grado
        global materia
        global obj_ventana
        obj_ventana = tkinter.Tk()#OBJETO DE LA VENTANA
        super().__init__(obj_ventana)
        obj_ventana.title("REGISTRAR !!!!")#TITULO DE LA VENTANA
        obj_ventana.geometry("500x300")#DIMENCION
        obj_ventana.configure(background="pink")#COLOR
        lblnombre = tkinter.Label(obj_ventana, text="NOMBRE:")#IMPRIME NONBRE EN LA INTERFAZ
        lblnombre.place(x=90, y=50)
        lblapellido = tkinter.Label(obj_ventana, text="APELLIDO:")#IMPRIME APELLIDO
        lblapellido.place(x=90, y=100)
        lblgrado = tkinter.Label(obj_ventana, text="GRADO:")#IMPRIME GRADO
        lblgrado.place(x=90, y=150)
        lblmateria= tkinter.Label(obj_ventana, text="MATERIA:")#IMPROME MATERIA
        lblmateria.place(x=90, y=200)#CORDENADAS DEKL TEXTO
        self.nombre1 = tkinter.Entry(obj_ventana, width=40)
        self.nombre1.place(x=200, y=50)
        self.apellido1 = tkinter.Entry(obj_ventana, width=40)
        self.apellido1.place(x=200, y=100)
        self.grado = tkinter.Entry(obj_ventana, width=40)
        self.grado.place(x=200, y=150)
        self.materia = tkinter.Entry(obj_ventana, width=40)
        self.materia.place(x=200, y=200)
        btnregresar = tkinter.Button(obj_ventana, text="REGRESAR ", command=self.regresar)
        btnregresar.place(x=120, y=270)
        btngrabar = tkinter.Button(obj_ventana, text="Guardar ", command=self.regresar)
        btngrabar.place(x=250, y=270)
        texto =tkinter.Button(obj_ventana, text="BIENVENIDO SISTEMA CALIFICACIONES 2023")
        texto.place(x=200, y=10)







    def regresar(self):#funcion para regresar a la primer pantalla


        nuevaventana = FrmLogin()
        nuevaventana = mainloop()



MATERIAS = 1












objeto = FrmLogin()
objeto.mainloop()
MATERIAS = 1



print("BIENVENIDO AL SISTEMA DE CALIFICACIONES 2023")
# Hacer un ciclo, pedir datos y sumar la calificación
contador = 1
sumatoria = 0
while contador <= MATERIAS:
    materia = input("Nombre de la materia {}: ".format(contador))
    calificacion = float(input("Calificación en {}: ".format(materia)))
    # Sumar la calificación a la sumatoria
    sumatoria = sumatoria + calificacion
    # Aumentar el contador para no hacer un ciclo infinito
    contador = contador + 1

# Hacer cálculos e imprimir resultados
promedio = sumatoria / MATERIAS

print("""***** Resultados *****
    SISTEMA DE CALIFICACIONES 2023
    Estudiante: {} | {} {}
    *******************************
    * Promedio: {}
    *******************************
    """.format(nombre1,apellido1, grado, promedio))


