"""
Desafío:
Crear un juego en el que la computadora elija un entero aleatorio X de 1 a 100 y se le pide al usuario que lo adivine.
En cada ronda, se le solicita al usuario un número de entrada.
Si el número ingresado es menor a X:
El juego muestra "Lo siento, "¡inténtalo de nuevo! Muy bajo."
Si el número ingresado es mayor a X:
El juego muestra Lo siento, "¡inténtalo de nuevo! Muy alto."
Si el número está correcto:
El juego finaliza y muestra "¡Felicidades! Lo has adivinado"

MejorasÑ
"""
from random import randint

# Se ejecuta hasta que el usuario introduzca un número entero
def validar_entero(a):
    try:
        a = int(a)
    except ValueError:
        print("Dato inválido. Debes ingresar un número entero")
        a = validar_entero(input("Cantidad inicial: "))        
    return a

# Se ejecuta hasta que el usuario introduzca dos números enteros a y b, donde a < b
def ingresar_rango():
    print("===================================================================================================================")
    a = validar_entero(input("Cantidad inicial: "))    
    b = validar_entero(input("Cantidad final: "))    
    while b <= a:
        print("La cantidad final debe ser mayor que la cantidad inicial.")
        b = validar_entero(input("Cantidad final: "))        
    return a, b

# Juego principal. Lo traté de hacer recursivo para "volver a jugar dentro del juego"
def jugar():
    a, b = ingresar_rango() # a es menor que b
    numero_aleatorio = randint(a, b)
    cant_de_intentos = 4 # Pendiente: investiguar cuál es la cantidad "justa" (fair) de intentos
    print("\n")
    while cant_de_intentos > 0:
        eleccion = validar_entero(input("Ingresa un número: "))
        if eleccion == numero_aleatorio:
            print("¡Felicidades! Lo has adivinado")
            cant_de_intentos = 0
        elif eleccion > numero_aleatorio:
            print("Sorry, tu número era muy alto.")
            cant_de_intentos -= 1
            print("Te quedan", cant_de_intentos, "intentos")
        else:
            print("Sorry, tu número era muy bajo.")
            cant_de_intentos -= 1
            print("Te quedan", cant_de_intentos, "intentos")
        
    
    if cant_de_intentos == 0 and eleccion != numero_aleatorio:
        print("Bajón, perdiste. F for you.")
        

    print("===================================================================================================================")
    tecla = input("¿Querés seguir jugando? Presiona s para sí, otra tecla para salir: ") 

    if tecla == "S" or tecla == "s":
        jugar()
    else:
        print("Esperamos que te haya gustado el jueguito. ¡Volvé pronto!")

# Script principal
print("ADIVINA EL NÚMERO")
print("Instrucciones")
print("    Ingresa un rango de números enteros, luego adivina el número que la computadora te genere a partir de ese rango")
jugar()