import json
import re
import random
import datetime
'''
COSAS PARA OPTIMIZAR MI MENU:
'''
def mostrar_menu(menu:list)->None:
    for opcion in menu:
        print(opcion)

def mostrar_datos(cualquier_dato)->None: #La uso solo cuando retornan algo sino me sale None
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(cualquier_dato)
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")

def ingresar_salir(accion:str)->None:
    print(f"-----------------------{accion}-----------------------")
'''
CALCULOS REUTILIZABLES:
'''
def calcular_contador(lista: list, clave=None, valor=None)->int:
    if(type(lista) == list and len(lista) > 0 and type(clave) == str and len(clave) > 0):
        if clave is None:
            contador = 0
            for heroe in lista:
                contador += 1
        else:
            contador = 0
            for heroe in lista:
                if heroe[clave] == valor:
                    contador += 1
    return contador

def calcular_contador_raza(lista:list, clave:str)->list:
    unico = list(set([heroe[clave] for heroe in lista]))
    resultados = []
    for i in unico:
        contador = calcular_contador(lista, clave, i)
        resultados.append((i, contador))
        #print(f"Cantidad de héroes con {clave} {i}: {contador}")
        
    return resultados

'''
ACTIVIDADES RESUELTAS:
'''
#1. Traer datos desde archivo: guardará el contenido del archivo DBZ.csv en una colección. Tener en
#cuenta que tanto razas y habilidades deben estar guardadas en algún tipo de colección debido a que
#un personaje puede tener más de una raza y más de una habilidad.
def parser_csv(path:str)->list:
    '''
    -Indicar que hace: Guarda datos de archivo en una coleccion
    -Que parámetros acepta: 1 string
    -Que devuelve: 1 lista
    '''
    lista_DBZ = []
    archivo = open(path, 'r', encoding="UTF-8")
    for line in archivo:
        register = re.split(",|\n",line)
        heroeDBZ = {}
        heroeDBZ["id"] = register[0]
        heroeDBZ["nombre"] = register[1]
        heroeDBZ["raza"] = register[2]
        heroeDBZ["poder_de_pelea"] = register[3]
        heroeDBZ["poder_de_ataque"] = register[4]
        heroeDBZ["habilidades"] = register[5]
        lista_DBZ.append(heroeDBZ)
    return lista_DBZ

#2. Listar cantidad por raza: mostrará todas las razas indicando la cantidad de personajes que
#corresponden a esa raza.
def mostrar_contador_raza(lista:list, clave:str)->None:
    '''
    -Indicar que hace: Muestra la cantidad por raza
    -Que parámetros acepta: 1 lista y 1 string
    -Que devuelve: Nada
    '''
    resultados = calcular_contador_raza(lista, clave)
    for tipo, contador in resultados:
        print(f"➣ Cantidad de héroes de DBZ de raza {tipo}: {contador}")

#3. Listar personajes por raza: mostrará cada raza indicando el nombre y poder de ataque de cada
#personaje que corresponde a esa raza. Dado que hay personajes que son cruza, los mismos podrán
#repetirse en los distintos listados.
def tiene_raza(personaje:str, raza:str)->str:
    '''
    -Indicar que hace: Raza a buscar en lista de razas
    -Que parámetros acepta: 2 strings
    -Que devuelve: 1 string
    '''
    return raza in personaje['raza']
def mostrar_heroes_raza(lista:list)->None:
    '''
    -Indicar que hace: Muestra Heroes en ambos lados si poseen mas de una raza
    -Que parámetros acepta: 1 string
    -Que devuelve: Nada
    '''
    unico = list(set([heroe['raza'] for heroe in lista]))
    for i in unico:
        print(f"➣ Los heroes que tienen raza {i} son: ")
        for heroe in lista:
            if tiene_raza(heroe, i):
                print(f"  Personaje: {heroe['nombre']} - Poder: {heroe['poder_de_ataque']}")

#4. Listar personajes por habilidad: el usuario ingresa la descripción de una habilidad y el programa
#deberá mostrar nombre, raza y promedio de poder entre ataque y defensa.               
def mostrar_personajes_por_habilidad(lista:list)->None:
    '''
    -Indicar que hace: Mostrar nombre, raza y promedio segun la habilidad que ingrese
    -Que parámetros acepta: 1 lista 
    -Que devuelve: Nada
    '''
    habilidad = input("\n➣ Ingrese la habilidad deseada: ")
    personajes_con_habilidad = []
    for personaje in lista:
        habilidades = personaje['habilidades'].replace("$%","").split("|")
        if habilidad in habilidades:
            personajes_con_habilidad.append(personaje)
    
    if len(personajes_con_habilidad) == 0:
        print("No hay personajes con esa habilidad.")
    else:
        print(f"Personajes con la habilidad '{habilidad}':")
        for personaje in personajes_con_habilidad:
            ataque = float(personaje['poder_de_ataque'])
            pelea = float(personaje['poder_de_pelea'])
            promedio = (ataque + pelea) / 2
            print(f"Nombre: {personaje['nombre']}, Raza: {personaje['raza']}, Promedio de poder: {promedio}")

