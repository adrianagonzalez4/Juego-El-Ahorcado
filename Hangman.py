# -----------------------------------------------------------------------
#          Proyecto Semestral - Análisis y Diseño de Algoritmos
#       Raj Ahir (20-39-6034) - Adriana González (8-997-2009) 1SF121
# -----------------------------------------------------------------------

# Archivo: Hangman.py
# En el juego de El Ahorcado, el jugador elije una categoría y piensa una palabra de ella donde, 
# esa palabra a buscar se representa con líneas (una por cada letra de la palabra que le 
# correspondió). Cuando el participante esté jugando, la letra que está en la palabra se sustituye
# en la línea por la letra. De lo contrario, si no lo está, se agrega una componente al monigote o 
# figura de palo que será ahorcado si pierde. El juego finaliza cuando se adivina la palabra o se 
# completó el monigote ahorcado.

import pygame, sys, os
import HangmanClase
pygame.init()
pygame.mixer.pre_init(44100, 16, 2)

# Carga los archivos de recursos PNG y WAV para la interfaz
def recursos(nomArchivo):
    if getattr(sys, 'frozen', False):
        datadir = os.path.dirname(sys.executable)
    else:
        datadir = os.path.dirname(__file__)
    return os.path.join(datadir, nomArchivo)


# Categoria definida con algunos animales
animalesCate = ['Llama', 'Jirafa', 'Panda', 'Pinguino', 'Tiburon', 'Serpiente', 'Tigre',
               'Oveja', 'Pajaro', 'Elefante', 'Conejo', 'Flamingo', 'Gato', 'Cocodrilo', 'Perro', 
               'Leon', 'Oso', 'Koala', 'Aguila', 'Loro', 'Ciervo', 'Cebra', 'Foca', 'Mapache']

# Categoria definida con las distintas provincias del país de Panamá
provinciasCate = ['Bocas del Toro', 'Chiriqui', 'Colon', 'Cocle', 'Los Santos', 'Veraguas',
               'Darien', 'Panama', 'Panama Oeste', 'Herrera']

# Categoria definida con distintas frutas
frutaCate = ['Manzana', 'Uva', 'Naranja', 'Mango', 'Coco', 'Maracuya', 'Kiwi', 'Pera',
             'Guanabana', 'Limon', 'Mamey', 'Papaya', 'Sandia', 'Melocoton', 'Ciruela', 'Marañon', 'Pitaya', 
             'Aguacate', 'Nectarina', 'Toronja', 'Arandano', 'Albaricoque', 'Cereza', 'Nance', 'Mamon Chino']

# Categoria definida con algunos países del mundo
paisesCate= ['Colombia', 'Panama', 'Australia', 'Alemania', 'Italia', 'Brasil', 'Argentina', 'Japon', 'Corea',
             'Portugal', 'Rusia', 'Sudafrica', 'Madagascar', 'Canada', 'India', 'Mexico', 'Inglaterra', 'China',
             'España', 'Francia', 'Peru', 'Uruguay', 'Paraguay', 'Chile', 'Costa Rica', 'Belice', 'Jamaica', 
             'Estados Unidos']

# Categoria definida con los distintos nombres de los compañeros de clase
est121List = ["Adriana", "Agustin", "Alejandro", "Alexander", "Alfonso", "Christopher", "Cristofer", "Diego",
              "Ever", "Hector", "Isaac", "Jairo", "Javier", "Jonathan",
              "Johnny", "Jordy", "Jose", "Kameron", "Lourdes", "Luis", "Mariel", "Marjorie", "Martin",
              "Maybeth", "Nicole", "Oscar", "Paola", "Raj", "Randy", "Ricardo", "Shruti",
              "Yeshua"]

hangman = HangmanClase.Hangman(animalesCate) # Clase donde al iniciar el juego la categoría por defecto es la de animales
hangman.resetGame() # Método para reiniciar la jugada 

screenWidth = 860 # Ancho definido para la ventana
screenHeight = 670 # Alto definido para la ventana
ganar = pygame.display.set_mode((screenWidth, screenHeight)) # Se define las dimensiones en Pygame con las variables anteriores
pygame.display.set_caption("El Ahorcado") # Se define el nombre de la ventana 

fuenteBase = pygame.font.Font(None, 50) # Se define el tamaño de la fuente del primer título
fuenteEncabezado = pygame.font.Font(None, 32) # Se define el tamaño de la fuente de los subtítulos
fuenteMarcaDeAgua = pygame.font.Font(None, 20) # Se define el tamaño de la fuente de la categoría que se está jugando actualmente

# Se define en las variables los nombres de los encabezados para cada campo de la interfaz

