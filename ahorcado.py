import random as rd
import os

#Eligue aleatoriamente una palabra
from random import choice
palabras=(choice(["hola","disco","teclado","corazon","amor","pizza","espejo","libreta","usb","memoria","avion","cristina","gato","perro","pollo","dani","oso","programacion","atun","gustavo","guitara","libro","fisica","matematicas","cesar","kilos","chamfles","tequila","vino","vodka","cerveza","chocomil","calculadora","celular","bateria","piano","computadora","cama","abuela","palo"]))
letra1=palabras
#El Desmadre que seleciona la palabra
indice=rd.randint(0,len(letra1)-1)
letra=letra1[indice]
PrimeraLetra=len(letra1[:indice])
Ultima=len(letra1[indice+1:])
#Estructuro una pista para adivinar la palabra
pista=(PrimeraLetra*" _ ") + letra + (Ultima*" _ ")

print(palabras) ##Solo es como prueba

#Pantalla de inicio
os.system ("clear")
print('''
      +---+
      |   |
          |
          |
          |
          |
    =========''')
print("\n===========¡Vamos a jugar!============ \n")

print(pista,"\n")

intentos = 0

res = input("Introduzca la palabra: ")

while intentos < 20:
    os.system ("clear")#Limpia la pantalla por cada intento
    #Dubuja al ahorcado dependiendo del numero de intentos
    if intentos <= 4:
        print('''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''')
    elif intentos <= 8:
        print('''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''')
    elif intentos <= 12:
        print('''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''')
    elif intentos <= 16:
        print('''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''')
    elif intentos <= 20:
        print('''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''')

    print("\n",pista,"\n")
    res = input("Intentalo de nuevo!: ")
    #Se va sumando el numero de intentos
    intentos = intentos + 1 
    #Si la palabra es correcta te saca del bucle
    if res == palabras:
        break
#Te dice si ganaste o perdiste    
if res == palabras:
    
    print("\n¡Ganaste!\n")

if res != palabras or intentos == 20:
    #Cuando pierdes te sale el ¡¡Ahorcado!!
    os.system("clear")
    print("\n¡Ahorcado!\n")
    print('''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''')