#5. Jugar batalla: El usuario seleccionará un personaje. La máquina selecciona otro al azar. Gana la
#batalla el personaje que más poder de ataque tenga. El personaje que gana la batalla se deberá
#guardar en un archivo de texto, incluyendo la fecha de la batalla, el nombre del personaje que ganó y
#el nombre del perdedor. Este archivo anexará cada dato.
def jugar_batalla(lista:list)->None:
    '''
    -Indicar que hace: Anexar archivo segun resultado de batalla
    -Que parámetros acepta: 1 lista
    -Que devuelve: Nada
    '''
    nombre_personaje = input("\n➣ Selecciona un personaje para jugar: ")
    personaje_usuario = None
    for personaje in lista:
        if personaje['nombre'] == nombre_personaje:
            personaje_usuario = personaje
            break
    
    if personaje_usuario is None:
        print("El personaje seleccionado no existe.")
        return
    
    personaje_maquina = random.choice(lista)
    while personaje_maquina == personaje_usuario:
        personaje_maquina = random.choice(lista)
    
    if float(personaje_usuario['poder_de_ataque']) > float(personaje_maquina['poder_de_ataque']):
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        nombre_ganador = personaje_usuario['nombre']
        nombre_perdedor = personaje_maquina['nombre']
        registro = f"Fecha y hora: {fecha}, Ganador: {nombre_ganador}, Perdedor: {nombre_perdedor}\n"
        with open("batallas.txt", "a") as file:
            file.write(registro)
        print(f"{nombre_ganador} ha ganado la batalla contra {nombre_perdedor}!")
    else:
        print(f"{personaje_maquina['nombre']} ha ganado la batalla contra {personaje_usuario['nombre']}!")

#6. Guardar Json: El usuario ingresa una raza y una habilidad. Generar un listado de los personajes que
#cumplan con los dos criterios ingresados, los mismos se guardarán en un archivo Json. Deberíamos
#guardar el nombre del personaje, el poder de ataque, y las habilidades que no fueron parte de la
#búsqueda. El nombre del archivo estará nomenclado con la descripción de la habilidad y de la raza.
#Por ejemplo: si el usuario ingresa Raza: Saiyan y Habilidad: Genki Dama
#Nombre del archivo:
#Saiyan_Genki_Dama.Json
#Datos :
#Goten - 3000 - Kamehameha + Tambor del trueno
#Goku - 5000000 - Kamehameha + Super Saiyan 2
def leer_json(nombre_archivo:str)->None:
    '''
    -Indicar que hace: Muestra los datos segun un formato especifico
    -Que parámetros acepta: 1 string
    -Que devuelve: Nada
    '''
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        datos_personajes = json.load(archivo)
    
    print("Personajes encontrados:")
    for nombre, datos in datos_personajes.items():
        poder_ataque = datos['poder_ataque']
        otras_habilidades = " + ".join(datos['otras_habilidades'])
        print(f"{nombre} - {poder_ataque} - {otras_habilidades}")
        
#7. Leer Json: permitirá mostrar un listado con los personajes guardados en el archivo Json de la opción 6.
def guardar_json(lista_personajes:list)->str:
    '''
    -Indicar que hace: Generar un listado, se guardarán en un archivo Json
    -Que parámetros acepta: 1 lista
    -Que devuelve: 1 string
    '''
    raza = input("\n➣ Ingrese la raza deseada: ")
    habilidad_eliminar = input("➣ Ingrese la habilidad deseada: ")
    
    personajes_filtrados = []
    for personaje in lista_personajes:
        if raza in personaje['raza'] and habilidad_eliminar in personaje['habilidades']:
            personajes_filtrados.append(personaje)
    datos_personajes = {}
    for personaje in personajes_filtrados:
        nombre = personaje['nombre']
        poder_ataque = personaje['poder_de_ataque']
        otras_habilidades = [habilidad.strip() for habilidad in personaje['habilidades'].replace('$%', '').split("|") if habilidad.strip() != habilidad_eliminar]
        datos_personajes[nombre] = {'poder_ataque': poder_ataque, 'otras_habilidades': otras_habilidades}
    
    nombre_archivo = f"{raza}_{habilidad_eliminar}.json"
    
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        json.dump(datos_personajes, archivo, indent=4, ensure_ascii=False )
        
    print(f"Archivo guardado con el nombre {nombre_archivo}")
    return nombre_archivo


