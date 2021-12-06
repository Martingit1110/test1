from random import choice, randint
from typing import List
from typing import Dict


def inicializar_tablero() -> list:
    tablero: list = []
    numero_casilla: int  = 1
    for i in range(10):
        fila: list = []
        tablero.append(fila)
        for j in range(10):
            fila.append(numero_casilla)
            numero_casilla += 1
    return tablero

def imprimir_tablero(nombre_jugador_1: str, nombre_jugador_2: str, tablero: list) -> None:
    numeros_una_cifra: tuple = (1,2,3,4,5,6,7,8,9)
    casillas_especiales: tuple = ("Esca","Serp","C.B.","C.M.","C.R.","H.L.")
    caracteres: tuple = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    for i in range(9, -1, -1):
        if i % 2 != 0:
            for j in range(9, -1, -1):
                if tablero[i][j] in casillas_especiales:
                    print(tablero[i][j], end = "   ")
                elif tablero[i][j] == 100:
                        print(tablero[i][j], end = "    ")
                elif tablero[i][j] in caracteres:
                        print(tablero[i][j], end = "      ")
                elif tablero[i][j] == f"{nombre_jugador_1} y {nombre_jugador_2}":
                    print(tablero[i][j], end = "  ")
                else:
                    print(tablero[i][j], end = "     ")
        else:
            for j in range(10):
                if tablero[i][j] in casillas_especiales:
                    print(tablero[i][j], end = "   ")
                elif tablero[i][j] in numeros_una_cifra:
                    print(tablero[i][j], end = "      ")
                elif tablero[i][j] in caracteres:
                        print(tablero[i][j], end = "      ")
                elif tablero[i][j] == f"{nombre_jugador_1} y {nombre_jugador_2}":
                    print(tablero[i][j], end = "  ")
                else:
                    print(tablero[i][j], end = "     ")
        print(" \n")

def iniciar_partida() -> list:
    print("¡Bienvenidos a serpientes y escaleras!\n")
    jugadores: list = [] 
    for i in range(2):
        jugadores.append(input(f"¿Jugador número {i + 1}, cúal es su nombre?\n"))
    jugadores.append(choice(jugadores))
    if jugadores[0] == jugadores[2]:
        del jugadores[2]
    else:
        jugadores[2] = jugadores[0]
        del jugadores[0]
    return jugadores

def dado() -> int:
    numero: int = randint(1,6)
    print(f"¡Te salió un {numero}!")
    return numero

def movimiento(posicion_jugador: int, numero: int) -> int:
    posicion_jugador += numero 
    if posicion_jugador > 100:
        posicion_jugador = 100
    print(f"¡Estas en la casilla {posicion_jugador}!\n")
    return posicion_jugador

def posicion_matriz_lista(posicion_jugador: int, tablero_espejo: list) -> list:
    posicion_matriz: list = []
    for fila in range(len(tablero_espejo)):
        for columna in range(len(tablero_espejo[fila])):
            if tablero_espejo[fila][columna] == posicion_jugador:
                posicion_matriz.append(fila)
                posicion_matriz.append(columna)
    return posicion_matriz

def poner_caracter(posicion_matriz_1: list, jugador_1_caracter: str, posicion_matriz_descarte_1: list, posicion_descarte_1: int, posicion_matriz_2: list, jugador_2_caracter: str, posicion_matriz_descarte_2: list, posicion_descarte_2: int, tablero: list) -> list:              
    tablero[posicion_matriz_descarte_1[0]][posicion_matriz_descarte_1[1]] = posicion_descarte_1
    tablero[posicion_matriz_1[0]][posicion_matriz_1[1]] = jugador_1_caracter.capitalize()
    tablero[posicion_matriz_descarte_2[0]][posicion_matriz_descarte_2[1]] = posicion_descarte_2
    tablero[posicion_matriz_2[0]][posicion_matriz_2[1]] = jugador_2_caracter.capitalize()
    if tablero[posicion_matriz_1[0]][posicion_matriz_1[1]] == tablero[posicion_matriz_2[0]][posicion_matriz_2[1]]:
        tablero[posicion_matriz_1[0]][posicion_matriz_1[1]] = f"{jugador_1_caracter.capitalize()} y {jugador_2_caracter.capitalize()}"
    return tablero

        
