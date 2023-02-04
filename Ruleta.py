
# lo ocupe para limpiar la terminal cada que se ejecuta os.system('cls')
import os
import random

from colorama import Fore as color, init, Back as fondo
init()

numeros = ["00", "0", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
numero = 10

# aqui lleno la lista numeros
while numero <= 36:
    numeros.append(str(numero))
    numero = numero+1
del numero

rojos = ["1", "3", "5", "7", "9", "12", "14", "16", "18",
         "19", "21", "23", "25", "27", "30", "32", "34", "36"]
negros = ["2", "4", "6", "8", "10", "11", "13", "15", "17",
          "20", "22", "24", "26", "28", "29", "31", "33", "35"]
ceros = ["0", "00"]


def mostrar():

    print("+--+--+--+--+--+--+--+--+--+--+--+--+--+")
    print("|:)|"+color.RED+numeros[4]+color.RESET+"|"+numeros[7]+"|"+color.RED+numeros[10]+color.RESET+"|"+color.RED+numeros[13]+color.RESET+"|"+numeros[16]+"|"+color.RED+numeros[19] + color.RESET +
          "|"+color.RED+numeros[22]+color.RESET+"|"+numeros[25]+"|"+color.RED+numeros[28]+color.RESET+"|"+color.RED+numeros[31]+color.RESET+"|"+numeros[34]+"|"+color.RED+numeros[37]+color.RESET+"|")
    print("+--+--+--+--+--+--+--+--+--+--+--+--+--+")
    print("|"+color.GREEN+numeros[0]+color.RESET+"|"+numeros[3]+"|"+color.RED+""+numeros[6]+color.RESET+"|"+numeros[9]+"|"+numeros[12]+"|"+color.RED+numeros[15]+color.RESET+"|" +
          numeros[18]+"|"+numeros[21]+"|"+color.RED+numeros[24]+color.RESET+"|"+numeros[27]+"|"+numeros[30]+"|"+color.RED+numeros[33]+color.RESET+"|"+numeros[36]+"|")
    print("+--+--+--+--+--+--+--+--+--+--+--+--+--+")
    print("| "+color.GREEN+numeros[1]+color.RESET+"|"+color.RED+numeros[2]+color.RESET+"|"+numeros[5]+"|"+color.RED+numeros[8]+color.RESET+"|"+numeros[11]+"|"+numeros[14]+"|" + color.RED +
          numeros[17]+color.RESET+"|"+color.RED+numeros[20]+color.RESET+"|"+numeros[23]+"|"+color.RED+numeros[26]+color.RESET+"|"+numeros[29]+"|"+numeros[32]+"|"+color.RED+numeros[35]+color.RESET+"|")
    print("+--+--+--+--+--+--+--+--+--+--+--+--+--+\n")


def lanzar():
    aleatorio = random.choice(numeros)
    return aleatorio


def resultado(ganador):

    lugar = numeros.index(ganador)
    chekpoint = numeros[lugar]

    numeros[lugar] = color.BLUE+"##"+color.RESET

    mostrar()

    numeros[lugar] = chekpoint
