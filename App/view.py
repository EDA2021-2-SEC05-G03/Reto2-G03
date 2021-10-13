"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from time import process_time
assert cf
import sys as sis
from datetime import datetime
from DISClib.ADT import map as mp

default_limit = 1000
sys.setrecursionlimit(default_limit*10)
catalog = None

#Imprimir el Menú
def printMenu():
    print ("Bienvenido")
    print ("1. Cargar archivos.")
    print ("2. Ordenar por orden de adquisición de las obras")
    print ("3. REQ. 1: Listar cronológicamente los artistas")
    print ("4. REQ. 2: Listar cronológicamente las adquisiciones.")
    print ("5. REQ. 3: Clasificar las obras de un artista por técnica")
    print ("6. REQ. 4: Clasificar las obras por la nacionalidad de sus creadores.")
    print ("7. REQ. 5: Costo de transportar las obras de un departamento a otro")
    print ("8. Las N obras mas antiguas de un medio específico")
    print ("0. Salir")

#Iniciador de catalogos y carga de datos
def initCatalog(tipolista: str):
    return controller.initCatalog(tipolista)
def loadData(catalog):
    controller.loadData(catalog)


#Funciones de imprimir: listas y cmpfunction de estas

#Menú Principal
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print ("Escoja el tipo de lista que quiere utilizar: ")
        print ("1. Array List.\n2. Single Linked")
        num = int(input("Digite el número de estructura de la lista escogido: "))
        if num == 1:
            tipolista = "ARRAY_LIST"
        else:
            tipolista = "SINGLE_LINKED"
        print("Cargando información de los archivos ....")
        t1 = process_time()
        catalog = initCatalog(tipolista)
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks']))) 
        t2 = process_time()
        time = t2-t1
        print("El tiempo para cargar los archivos fue de:", str(time) , "s")     

        
    elif int(inputs[0]) == 8:
        medio = input("Digite el medio a evaluar: ")
        controller.nmasantiguas(catalog, medio)
    else:
        sys.exit(0)
sys.exit(0)