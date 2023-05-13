from art import text2art
import os
import datetime

Art = text2art("<FAST-FLASK>")
print(Art)

def mostrar_menu(opciones):
    print('Seleccione una opción / Select an option:\n')
    for clave in sorted(opciones):
        print(f'{clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while True:
        a = input('\nHa seleccionado: ')
        if a in opciones:
            return a
        print('ERROR.')

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    while True:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
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

class Flask_main:
    def __init__(self, filename, ruta, contenido):
        self.filenama = filename
        self.ruta = ruta
        contenido = contenido
        mainpy = Flask_main(filename='app.py', ruta=None, contenido='')

def crear_archivo(nombre, contenido):
    ruta = f'{nombre}/templates/'
    os.makedirs(ruta, exist_ok=True)
    fecha_genera = datetime.datetime.now()

    with open(f'{nombre}/app.py', 'w') as f:
        f.write("from flask import Flask\n\n")
        f.write("app = Flask(__name__)\n\n")
        f.write("@app.route('/')\n")
        f.write("def hello_world():\n")
        f.write(f"    return '<p>Hello World from FasT-FlasK!, Generated: {fecha_genera} </p>'\n")

    with open(f'{ruta}index.html', 'w') as f:
        f.write("<!DOCTYPE html>\n")
        f.write('<html lang="en">\n')
        f.write("<head>\n")
        f.write("<meta charset='UTF-
