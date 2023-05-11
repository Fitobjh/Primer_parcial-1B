'''
Adolfo Pumacayo 1B Primer Parcial
'''
import json
from funciones_primer_parcial import * 
from os import system

ingresar_salir("MENU")
menu = ["1-Traer datos desde archivo",
        "2-Listar cantidad por raza",
        "3-Listar personajes por raza",
        "4-Listar personajes por habilidad",
        "5-Jugar batalla",
        "6-Guardar Json",
        "7-Leer Json",
        "8-SALIR",]

seguir = True

while seguir == True:
    mostrar_menu(menu)
    respuesta = int(input("Ingrese una opcion: "))
    
    match respuesta:
        case 1:
            lista = parser_csv('DBZ.csv')
            mostrar_datos(lista)
        case 2:
            lista = parser_csv('DBZ.csv')
            mostrar_contador_raza(lista, 'raza')
        case 3:
            lista = parser_csv('DBZ.csv')
            mostrar_heroes_raza(lista)
        case 4:
            lista = parser_csv('DBZ.csv')
            mostrar_personajes_por_habilidad(lista)
        case 5:
            lista = parser_csv('DBZ.csv')
            jugar_batalla(lista)
        case 6:
            lista = parser_csv('DBZ.csv')
            nombre_archivo = guardar_json(lista)
            leer_json(nombre_archivo)
        case 7:
            lista = parser_csv('DBZ.csv')
            guardar_json(lista)
        case 8:
            ingresar_salir("Saliste")
            seguir = False
    input("\nEnter para continuar\n")