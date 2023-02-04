
import Menu
from colorama import Fore, init
init()

salir = False

while salir == False:
    Menu.mostrar()

    try:
        opcion = int(input(Fore.CYAN+"\nIngrese su opcion: "+Fore.RESET))
    except:
        print("")
    else:

        if opcion == 0:
            salir = True
        else:
            Menu.seleccion(opcion)

print(Fore.YELLOW+"\nGracias por volver\n")