inputEncab = 'Adivina la letra o la palabra:'
outputEncab = 'Comentario:'
palabractualEncab = 'Palabra actual:'
letrausadaEncab = 'Letras usadas:'
letrausadaLista = ''
inputTexto = ''
outputTexto = ''
animalEncab = 'Animales'
provinciaEncab = 'Provincias'
frutaEncab = 'Frutas'
paisEncab = 'Países'
alumnosEncab = 'Alumnos'

# Se designa en las variables el camino de los archivos de recursos PNG y WAV a utilizar en la interfaz

refrescarLogoPath = recursos('img/refresh.png')
silenciarPath = recursos('img/mute.png')
noSilenciarPath = recursos('img/notMute.png')
hangman0Path = recursos('img/hangman0.png')
hangman1Path = recursos('img/hangman1.png')
hangman2Path = recursos('img/hangman2.png')
hangman3Path = recursos('img/hangman3.png')
hangman4Path = recursos('img/hangman4.png')
hangman5Path = recursos('img/hangman5.png')
hangman6Path = recursos('img/hangman6.png')
fondoPath = recursos('img/paperBackground.jpg')
iconoPath = recursos('img/hangmanLogo.png')
errorSonidoPath = recursos('sound/wrong.wav')
correctoSonidoPath = recursos('sound/correct.wav')
perderSonidoPath = recursos('sound/lost.wav')
ganarSonidoPath = recursos('sound/won.wav')

# Se designa la funcion para retornar las imagenes del monigote como recursos en la superficie

refrescarLogo = pygame.image.load(refrescarLogoPath)
mute = pygame.image.load(silenciarPath)
notMute = pygame.image.load(noSilenciarPath)
hangman0 = pygame.image.load(hangman0Path)
hangman1 = pygame.image.load(hangman1Path)
hangman2 = pygame.image.load(hangman2Path)
hangman3 = pygame.image.load(hangman3Path)
hangman4 = pygame.image.load(hangman4Path)
hangman5 = pygame.image.load(hangman5Path)
hangman6 = pygame.image.load(hangman6Path)
fondo = pygame.image.load(fondoPath)
icon = pygame.image.load(iconoPath)

# Se designa el tamaño en escala del fondo e ícono de la ventana

fondo = pygame.transform.scale(fondo, (screenWidth, screenHeight)) # Tamaño para el fondo de la pantalla
icon = pygame.transform.scale(icon, (32, 32)) # Tamaño para el ícono de la ventana

pygame.display.set_icon(icon) # Se designa el ícono o logo para la ventana

# Se designa la funcion para retornar los sonidos de las acciones como recursos en la superficie

errorSonido = pygame.mixer.Sound(errorSonidoPath)
correctoSonido = pygame.mixer.Sound(correctoSonidoPath)
perderSonido = pygame.mixer.Sound(perderSonidoPath)
ganarSonido = pygame.mixer.Sound(ganarSonidoPath)

# Se designa el tamaño para cada recuadro de los campos y de los botones de la interfaz 

inputRect = pygame.Rect(10, 10, 580, 140)
outputRect = pygame.Rect(10, 160, 580, 140)
palabractualRect = pygame.Rect(10, 310, 580, 140)
letrausadaRect = pygame.Rect(10, 460, 580, 140)
refrescarBtn = pygame.Rect(600, 460, 250, 140)
animalBtn = pygame.Rect(10, 610, 160, 50)
provinciaBtn = pygame.Rect(180, 610, 160, 50)
frutaBtn = pygame.Rect(350, 610, 160, 50)
paisBtn = pygame.Rect(520, 610, 160, 50)
alumnosBtn = pygame.Rect(690, 610, 160, 50)
sonidoBtn = pygame.Rect(screenWidth - 28, 3, 24, 20)


colorActivo = pygame.Color('gray27') # Se designa el color gris oscuro para el fondo del primer recuadro
colorPasivo = pygame.Color('gray15') # Se designa el color gris tenue para el fondo de los subtítulos
color = colorPasivo

activar = True # Variable para habilitar el sonido en el juego
sonidoControl = True # Variable para de control para el sonido

# Ingreso de datos