def turno(nombre_jugador: str, posicion_jugador: int, posicion_matriz: list, escaleras_y_serpientes: dict, numero: int, tablero: list, tablero_espejo: list, fin_del_tablero: int, estadistica_casilleros: list) -> tuple:
    posicion_jugador: int = movimiento(posicion_jugador, numero)
    posicion_matriz: list = posicion_matriz_lista(posicion_jugador, tablero_espejo)
    while tablero[posicion_matriz[0]][posicion_matriz[1]] == "Esca" or tablero[posicion_matriz[0]][posicion_matriz[1]] == "Serp" or tablero[posicion_matriz[0]][posicion_matriz[1]] == "C.B." or tablero[posicion_matriz[0]][posicion_matriz[1]] == "C.M." or tablero[posicion_matriz[0]][posicion_matriz[1]] == "C.R." or tablero[posicion_matriz[0]][posicion_matriz[1]] == "H.L.":
        datos: tuple = checkeo_casilleros_especiales(nombre_jugador, posicion_jugador, posicion_matriz, escaleras_y_serpientes, tablero, tablero_espejo, estadistica_casilleros)
        posicion_jugador: int = datos[0]
        estadistica_casilleros: list = datos[1]
        posicion_matriz: list = posicion_matriz_lista(posicion_jugador, tablero_espejo)
    if posicion_jugador >= fin_del_tablero:
        print(f"¡{nombre_jugador} ganaste el juego, felicitaciones!\n")
    return posicion_jugador, estadistica_casilleros

def crear_escaleras_y_serpientes(escaleras_y_serpientes: dict, tablero: list) -> list:
    for i in escaleras_y_serpientes.keys():
        if i < escaleras_y_serpientes[i]:
            for fila in range(len(tablero)):
                for columna in range(len(tablero[fila])):
                    if tablero[fila][columna] == i:
                        tablero[fila][columna] = "Esca"
        else:
            for fila in range(len(tablero)):
                    for columna in range(len(tablero[fila])):
                        if tablero[fila][columna] == i:
                            tablero[fila][columna] = "Serp"
    return tablero

def crear_casillero_cascara_banana(escaleras_y_serpientes: list, tablero: list) -> list:
    casillero_cascara_banana: str = "C.B."
    cantidad_de_casilleros: int = 5
    posicion_casillero_banana: list = [0,0] 
    for i in range(cantidad_de_casilleros):
        ubicar_cascara_de_banana(casillero_cascara_banana, posicion_casillero_banana, escaleras_y_serpientes, tablero) 
    return tablero

def ubicar_cascara_de_banana(casillero_cascara_banana: str, posicion_casillero_banana: list, escaleras_y_serpientes: dict, tablero: list) -> list:
    posicion_casillero_banana[0] = randint(2,9) 
    posicion_casillero_banana[1] = randint(0,9)
    casilla_random: int or str = tablero[posicion_casillero_banana[0]][posicion_casillero_banana[1]]
    if casilla_random == "Esca": 
        ubicar_cascara_de_banana(casillero_cascara_banana, posicion_casillero_banana, escaleras_y_serpientes, tablero)
    elif casilla_random == "Serp": 
        ubicar_cascara_de_banana(casillero_cascara_banana, posicion_casillero_banana, escaleras_y_serpientes, tablero)
    elif casilla_random in escaleras_y_serpientes.values(): 
        ubicar_cascara_de_banana(casillero_cascara_banana, posicion_casillero_banana, escaleras_y_serpientes, tablero)
    elif casilla_random == "C.B.": 
        ubicar_cascara_de_banana(casillero_cascara_banana, posicion_casillero_banana, escaleras_y_serpientes, tablero)
    elif casilla_random == 100:
        ubicar_cascara_de_banana(casillero_cascara_banana, posicion_casillero_banana, escaleras_y_serpientes, tablero)
    elif casilla_random == 0:
        ubicar_cascara_de_banana(casillero_cascara_banana, posicion_casillero_banana, escaleras_y_serpientes, tablero)
    tablero[posicion_casillero_banana[0]][posicion_casillero_banana[1]] = casillero_cascara_banana
    return tablero

