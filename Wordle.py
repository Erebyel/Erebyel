import random

palabras = ['ACARO',  'OREJA',  'AGUJA',  'AMADA',  'ANDEN',  'ANGEL',  'ARBOL',  'ARPIA',  'AVENA',  'AVION',  'BALSA',  'BANCO',  'BARCA',  'BELFO',  'BOTON',  'BRAGA',  'BRISA',  'BRUJA',  'CANOA',  'CARTA',  'CIELO',  'CISNE',  'COFRE',  'CUEVA',  'DARDO',  'DATIL',  'DIODO',  'DIQUE',  'DOLOR',  'DROGA',  'ENANO',  'EPOCA',  'FAROL',  'FENIX',  'FEUDO',  'FIERA',  'FLOTA',  'FRESA',  'FRUTA',  'FUEGO',  'GALLO',  'GLOBO',  'GRASA',  'HACHA',  'HIDRA',  'HIENA',  'HOGAR',  'HUESO',  'HURON',  'JABON',  'JAMON',  'JARRA',  'JAULA',  'JERBO',  'JUSTA',  'LANZA',  'LIBRO',  'LICOR',  'LIGUE',  'LIMON',  'LINCE',  'LLAVE',  'MAMUT',  'MANTA',  'MEIGA',  'MIRLO',  'MONTE',  'MOSCA',  'NARIZ',  'NIEVE',  'NINFA',  'NOCHE',  'NORIA',  'NYLON',  'ÑANDU',  'OASIS',  'ORATE',  'OREJA',  'OSTRA',  'OTOÑO',  'OVEJA',  'PERRO',  'PLANO',  'PLATA',  'PLAYA',  'PLUMA',  'PULGA',  'RADIO',  'RATON',  'REINA',  'REINO',  'ROCIO',  'RUINA',  'SALUD',  'SUEÑO',  'TIFON',  'TIMON',  'TORRE',  'TRIGO',  'TROLL',  'TUCAN',  'TUMBA',  'VAGON',  'VALLE',  'VIEJO',  'VODKA',  'VUELO',  'YEGUA',  'YOGUR',  'CEBRA',  'ZORRO',  'ZUECO']

def selector():
    '''Selecciona una palabra aleatoria del diccionario que el jugador deberá adivinar para poder iniciar el juego.'''
    return palabras[random.randint(1, len(palabras)-1)].upper()

def iniciar(palabra):
    '''Función con la que el jugador elige la palabra con la que va a jugar la ronda.'''
    return input('Introduce una palabra de 5 letras: ').upper()

def Wordle(jugador, palabra):
    programa = list(palabra)
    propuesta = list(jugador)

    esta = []
    for caracter in propuesta:
        if caracter in programa:
            esta.append(caracter)
    esta = sorted(set(esta))
    if esta:
        print('Las siguientes letras están, pero no en el orden correcto: ' + ', '.join(esta))
    else:
        print('Ninguna de las letras está en la palabra que debes adivinar.')

    respuesta =[]
    for posicion in range(len(propuesta)):
        if programa[posicion] != propuesta[posicion]:
            respuesta.append('_')
        else:
            respuesta.append(propuesta[posicion])

    coincide_lugar = []
    for lugar in range(len(palabra)):
        if programa[lugar] == propuesta[lugar]:
            coincide_lugar.append(propuesta[lugar])

    if len(set(respuesta)) != 1:
        print('Las siguientes letras están en el orden correcto: ' + ' '.join(respuesta))
    else:
        print('Lo siento, tu palabra no contiene ninguna coincidencia con la que debes adivinar.')

def juego():
    contador = 0
    palabra = selector()
    while (contador < 5):
        contador += 1
        print('\n\n||====RONDA ' + str(contador) + '====||')
        jugador = iniciar(palabra)

        if len(jugador) != len(palabra):
            print('Lo sentimos, tu palabra, ' + str(jugador).lower() + ', tiene ' + str(len(jugador)) + ' letras y buscamos una palabra de 5; introduce otra.')

        elif palabra != jugador:
            Wordle(jugador, palabra)

        elif palabra == jugador:
            print('¡Enorabuena! Has adivinado la palabra en ' + str(contador) + ' intentos.')
            contador = 6

    if palabra != jugador:
        print('\n||====SE ACABÓ====||\nLo siento, has superado el número de intentos, la palabra era: ' + palabra)

        
jugar = 'S'
while 'S' in list(jugar):
    juego()
    jugar = input('¿Quieres jugar de nuevo? Responda: S/N \n Respuesta:').upper()
