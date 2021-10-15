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
    print ("2. Requerimiento 2: Listar cronológicamente los artistas.")
    print ("0. Salir")

#Iniciador de catalogos y carga de datos
def initCatalog():
    return controller.initCatalog()
def loadData(catalog):
    controller.loadData(catalog)


#Funciones de imprimir: listas y cmpfunction de estas

#Menú Principal
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        t1 = process_time()
        catalog = initCatalog()
        loadData(catalog)
        t2 = process_time()
        time = t2-t1
        print("El tiempo para cargar los archivos fue de:", str(time) , "s")    

    elif int(inputs[0]) == 2: 
        begin1 = int(input("Digite el año de nacimiento inicial: "))
        begin2 = int(input("Digite el año de nacimiento final: "))
        respuestas = controller.requerimiento2(catalog, begin1, begin2)
        print("El número total de artistas que nacieron en ese rango de fechas fue de " + str(respuestas[0]))
        for i in lt.iterator(respuestas[1]):
            print(i["DisplayName"])

        
    else:
        sys.exit(0)
sys.exit(0)