def crear_casillero_magico(escaleras_y_serpientes: list, tablero: list) -> list:
    casillero_magico: str = "C.M."
    cantidad_de_casilleros: int = 3
    posicion_casillero_magico: list = [0,0] 
    for i in range(cantidad_de_casilleros):
        ubicar_casillero_magico(casillero_magico, posicion_casillero_magico, escaleras_y_serpientes, tablero) 
    return tablero

def ubicar_casillero_magico(casillero_magico: str, posicion_casillero_magico: list, escaleras_y_serpientes: dict, tablero: list) -> list:
    posicion_casillero_magico[0] = randint(0,9) 
    posicion_casillero_magico[1] = randint(0,9)
    casilla_random: int or str = tablero[posicion_casillero_magico[0]][posicion_casillero_magico[1]]
    if casilla_random == "Esca": 
        ubicar_casillero_magico(casillero_magico, posicion_casillero_magico, escaleras_y_serpientes, tablero)
    elif casilla_random == "Serp": 
        ubicar_casillero_magico(casillero_magico, posicion_casillero_magico, escaleras_y_serpientes, tablero)
    elif casilla_random in escaleras_y_serpientes.values(): 
        ubicar_casillero_magico(casillero_magico, posicion_casillero_magico, escaleras_y_serpientes, tablero)
    elif casilla_random == "C.B.": 
        ubicar_casillero_magico(casillero_magico, posicion_casillero_magico, escaleras_y_serpientes, tablero)
    elif casilla_random == "C.M.": 
        ubicar_casillero_magico(casillero_magico, posicion_casillero_magico, escaleras_y_serpientes, tablero)
    elif casilla_random == 100:
        ubicar_casillero_magico(casillero_magico, posicion_casillero_magico, escaleras_y_serpientes, tablero)
    elif casilla_random == 0:
        ubicar_casillero_magico(casillero_magico, posicion_casillero_magico, escaleras_y_serpientes, tablero)
    tablero[posicion_casillero_magico[0]][posicion_casillero_magico[1]] = casillero_magico
    return tablero

def crear_casillero_rushero(escaleras_y_serpientes: list, tablero: list) -> list:
    casillero_rushero: str = "C.R."
    cantidad_de_casilleros: int = 1
    posicion_casillero_rushero: list = [0,0] 
    for i in range(cantidad_de_casilleros):
        ubicar_casillero_rushero(casillero_rushero, posicion_casillero_rushero, escaleras_y_serpientes, tablero) 
    return tablero

def ubicar_casillero_rushero(casillero_rushero: str, posicion_casillero_rushero: list, escaleras_y_serpientes: dict, tablero: list) -> list:
    posicion_casillero_rushero[0] = randint(0,9) 
    posicion_casillero_rushero[1] = randint(0,8)
    casilla_random: int or str = tablero[posicion_casillero_rushero[0]][posicion_casillero_rushero[1]]
    if casilla_random == "Esca": 
        ubicar_casillero_rushero(casillero_rushero, posicion_casillero_rushero, escaleras_y_serpientes, tablero)
    elif casilla_random == "Serp": 
        ubicar_casillero_rushero(casillero_rushero, posicion_casillero_rushero, escaleras_y_serpientes, tablero)
    elif casilla_random in escaleras_y_serpientes.values(): 
        ubicar_casillero_rushero(casillero_rushero, posicion_casillero_rushero, escaleras_y_serpientes, tablero)
    elif casilla_random == "C.B.": 
        ubicar_casillero_rushero(casillero_rushero, posicion_casillero_rushero, escaleras_y_serpientes, tablero)
    elif casilla_random == "C.M.": 
        ubicar_casillero_rushero(casillero_rushero, posicion_casillero_rushero, escaleras_y_serpientes, tablero)    
    elif casilla_random == "C.R.": 
        ubicar_casillero_rushero(casillero_rushero, posicion_casillero_rushero, escaleras_y_serpientes, tablero)
    elif casilla_random == 100:
        ubicar_casillero_rushero(casillero_rushero, posicion_casillero_rushero, escaleras_y_serpientes, tablero)
    elif casilla_random == 0:
        ubicar_casillero_rushero(casillero_rushero, posicion_casillero_rushero, escaleras_y_serpientes, tablero)
    tablero[posicion_casillero_rushero[0]][posicion_casillero_rushero[1]] = casillero_rushero
    return tablero

