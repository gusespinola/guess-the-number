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

Mejoras: 
*Se puede jugar más de una vez si se desea.
*Al salir, se imprimen las estadśiticas del jugador.

Pendientes:
*Limitar la cantidad de intentos si el rango es demasiiado grande.
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

# Juego principal. Termina cuando se adivina el juego
def jugar():
    a, b = ingresar_rango() # Ingresar dos números a y b, donde a < b
    numero_aleatorio = randint(a, b)
    cant_de_intentos = 0 # cantidad de intentos en un solo juego 
    
    print("\n")
    fin_del_juego = False
    while fin_del_juego == False:
        eleccion = validar_entero(input("Ingresa un número: "))
        if eleccion == numero_aleatorio:
            cant_de_intentos += 1
            print("¡Felicidades! Lo has adivinado en", cant_de_intentos, "intentos.")
            fin_del_juego = True
        elif eleccion > numero_aleatorio:
            print("Sorry, tu número era muy alto.")
            cant_de_intentos += 1
        else:
            print("Sorry, tu número era muy bajo.")
            cant_de_intentos += 1

    return cant_de_intentos

# Script principal
print("ADIVINA EL NÚMERO")
print("Instrucciones:")
print("    Ingresá un rango de números enteros, luego adiviná el número que la computadora te genere a partir de ese rango.")
acum_de_intentos = 0 # acumulador de la cantidad de intentos de todos los juegos
cant_de_juegos = 0 # cantidad de juegos
tecla = "S" # Permite jugar al menos una vez
while tecla == "S" or tecla == "s":
    intentos = jugar()
    cant_de_juegos += 1
    acum_de_intentos += intentos
    print("===================================================================================================================")
    tecla = input("¿Querés seguir jugando? Presiona s para sí, otra tecla para salir: ") 

promedio_intentos = round(acum_de_intentos / cant_de_juegos, 2)
print("\n")
print("Tus estadísticas: Has ganado", cant_de_juegos, "juegos, usando", promedio_intentos, "intentos en promedio.")
print("Esperamos que te haya gustado el jueguito. ¡Volvé pronto!")