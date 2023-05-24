# -----------------------------------------------------------------------
#          Proyecto Semestral - Análisis y Diseño de Algoritmos
#       Raj Ahir (20-39-6034) - Adriana González (8-997-2009) 1SF121
# -----------------------------------------------------------------------

# Programa que permite al usuario jugar

import random

class Hangman:

    def __init__(propio, categorias): # Método constructor para las categorías

        propio.letrausadas = []
        propio.categorias = categorias
        propio.intentos = 0
        propio.palabra = ''
        propio.actualPalabra = ''

    def randomPalabra(propio): # Método para determinar una palabra aleatoria de las categorías
        return propio.categorias[random.randrange(len(propio.categorias))]

    def resetGame(propio): # Método para determinar el reinicio de la partida dentro de la categoría
        propio.letrausadas = []
        propio.intentos = 0
        propio.palabra = propio.randomPalabra()
        propio.actualPalabra = ''
        for i in range(len(propio.palabra)):
            if propio.palabra[i:i+1] == " ":
                propio.actualPalabra += " "
            else:
                propio.actualPalabra += '_'

    def adivinarLetra(propio, userInput): # Método para adivinar la letra de la palabra a jugar
        userInput = userInput.casefold()
        if propio.intentos == 6:
            propio.actualPalabra = propio.getPalabra() # Se obtiene la derrota después de seis intentos
            return "Ya has perdido!"
        elif propio.actualPalabra == propio.getPalabra(): # Se obtiene la victoria después de haber acertado la palabra
            return "Ya has ganado!"
        elif len(userInput) == 1:
            for x in propio.letrausadas:
                if x == userInput: # Si el ingreso de la letra se repite, se muestra la letra repetida
                    return "Letra Repetida" 
            count = 0
            for i in range(len(propio.palabra)): # Comparación de las letras ingresadas con la palabra a adivinar
                if userInput == propio.palabra[i: i + 1].casefold():
                    propio.actualPalabra = propio.actualPalabra[:i] + propio.getPalabra()[i:i+1] + propio.actualPalabra[i+1:]
                    count += 1
            if propio.palabra == propio.actualPalabra: # Si la palabra es acertada gana
                        return "Ganaste!"
            if count == 0:
                propio.intentos += 1
            elif count > 0:
                propio.letrausadas.append(userInput) # Comparación acertada de la letra con respecto a la palabra
                return "Correcto"
            if propio.intentos == 6:
                propio.letrausadas.append(userInput)
                propio.actualPalabra = propio.getPalabra() # Si la palabra es incorrecta pierde
                return "Perdiste!"
            propio.letrausadas.append(userInput) # Comparación incorrecta de la letra con respecto a la palabra
            return "Incorrecto"
        elif len(userInput) > 1:
            if userInput == propio.palabra.casefold():
                propio.actualPalabra = propio.palabra # Si la palabra es acertada gana
                return "Ganaste!"
            else:
                propio.intentos += 1
                if propio.intentos == 6:
                    propio.actualPalabra = propio.getPalabra() # Comparación incorrecta por los fallos consecutivos de intentos
                    return "Perdiste!"
                return "Incorrecto"

    def getLetrasUsadas(propio): # Método para obtener las letras usadas
        return propio.letrausadas

    def getIntentos(propio): # Método para obtener las intentos a fin de mostrar el monigote
        return propio.intentos

    def getPalabra(propio): # Método para obtener las palabras a jugar
        return propio.palabra

    def getActualPalabra(propio): # Método para obtener la palabra actual a adivinar
        formattedActualPalabra = ''
        for i in range (len(propio.actualPalabra)):
            formattedActualPalabra += propio.actualPalabra[i:i+1] + ' '
        return formattedActualPalabra

    def getCategorias(propio): # Método para obtener las categorías a jugar
        return propio.categorias