def crear_casillero_hongo_loco(escaleras_y_serpientes: list, tablero: list) -> list:
    casillero_hongo_loco: str = "H.L."
    cantidad_de_casilleros: int = 1
    posicion_casillero_hongo_loco: list = [0,0] 
    for i in range(cantidad_de_casilleros):
        ubicar_hongo_loco(casillero_hongo_loco, posicion_casillero_hongo_loco, escaleras_y_serpientes, tablero) 
    return tablero

def ubicar_hongo_loco(casillero_hongo_loco: str, posicion_casillero_hongo_loco: list, escaleras_y_serpientes: dict, tablero: list) -> list:
    posicion_casillero_hongo_loco[0] = randint(0,9) 
    posicion_casillero_hongo_loco[1] = randint(1,9)
    casilla_random: int or str = tablero[posicion_casillero_hongo_loco[0]][posicion_casillero_hongo_loco[1]]
    if casilla_random == "Esca": 
        ubicar_hongo_loco(casillero_hongo_loco, posicion_casillero_hongo_loco, escaleras_y_serpientes, tablero)
    elif casilla_random == "Serp": 
        ubicar_hongo_loco(casillero_hongo_loco, posicion_casillero_hongo_loco, escaleras_y_serpientes, tablero)
    elif casilla_random in escaleras_y_serpientes.values(): 
        ubicar_hongo_loco(casillero_hongo_loco, posicion_casillero_hongo_loco, escaleras_y_serpientes, tablero)
    elif casilla_random == "C.B.": 
        ubicar_hongo_loco(casillero_hongo_loco, posicion_casillero_hongo_loco, escaleras_y_serpientes, tablero)
    elif casilla_random == "C.M.": 
        ubicar_hongo_loco(casillero_hongo_loco, posicion_casillero_hongo_loco, escaleras_y_serpientes, tablero)
    elif casilla_random == "C.R.": 
        ubicar_hongo_loco(casillero_hongo_loco, posicion_casillero_hongo_loco, escaleras_y_serpientes, tablero)
    elif casilla_random == "H.L.": 
        ubicar_hongo_loco(casillero_hongo_loco, posicion_casillero_hongo_loco, escaleras_y_serpientes, tablero)
    elif casilla_random == 100:
        ubicar_hongo_loco(casillero_hongo_loco, posicion_casillero_hongo_loco, escaleras_y_serpientes, tablero)
    elif casilla_random == 0:
        ubicar_hongo_loco(casillero_hongo_loco, posicion_casillero_hongo_loco, escaleras_y_serpientes, tablero)
    tablero[posicion_casillero_hongo_loco[0]][posicion_casillero_hongo_loco[1]] = casillero_hongo_loco
    return tablero

