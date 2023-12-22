from art import text2art
import datetime
from flask import Flask

ERROR_MESSAGE = 'ERROR. Seleccione una opción válida.'
EXIT_MESSAGE = 'Saliendo...'
HELP_MESSAGE = 'Mostrando ayuda...'

def print_title():
    title = text2art("<FAST-FLASK>")
    print(title)

def print_menu(options):
    print('Seleccione una opción / Select an option:\n')
    for key, value in options.items():
        print(f'{key}) {value[0]}')

def get_user_choice(options):
    while True:
        user_input = input('\nHa seleccionado: ')
        if user_input in options:
            return user_input
        print(ERROR_MESSAGE)

def run_flask_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        now = datetime.datetime.now()
        return f'<p>Hello World from FasT-FlasK!, Generated: {now}</p>'
    app.run()

def action2():
    print('Ejecutando acción 2')

def action3():
    print('Ejecutando acción 3')

def exit_program():
    print(EXIT_MESSAGE)
    exit()

def show_help():
    print(HELP_MESSAGE)

def generate_menu(options, exit_option):
    while True:
        print_menu(options)
        user_choice = get_user_choice(options)
        options[user_choice][1]()
        print()
        if user_choice == exit_option:
            break

def main():
    menu_options = {
        '1': ('Simple Blank Flask App', run_flask_app),
        '2': ('Flask App with example Template', action2),
        '3': ('Flask Simple REST API', action3),
        '4': ('Exit / Salir', exit_program),
        '5': ('Ayuda / Help', show_help)
    }
    generate_menu(menu_options, '4')

if __name__ == "__main__":
    print_title()
    main()