while True:
    palabractual = hangman.getActualPalabra() # Se llama al método para la palabra escogida aleatoriamente para jugar
    letrausada = '' # Se designa para esta variable la letra ingresada correctamente
    letrausada2 = '' # Se designa para esta variable la letra ingresada errónea
    for x in hangman.getLetrasUsadas(): # Se llama al método de las letras ingresadas
        if len(letrausada) < 20:
            letrausada += x + ' ' # Acumulador para la letra correcta ingresada 
        else:
            letrausada2 += x + ' ' # Acumulador para la letra errada ingresada 

    for event in pygame.event.get(): # Se designa la finalización de la partida jugada
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN: # Módulo que permite hacer click en los botones
            if inputRect.collidepoint(event.pos): 
                active=True
            elif sonidoBtn.collidepoint(event.pos): # Click que se realiza en el botón para activar o desactivar el sonido
                if sonidoControl == True:
                    sonidoControl = False
                else:
                    sonidoControl = True
            elif refrescarBtn.collidepoint(event.pos):  # Click que se realiza en el botón para cambiar de palabra dentro de la partida
                hangman.resetGame()
                inputTexto = ''
                outputTexto = ''
            elif animalBtn.collidepoint(event.pos): # Click que se realiza en el botón para jugar en la categoría de animales
                hangman = HangmanClase.Hangman(animalesCate) 
                hangman.resetGame()
                inputTexto = ''
                outputTexto = ''
            elif provinciaBtn.collidepoint(event.pos): # Click que se realiza en el botón para jugar en la categoría de provincias
                hangman = HangmanClase.Hangman(provinciasCate)
                hangman.resetGame()
                inputTexto = ''
                outputTexto = ''
            elif frutaBtn.collidepoint(event.pos): # Click que se realiza en el botón para jugar en la categoría de frutas
                hangman = HangmanClase.Hangman(frutaCate)
                hangman.resetGame()
                inputTexto = ''
                outputTexto = ''
            elif paisBtn.collidepoint(event.pos): # Click que se realiza en el botón para jugar en la categoría de países
                hangman = HangmanClase.Hangman(paisesCate)
                hangman.resetGame()
                inputTexto = ''
                outputTexto = ''
            elif alumnosBtn.collidepoint(event.pos): # Click que se realiza en el botón para jugar en la categoría de alumnos
                hangman = HangmanClase.Hangman(est121List)
                hangman.resetGame()
                inputTexto = ''
                outputTexto = ''
            else:
                activar=False

        if event.type == pygame.KEYDOWN: # Función para detectar el ingreso de alguna letra en el juego
            if activar == True:
                if event.key == pygame.K_BACKSPACE:
                    inputTexto = inputTexto[:-1] # Ingreso de la letra a evauluar
                elif event.key == pygame.K_RETURN:
                    if len(inputTexto) > 0:
                        outputTexto = hangman.adivinarLetra(inputTexto) # Se utiliza el método adivinarLetra para determinar la salida de retroalimentación
                        inputTexto = ''
                        if sonidoControl == True: 
                            if outputTexto == 'Incorrecto': # Se activa el sonido de error si es incorrecta la letra ingresada
                                pygame.mixer.Sound.play(errorSonido)
                            elif outputTexto == 'Correcto': # Se activa el sonido de correcto si es correcta la letra ingresada
                                pygame.mixer.Sound.play(correctoSonido)
                            elif outputTexto == 'Perdiste!': # Se activa el sonido de perder si perdiste con la letra ingresada
                                pygame.mixer.Sound.play(perderSonido)
                            elif outputTexto == 'Ganaste!': # Se activa el sonido de ganar si ganaste con la letra ingresada
                                pygame.mixer.Sound.play(ganarSonido)
                else:
                    inputTexto += event.unicode

    ganar.fill(pygame.Color('floralwhite')) # Color para el texto de los recuadros grises
    ganar.blit(fondo, (0, 0))

    # Designar color según su intensidad

    if activar:
        color = colorActivo
    else:
        color = colorPasivo

    # Designar sonido según el click realizado

    if sonidoControl:
        soundLogo = notMute
    else:
        soundLogo = mute


    # Se designa la imagen del monigote según los intentos incorrectos realizados

    if hangman.getIntentos() == 0:
        hangmanImage = hangman0
    elif hangman.getIntentos() == 1:
        hangmanImage = hangman1
    elif hangman.getIntentos() == 2:
        hangmanImage = hangman2
    elif hangman.getIntentos() == 3:
        hangmanImage = hangman3
    elif hangman.getIntentos() == 4:
        hangmanImage = hangman4
    elif hangman.getIntentos() == 5:
        hangmanImage = hangman5
    elif hangman.getIntentos() == 6:
        hangmanImage = hangman6

    # Se designa el tamaño en escala para las imágenes del monigote
    hangmanImage = pygame.transform.scale(hangmanImage, (300, 400))

    # Se designa el estado de la categoría actual en jugar

    if hangman.getCategorias() == animalesCate:
        currentWordList = 'Categoría actual: Animales'
    elif hangman.getCategorias() == provinciasCate:
        currentWordList = 'Categoría actual: Provincias'
    elif hangman.getCategorias() == frutaCate:
        currentWordList = 'Categoría actual: Frutas'
    elif hangman.getCategorias() == paisesCate:
        currentWordList = 'Categoría actual: Países'
    elif hangman.getCategorias() == est121List:
        currentWordList = 'Categoría actual: Alumnos'

    # Se designa los colores de fondo utilizados para la interfaz
    
    pygame.draw.rect(ganar, color, inputRect)
    pygame.draw.rect(ganar, pygame.Color('gray15'), outputRect)
    pygame.draw.rect(ganar, pygame.Color('gray15'), palabractualRect)
    pygame.draw.rect(ganar, pygame.Color('gray15'), letrausadaRect)
    pygame.draw.rect(ganar, pygame.Color('skyblue'), refrescarBtn)
    pygame.draw.rect(ganar, pygame.Color('indianred1'), animalBtn)
    pygame.draw.rect(ganar, pygame.Color('indianred1'), provinciaBtn)
    pygame.draw.rect(ganar, pygame.Color('indianred1'), frutaBtn)
    pygame.draw.rect(ganar, pygame.Color('indianred1'), paisBtn)
    pygame.draw.rect(ganar, pygame.Color('indianred1'), alumnosBtn)


    # Se designa la tonalidad de colores para los recuadros y letras o palabras de la interfaz

    inputSuperficie = fuenteBase.render(inputTexto,True, (255,255,255))
    inputEncabSuperficie = fuenteBase.render(inputEncab, True, (255,255,255))
    resultadoSuperficie = fuenteBase.render(outputTexto, True, (255,255,255))
    resultadoEncabSuperficie = fuenteEncabezado.render(outputEncab, True, (255,255,255))
    actualSuperficie = fuenteBase.render(palabractual,True, (255,255,255))
    actualEncabSuperficie = fuenteEncabezado.render(palabractualEncab, True, (255,255,255))
    letrausadaSuperficie = fuenteBase.render(letrausada, True, (255, 255, 255))
    letrausadaSuperficie2 = fuenteBase.render(letrausada2, True, (255, 255, 255))
    letrausadaEncabSuperficie = fuenteEncabezado.render(letrausadaEncab, True, (255, 255, 255))
    categoriaSuperficie = fuenteMarcaDeAgua.render(currentWordList, True, pygame.Color('gray27'))
    animalEncabSuperficie = fuenteEncabezado.render(animalEncab, True, (0, 0, 0))
    provinciaEncabSuperficie = fuenteEncabezado.render(provinciaEncab, True, (0, 0, 0))
    frutaEncabSuperficie = fuenteEncabezado.render(frutaEncab, True, (0, 0, 0))
    paisEncabSuperficie = fuenteEncabezado.render(paisEncab, True, (0, 0, 0))
    alumnosEncabSuperficie = fuenteEncabezado.render(alumnosEncab, True, (0, 0, 0))

    # Se designa las posiciones en los ejes x y y para las superficies de la interfaz

    ganar.blit(inputSuperficie,(inputRect.x + 5, inputRect.y + 60))
    ganar.blit(inputEncabSuperficie, (inputRect.x + 5, inputRect.y + 5))
    ganar.blit(resultadoSuperficie, (outputRect.x + 5, outputRect.y + 50))
    ganar.blit(resultadoEncabSuperficie, (outputRect.x + 5, outputRect.y + 5))
    ganar.blit(actualSuperficie, (palabractualRect.x + 5, palabractualRect.y + 45))
    ganar.blit(actualEncabSuperficie, (palabractualRect.x + 5, palabractualRect.y + 5))
    ganar.blit(letrausadaSuperficie, (letrausadaRect.x + 5, letrausadaRect.y + 40))
    ganar.blit(letrausadaSuperficie2, (letrausadaRect.x + 5, letrausadaRect.y + 80))
    ganar.blit(letrausadaEncabSuperficie, (letrausadaRect.x + 5, letrausadaRect.y + 5))
    ganar.blit(refrescarLogo, (refrescarBtn.x + 75, refrescarBtn.y + 25))
    ganar.blit(hangmanImage, (575, 30))
    ganar.blit(categoriaSuperficie, (600, 8))
    ganar.blit(animalEncabSuperficie, (animalBtn.x + 30, animalBtn.y + 15))
    ganar.blit(provinciaEncabSuperficie, (provinciaBtn.x + 26, provinciaBtn.y + 15))
    ganar.blit(frutaEncabSuperficie, (frutaBtn.x + 47, frutaBtn.y + 15))
    ganar.blit(paisEncabSuperficie, (paisBtn.x + 47, paisBtn.y + 15))
    ganar.blit(alumnosEncabSuperficie, (alumnosBtn.x + 35, alumnosBtn.y + 15))
    ganar.blit(soundLogo, (screenWidth - 25, 2))

    pygame.display.flip()