def checkeo_casilleros_especiales(nombre_jugador: str, posicion_jugador: int, posicion_matriz: list, escaleras_y_serpientes: dict, tablero: list, tablero_espejo: list, estadistica_casilleros: list) -> tuple:        
    if tablero[posicion_matriz[0]][posicion_matriz[1]] == "C.B.":
        print(f"¡{nombre_jugador}, caíste en un casillero cascara de banana! Te caes 2 pisos (20 casilleros).")
        posicion_jugador -= 20
        estadistica_casilleros[2] += 1
        print(f"¡Estas en la casilla {posicion_jugador}!\n")
        posicion_matriz: list = posicion_matriz_lista(posicion_jugador, tablero_espejo)
    elif tablero[posicion_matriz[0]][posicion_matriz[1]] == "C.M.":
        print(f"¡{nombre_jugador}, caíste en un casillero magico! Te transportas a un casillero aleatorio del tablero.")
        posicion_jugador = randint(2,99)
        estadistica_casilleros[3] += 1
        print(f"¡Estas en la casilla {posicion_jugador}!\n")
        posicion_matriz: list = posicion_matriz_lista(posicion_jugador, tablero_espejo) 
    elif tablero[posicion_matriz[0]][posicion_matriz[1]] == "C.R.":
        print(f"¡Que suerte {nombre_jugador}, caíste en un casillero rushero! Corres hasta el final de la fila.")
        posicion_jugador = tablero_espejo[posicion_matriz[0]][9]
        estadistica_casilleros[4] += 1
        print(f"¡Estas en la casilla {posicion_jugador}!\n")
        posicion_matriz: list = posicion_matriz_lista(posicion_jugador, tablero_espejo)
    elif tablero[posicion_matriz[0]][posicion_matriz[1]] == "H.L.":
        print(f"¡Que mala suerte {nombre_jugador}, caíste en un casillero \"hongos locos\"! Corres hasta el principio de la fila.")
        posicion_jugador = tablero_espejo[posicion_matriz[0]][0]
        estadistica_casilleros[5] += 1
        print(f"¡Estas en la casilla {posicion_jugador}!\n")
        posicion_matriz: list = posicion_matriz_lista(posicion_jugador, tablero_espejo)
    elif tablero[posicion_matriz[0]][posicion_matriz[1]] == "Esca":
        print(f"¡{nombre_jugador}, caíste en una escalera!")
        posicion_jugador = escaleras_y_serpientes[posicion_jugador]
        estadistica_casilleros[0] += 1
        print(f"¡Estas en la casilla {posicion_jugador}!\n")
        posicion_matriz: list = posicion_matriz_lista(posicion_jugador, tablero_espejo)
    elif tablero[posicion_matriz[0]][posicion_matriz[1]] == "Serp":
        print(f"¡{nombre_jugador}, caíste en una serpiente!")
        posicion_jugador = escaleras_y_serpientes[posicion_jugador]
        estadistica_casilleros[1] += 1
        print(f"¡Estas en la casilla {posicion_jugador}!\n")
        posicion_matriz: list = posicion_matriz_lista(posicion_jugador, tablero_espejo)
    return posicion_jugador, estadistica_casilleros
    
def tablero_con_casillas_especiales(escaleras_y_serpientes: dict, tablero: list) -> list:
    crear_escaleras_y_serpientes(escaleras_y_serpientes, tablero)
    crear_casillero_cascara_banana(escaleras_y_serpientes, tablero)
    crear_casillero_magico(escaleras_y_serpientes, tablero)
    crear_casillero_rushero(escaleras_y_serpientes, tablero)
    crear_casillero_hongo_loco(escaleras_y_serpientes, tablero)
    return tablero

def checkear_ganador (fin_del_tablero: int,posicion_jugador: int) -> bool:
    if posicion_jugador >= fin_del_tablero:
        return True
    else:
        return False

def imprimir_escaleras_y_serpientes(escaleras_y_serpientes: dict) -> None:
    for i in escaleras_y_serpientes.keys():
        if i < escaleras_y_serpientes[i]:
            print(f"Escalera: casilla {i} -> casilla {escaleras_y_serpientes[i]}")
        else:
            print(f"Serpiente: casilla {i} -> casilla {escaleras_y_serpientes[i]}")

