from data_stark import lista_personajes
import os


def menu():
    os.system("cls")
    print("""
                        ***MENU 00 STARK*** 
            1. nombre de cada superhéroe
            2. nombre de cada superhéroe junto a altura del mismo
            3. el superhéroe más alto (MÁXIMO)
            4. el superhéroe más bajo (MÍNIMO)
            5. la altura promedio de los superhéroes (PROMEDIO)
            6. el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
            7. Calcular e informar cual es el superhéroe más y menos pesado.
            8. MENU 01
            9. SALIR    
          """)
    
    try:
        seleccion = int(input("seleccione uno de estos numeros: "))
        
    except ValueError:
        print("debes seleccionar un numero")
    else:
        while (seleccion <= 0 or seleccion >= 11):
            print(int(input("elige un numero entre 1 y 10: ")))
            
        return seleccion


def resultado(seleccion):
    match(seleccion):
        case 1:
            print(nombres)
        case 2:
            print(nombres_altruas)
        case 3:
            print(altura_max)
        case 4:
            print(altura_min)
        case 5:
            print(promedio_alturas)
        case 6:
            print(max_min)
        case 7:
            print(peso_max_min)
        case 8:
            print(menu_01)
        case 9:
            salida = input("Desea salir? s/n: ")
            while salida == "s" or salida == "n":
                break
                
    return seleccion


def superheroes(lista: list, key: str) -> list:
    list_nombres = []
    for heroe in lista:
        list_nombres.append(heroe[key])

    return list_nombres


def heroes_altura(lista: list, nombre: str, altura: str) -> list:
    nombres = []
    alturas = []

    for hero in lista:
        nombres.append(hero[nombre])
        alturas.append(float(hero[altura]))
    return nombres, alturas


def hero_max(lista: list, nombre: str, altura: str):
    name_max = None
    flag_max = True
    for hero in lista:
        if flag_max or altura_max > float(hero[altura]):
            altura_max = float(hero[altura])
            name_max = hero[nombre]
            flag_max = False

    return (name_max, altura_max)


def hero_min(lista: list, nombre: str, altura: str):
    name_min = None
    flag_min = True
    for hero in lista:
        if flag_min or altura_min > float(hero[altura]):
            altura_min = float(hero[altura])
            name_min = hero[nombre]
            flag_min = False

    return (name_min, altura_min)


def hero_promedio(lista: list, altura: str):
    acumulador = 0
    contador = 0
    for hero in lista:
        acumulador += float(hero[altura])
        contador += 1

    promedio = acumulador / contador

    return promedio


def hero_peso(lista: list, nombre: str, peso: str,):
    name_max = None
    flag_max = True
    name_min = None
    flag_min = True
    
    for hero in lista:
        if flag_max or float(hero[peso]) > peso_max:
            peso_max = float(hero[peso])
            name_max = hero[nombre]
            flag_max = False
            
    for hero in lista:
        if flag_min or float(hero[peso]) < peso_min:
            peso_min = float(hero[peso])
            name_min = hero[nombre]
            flag_min = False

    return (name_min, peso_min),(name_max,peso_max)


nombres = superheroes(lista_personajes, "nombre")
nombres_altruas = heroes_altura(lista_personajes, "nombre", "altura")
altura_max = hero_max(lista_personajes, "nombre", "altura")
altura_min = hero_min(lista_personajes, "nombre", "altura")
promedio_alturas = hero_promedio(lista_personajes, "altura")
max_min = altura_max, altura_min
peso_max_min = hero_peso(lista_personajes,"nombre","peso")

#---------------------------------------------------------------------------------------------

def menu_01 ():
    print("""
                                    *** MENU 01 *** 
            1.el nombre de cada superhéroe de género M
            2.el nombre de cada superhéroe de género F
            3. el superhéroe más alto de género M
            4. el superhéroe más alto de género F
            5. el superhéroe más bajo de género M
            6. el superhéroe más bajo de género F
            7. la altura promedio de los superhéroes de género M
            8. la altura promedio de los superhéroes de género F
            9. el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
            10. cuántos superhéroes tienen cada tipo de color de ojos.
            11. cuántos superhéroes tienen cada tipo de color de pelo.
            12. cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, ‘No Tiene’).
            13. todos los superhéroes agrupados por color de ojos.
            14. todos los superhéroes agrupados por color de pelo.
            15. todos los superhéroes agrupados por tipo de inteligencia
        """)
    try:
        seleccion_01 = int(input("seleccione uno de estos numeros: "))
    except ValueError:
        print("debes seleccionar un numero")
    else:
        while (seleccion_01 <= 0 or seleccion_01 >= 11):
            print(int(input("elige un numero entre 1 y 10: ")))

        return seleccion_01
    
def resultado_01(seleccion_01):
    match(seleccion_01):
        case 1:
            print(nombres)
        case 2:
            print(nombres_altruas)
        case 3:
            print(altura_max)
        case 4:
            print(altura_min)
        case 5:
            print(promedio_alturas)
        case 6:
            print(max_min)
        case 7:
            print(peso_max_min)
        case 8:
            print(menu_01)
        case 9:
            salida = input("Desea salir? s/n: ")
            while salida == "s" or salida == "n":
                break
                
    return seleccion_01