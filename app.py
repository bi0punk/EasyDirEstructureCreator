from art import *
import os


Art=text2art("<FAST-FLASK>")
print(Art)
# Create the menu




def crea_directorio(nombre):
    """ print(nombre) """
    os.makedirs('hola/dir2/dir3', exist_ok=True)


def mostrar_menu(opciones):
    print('OPTIONS:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('SELECT : ')) not in opciones:
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
        '1': ('Simple blank flask app', accion1),
        '2': ('Flask app with example template', accion2),
        '3': ('Flask REST simple api', accion3),
        '4': ('Exit', salir),
        '5': ('Ayuda', ayuda)
    }

    generar_menu(opciones, '5')


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

if __name__ == '__main__':
    menu_principal()