def juego() -> list:

    estadistica_casilleros: list = [0, 0, 0, 0, 0, 0]

    escaleras_y_serpientes: dict = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96, 86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}

    tablero: list = inicializar_tablero()
    tablero: list = tablero_con_casillas_especiales(escaleras_y_serpientes, tablero)
    tablero_espejo: list = inicializar_tablero()
        
    nombre_jugador_1: str = "jugador 1"
    nombre_jugador_2: str = "jugador 2"
        
    posicion_jugador_1: int = 1
    posicion_descarte_1: int = posicion_jugador_1
    posicion_matriz_1: list = [0,0]
    posicion_matriz_descarte_1: list = posicion_matriz_1

    posicion_jugador_2: int = 1
    posicion_descarte_2: int = posicion_jugador_2
    posicion_matriz_2: list = [0,0]
    posicion_matriz_descarte_2: list = posicion_matriz_2

    fin_del_tablero: int = 100
    ganada: bool = False

    jugadores: list = iniciar_partida()
    nombre_jugador_1: str = jugadores[0] 
    nombre_jugador_2: str = jugadores[1]
    jugador_1_caracter: str = nombre_jugador_1[:1]
    jugador_2_caracter: str = nombre_jugador_2[:1]
    
    input("A continuacion se mostrará valores de \"escaleras y serpientes\" y el tablero:\n")
    print("C.B. = Casillero \"cáscara de banana\"\nC.M. = Casillero \"mágico\"\nC.R. = Casillero \"rushero\"\nH.L. = Casillero \"hongos locos\"\n")
    imprimir_escaleras_y_serpientes(escaleras_y_serpientes)
    print()
    imprimir_tablero(nombre_jugador_1, nombre_jugador_2, tablero)

    while not ganada:
        input(f"¡{nombre_jugador_1} es tu turno!\n")
        print(f"¡Estas en la casilla {posicion_jugador_1}!")
        numero: int = dado()
        posicion_descarte_1: int = posicion_jugador_1
        posicion_matriz_descarte_1: list = posicion_matriz_1
        datos: tuple = turno(nombre_jugador_1, posicion_jugador_1, posicion_matriz_1, escaleras_y_serpientes, numero, tablero, tablero_espejo, fin_del_tablero, estadistica_casilleros)       
        posicion_jugador_1: int = datos[0]
        estadistica_casilleros: list = datos[1]
        posicion_matriz_1: list = posicion_matriz_lista(posicion_jugador_1, tablero_espejo)
        tablero = poner_caracter(posicion_matriz_1, jugador_1_caracter, posicion_matriz_descarte_1, posicion_descarte_1, posicion_matriz_2, jugador_2_caracter, posicion_matriz_descarte_2, posicion_descarte_2, tablero)
        input("A continuacion se mostrará valores de \"escaleras y serpientes\" y el tablero:\n")
        imprimir_escaleras_y_serpientes(escaleras_y_serpientes)
        print()
        imprimir_tablero(nombre_jugador_1, nombre_jugador_2, tablero)
        ganada: bool = checkear_ganador(fin_del_tablero, posicion_jugador_1)
        
        if not ganada:
            input(f"¡{nombre_jugador_2} es tu turno!\n")
            print(f"¡Estas en la casilla {posicion_jugador_2}!")
            numero: int = dado()
            posicion_descarte_2: int = posicion_jugador_2
            posicion_matriz_descarte_2: list = posicion_matriz_2
            datos: tuple = turno(nombre_jugador_2, posicion_jugador_2, posicion_matriz_2, escaleras_y_serpientes, numero, tablero, tablero_espejo, fin_del_tablero, estadistica_casilleros)
            posicion_jugador_2: int = datos[0]
            estadistica_casilleros: list = datos[1]
            posicion_matriz_2: list = posicion_matriz_lista(posicion_jugador_2, tablero_espejo)
            
            tablero = poner_caracter(posicion_matriz_1, jugador_1_caracter, posicion_matriz_descarte_1, posicion_descarte_1, posicion_matriz_2, jugador_2_caracter, posicion_matriz_descarte_2, posicion_descarte_2, tablero)       
            input("A continuacion se mostrará valores de \"escaleras y serpientes\" y el tablero:\n")
            imprimir_escaleras_y_serpientes(escaleras_y_serpientes)
            print()
            imprimir_tablero(nombre_jugador_1, nombre_jugador_2, tablero)
            ganada: bool = checkear_ganador(fin_del_tablero, posicion_jugador_2)

    return estadistica_casilleros

