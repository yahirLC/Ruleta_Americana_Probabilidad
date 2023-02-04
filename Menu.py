import os
import Ruleta
from Ruleta import rojos, negros, ceros
from colorama import Fore, init

init()  # inicio el colorama


def mostrar():
    os.system('cls')
    print(Fore.RED+"MENU:")
    print(Fore.YELLOW+"  1.-Jugar")
    print("  0.-Salir"+Fore.RESET)


def seleccion(opcion: int):
    if opcion == 1:
        jugar()
    elif opcion == 0:
        return False


def jugar():
    os.system('cls')

    print(Fore.YELLOW+"Bienvenido vamos a comenzar\n"+Fore.RESET)
    Ruleta.mostrar()

    # de aqui tome para tomar de una lista un valor aleatorio https://parzibyte.me/blog/2019/03/19/python-seleccionar-elemento-aleatorio-arreglo-lista/
    input(Fore.CYAN+"Precione una tecla para lanzar la rueda..."+Fore.RESET)

    os.system('cls')
    numero = Ruleta.lanzar()
    Ruleta.resultado(numero)

    def resultado():
        color = ""

        try:
            ceros.index(numero)
        except:
            try:
                rojos.index(numero)
            except:
                color = "n"
            else:
                color = "r"
        else:
            color = "v"

        if color == "v":
            print(Fore.YELLOW+"[["+Fore.GREEN+numero +
                  " Cero" + Fore.YELLOW+"]]\n"+Fore.RESET)
        elif color == "r":
            print(Fore.YELLOW+"[["+Fore.RED+numero +
                  " Rojo"+Fore.YELLOW+"]]\n"+Fore.RESET)
        else:
            print(Fore.YELLOW +
                  "[["+Fore.RESET+numero+" Negro"+Fore.YELLOW+"]]\n")

    resultado()

    print(Fore.YELLOW+"1.Realizar otro tiro")
    print("0.Salir\n"+Fore.RESET)

    #############

    opcion = ""

    while opcion == "":

        opcion = input(Fore.CYAN+"Su opcion: "+Fore.RESET)

        if opcion == "1" or opcion == "0":
            if opcion == "1":
                jugar()
            elif opcion == "0" or 0:
                print("")
        else:
            os.system('cls')
            Ruleta.resultado(numero)
            resultado()

            print(Fore.YELLOW+"1.Realizar otro tiro")
            print("0.Salir\n"+Fore.RESET)

            opcion = ""
