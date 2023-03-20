# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from art import *
import os
a = tprint("flAKS")
print(a)
print("hola mundo")

Art=text2art("<Fast-Flask>")
print(Art)
# Create the menu




def crea_directorio():
    os.makedirs('dir1/dir2/dir3', exist_ok=True)

menu = ConsoleMenu("Project Structure Generator", ""+str(Art))

# Create some items

# MenuItem is the base class for all items, it doesn't do anything when selected


# Crear algunos elementos

# MenuItem es la clase base para todos los elementos, no hace nada cuando se selecciona
""" menu_item = MenuItem("Menu Item") """

# A FunctionItem runs a Python function when selected
# Un elemento de función ejecuta una función de Python cuando se selecciona
function_item = FunctionItem("Flask Blank Project", input, ["Enter an input "])



# Un CommandItem ejecuta un comando de consola
# A CommandItem runs a console command
command_item = CommandItem("Run a console command",  "ls > data.txt")


# A SelectionMenu constructs a menu from a list of strings
# Un SelectionMenu construye un menú a partir de una lista de cadenas
selection_menu = SelectionMenu(["item1", "item2", "item3"])



# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu

# Un SubmenuItem le permite agregar un menú (el menú de selección anterior, por ejemplo)
# como submenú de otro menú

submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
# Una vez que hayamos terminado de crearlos, solo agregamos los elementos al menú
""" menu.append_item(menu_item) """
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)


# Finally, we call show to show the menu and allow the user to interact
# Finalmente, llamamos show para mostrar el menú y permitir que el usuario interactúe
menu.show()