def salir(select: str) -> bool:
    if select == "Salir" or select == "salir" or select == "4":
        print("¡Gracias por jugar Escaleras y serpientes!\n")
        return True
    else:
        return False

def main() -> None:

    se_jugo_antes: bool = False
    terminar_programa: bool = False

    estadistica_escalera: int = 0
    estadistica_serpiente: int = 0
    estadistica_cascara_banana: int = 0
    estadistica_casillero_magico: int = 0
    estadistica_casillero_rushero: int = 0
    estadistica_hongos_locos: int = 0
    
    while not terminar_programa:
        print()
        print("Escaleras y serpientes\n\n") 
        print("1.Iniciar partida\n2.Mostrar estadisticas de casilleros\n3.Resetear estadisticas de casilleros\n4.Salir")
        select = input()
        print()
        if select == "Iniciar partida" or select == "iniciar partida" or select == "1":
            estadisticas: list = juego()
            estadistica_escalera += estadisticas[0]
            estadistica_serpiente += estadisticas[1]
            estadistica_cascara_banana += estadisticas[2]
            estadistica_casillero_magico += estadisticas[3]
            estadistica_casillero_rushero += estadisticas[4]
            estadistica_hongos_locos += estadisticas[5]
            se_jugo_antes = True
            print("Volviendo al menu principal...")
        elif select == "Mostrar estadisticas de casilleros" or select == "mostrar estadisticas de casilleros" or select == "2":
            if not se_jugo_antes:
                print("No hay estadisticas sobre los casilleros debido a que nunca se jugó una partida\n")
            else:
                print(f"Cantidad de escaleras utilizadas: {estadistica_escalera}\nCantidad de serpientes utilizadas: {estadistica_serpiente}\nCantidad de casilleros \"cascara de banana\" utilizados: {estadistica_cascara_banana}\nCantidad de casilleros magicos utilizados: {estadistica_casillero_magico}\nCantidad de casilleros rusheros utilizados: {estadistica_casillero_rushero}\nCantidad de casilleros \"hongos locos\" utilizados: {estadistica_hongos_locos}\n")
                print("Volviendo al menu principal...")
            
        elif select == "Resetear estadisticas de casilleros" or select == "resetear estadisticas de casilleros" or select == "3":
            if not se_jugo_antes:
                print("No se puede resetear las estadisticas sobre los casilleros debido a que nunca se jugó una partida.\n")
            else:
                estadistica_escalera: int = 0 
                estadistica_serpiente: int = 0
                estadistica_cascara_banana: int = 0
                estadistica_casillero_magico: int = 0
                estadistica_casillero_rushero: int = 0
                estadistica_hongos_locos: int = 0
                print(f"Las estadisticas de los casilleros se han reseteado:\n\n\nCantidad de escaleras utilizadas: {estadistica_escalera}\nCantidad de serpientes utilizadas: {estadistica_serpiente}\nCantidad de casilleros \"cascara de banana\" utilizados: {estadistica_cascara_banana}\nCantidad de casilleros magicos utilizados: {estadistica_casillero_magico}\nCantidad de casilleros rusheros utilizados: {estadistica_casillero_rushero}\nCantidad de casilleros \"hongos locos\" utilizados: {estadistica_hongos_locos}\n")
            print("Volviendo al menu principal...")
        else:
            terminar_programa: bool = salir(select)

main()


