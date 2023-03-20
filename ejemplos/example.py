import os
import sys

from consolemenu import *
from consolemenu.items import *


def input_handler():
    pu = PromptUtils(Screen())
    # PromptUtils.input() returns an InputResult
    result = pu.input("Enter an input")
    pu.println("\nYou entered:", result.input_string, "\n")
    pu.enter_to_continue()

def input2_handler():
    pu = PromptUtils(Screen())
    # PromptUtils.input() returns an InputResult
    result = pu.input("Enter an input")
    pu.println("\nYou entered:", result.input_string, "\n")
    pu.enter_to_continue()

def crea_directorio():
    os.makedirs('dir1/dir2/dir3', exist_ok=True)
    
def main():

    # Crea el menú raíz

    menu = ConsoleMenu("Root Menu", "This is the Root Menu Subtitle")

    item1 = MenuItem("Item 1")

    # Crear un elemento de menú que llame a una función

    function_item = FunctionItem("Fun item", crea_directorio)
    function_item = FunctionItem("hola", input2_handler)



    # Cree un elemento de menú que llame a un comando del sistema, según el tipo de sistema operativo

    if sys.platform.startswith('win'):
        command_item = CommandItem("Command", 'cmd /c \"echo this is a shell. Press enter to continue." && set /p=\"')
    else:
        command_item = CommandItem("Command", 'sh -c \'echo "this is a shell. Press enter to continue."; read\'')



    # Cree un submenú usando un menú de selección, que toma una lista de cadenas para crear los elementos del menú.

    submenu = SelectionMenu(["item1", "item2", "item3"], title="Selection Menu",
                            subtitle="These menu items return to the previous menu")


    # Crear el elemento de menú que abre el submenú Selección
    submenu_item = SubmenuItem("Submenu item", submenu=submenu)
    submenu_item.set_menu(menu)


    # Cree un segundo submenú, pero esta vez use una instancia estándar de ConsoleMenu
    submenu_2 = ConsoleMenu("Another Submenu Title", "Submenu subtitle.")
    function_item_2 = FunctionItem("Fun item", Screen().input, ["Enter an input: "])
    item2 = MenuItem("Another Item")
    submenu_2.append_item(function_item_2)
    submenu_2.append_item(item2)
    submenu_item_2 = SubmenuItem("Another submenu", submenu=submenu_2)
    submenu_item_2.set_menu(menu)



    # Agregue todos los elementos al menú raíz
    menu.append_item(item1)
    menu.append_item(function_item)
    menu.append_item(command_item)
    menu.append_item(submenu_item)
    menu.append_item(submenu_item_2)


    # Mostrar el menú
    menu.start()
    menu.join()


if __name__ == "__main__":
    main()
