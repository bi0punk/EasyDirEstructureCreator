from art import text2art
import os
import datetime
from flask import Flask

Art = text2art("<FAST-FLASK>")
print(Art)

def mostrar_menu(opciones):
    print('Seleccione una opción / Select an option:\n')
    for clave, valor in opciones.items():
        print(f'{clave}) {valor[0]}')

def leer_opcion(opciones):
    while True:
        a = input('\nHa seleccionado: ')
        if a in opciones:
            return a
        print('ERROR.')

def accion1():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        fecha_genera = datetime.datetime.now()
        return f'<p>Hello World from FasT-FlasK!, Generated: {fecha_genera}</p>'

    app.run()

def accion2():
    print('Ejecutando acción 2')

def accion3():
    print('Ejecutando acción 3')

def salir():
    print('Saliendo...')
    exit()

def ayuda():
    print('Mostrando ayuda...')

def generar_menu(opciones, opcion_salida):
    while True:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        opciones[opcion][1]()
        print()
        if opcion == opcion_salida:
            break

def menu_principal():
    opciones = {
        '1': ('Simple Blank Flask App', accion1),
        '2': ('Flask App with example Template', accion2),
        '3': ('Flask Simple REST API', accion3),
        '4': ('Exit / Salir', salir),
        '5': ('Ayuda / Help', ayuda)
    }
    generar_menu(opciones, '5')

if __name__ == "__main__":
    menu_principal()
