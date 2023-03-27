from art import *
import os
from datetime import datetime
#CREAMOS NOMBRE DE APP MEDIANTE CODIGO ASC¢→
Art=text2art("<FAST-FLASK>")
print(Art)


# Create the menu
def mostrar_menu(opciones):
    print(' Seleccione una opción / Select an option: \n')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input(' \nA seleccionado : ')) not in opciones:
        print('ERROR.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()
    


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Simple Blank Flask App', accion1),
        '2': ('Flask App with example Template', accion2),
        '3': ('Flask Simple REST API', accion3),
        '4': ('Exit / Salir', salir),
        '5': ('Ayuda / Help', ayuda)
    }

    generar_menu(opciones, '5')

#Accciones del menu

def accion1():
    print('Has elegido la opción 1')
    print("Ingrese nombre de proyecto")
    nombre_proyecto = input()
    crea_directorio(nombre_proyecto)
    

def accion2():
    print('Has elegido la opción 2')


def accion3():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')


def ayuda():
    print("Ayuda")

#Funciones propias del script


#Crea una carpeta con el nombre del proyecto
def crea_directorio(nombre):
    ruta = f'{nombre}/templates/'
    os.makedirs(f'{nombre}/templates/', exist_ok=True)
    fecha_genera = datetime.now()
    """ f = open (f'{ruta}app.py','w') """
    f = open (f'{nombre}/app.py','w')
    f.write("from flask import Flask\n")
    f.write('\n')
    f.write('\n')
    f.write("app = Flask(__name__)\n")
    f.write('\n')
    f.write('\n')
    f.write('@app.route("/")\n')
    f.write("def hello_world():\n")
    f.write(f'   return "<p>Hello World from FasT-FlasK!, generated {fecha_genera}</p>"')
    f.close()
        







if __name__ == '__main__':
    menu_principal()