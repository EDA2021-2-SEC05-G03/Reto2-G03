"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
from datetime import datetime
import time

# Construccion de modelos
def newCatalog():
    catalog = {'artists': None,
               'artworks': None,
               }
    catalog["artists"] = mp.newMap(numelements = 1100, maptype="PROBING", loadfactor= 0.75 )
    catalog["artworks"] = mp.newMap(numelements = 3000, maptype="PROBING", loadfactor= 0.75 )
    catalog["Medios"] = mp.newMap(numelements = 2000, maptype="PROBING", loadfactor= 0.75 )
    catalog["Nacionalidades"] = mp.newMap(numelements = 400, maptype="PROBING", loadfactor= 0.75 )
    catalog["Obras"] = mp.newMap(numelements = 200, maptype="PROBING", loadfactor= 0.80 )
    return catalog 

# Funciones para agregar informacion a los catalogos
def addArtists(catalog,artist):
    obras = lt.newList(datastructure="ARRAY_LIST")
    artist["Obras"] = obras
    mp.put(catalog["artists"], artist["ConstituentID"], artist)
    addNationalitys(catalog,artist)
    
def fechas(catalog, artwork):
    mp.put(catalog["Obras"], artwork["Title"], artwork["Date"])

def addArtworks(catalog,artwork):
    mp.put(catalog["artworks"], artwork["ObjectID"], artwork)
    listaartistas = artwork["ConstituentID"].split(",")
    for artista in listaartistas:
        artista = artista.replace(" ", "")
        artista = artista.replace("[", "")
        artista = artista.replace("]", "")
        presente = mp.contains(catalog["artists"], artista)
        if presente:
            artistamap = mp.get(catalog["artists"],artista)["value"]
            lt.addLast(artistamap["Obras"], artwork)


    
def addMedium(catalog, artwork):  
    presente = mp.contains(catalog["Medios"], artwork["Medium"])
    if not presente:
        if artwork["Medium"] != "" and artwork["Medium"] != None:
            lista = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lista, artwork["Title"])
            mp.put(catalog["Medios"], artwork["Medium"], lista)
        else:
            None
    else:
        lista = mp.get(catalog["Medios"], artwork["Medium"])["value"]
        lt.addLast(lista, artwork["Title"])
        mp.put(catalog["Medios"], artwork["Medium"], lista)

def addNationalitys(catalog, artist):  
    presente = mp.contains(catalog["Nacionalidades"], artist["Nationality"])
    if not presente:
        lista = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lista, artist["ConstituentID"])
        mp.put(catalog["Nacionalidades"], artist["Nationality"], lista)
    else:
        lista = mp.get(catalog["Nacionalidades"], artist["Nationality"])["value"]
        lt.addLast(lista, artist["ConstituentID"])
        mp.put(catalog["Medios"], artist["Nationality"], lista)





# Funciones utilizadas para comparar elementos dentro de una lista


#Funciones de los requerimientos

def nacionalidad(catalog, nacionalidad):
    nacionalidad = mp.get(catalog["Nacionalidades"],nacionalidad)["value"]
    tamañoobras= 0
    for artista in lt.iterator(nacionalidad):
        obras = mp.get(catalog["artists"],artista)["value"]
        obras = obras["Obras"]
        tamaño = lt.size(obras)
        tamañoobras += tamaño

    return tamañoobras

def obrasantiguas(catalog, medio):
    medios = catalog["Medios"]
    m = mp.get(medios, medio)
    obras = m["value"]["elements"]
    llaves = lt.newList(datastructure="ARRAY_LIST")
    aorden = lt.newList(datastructure="ARRAY_LIST")

    for i in obras:     
        cat = catalog["Obras"]
        pareja = mp.get(cat, i)        
        fecha = pareja["value"]
        lt.addLast(llaves,i)
        lt.addLast(llaves,fecha)
        lt.addLast(aorden,fecha)

    ordenada = ms.sort(aorden, cmpfun)
    
    l = lt.newList(datastructure="ARRAY_LIST")
    for f in lt.iterator(ordenada):
        pos = lt.isPresent(llaves,f)
        pos2 = pos-1
        obras = lt.getElement(llaves, pos2)
        fecha = lt.getElement(llaves, pos)
        lt.addLast(l,obras)      
        lt.addLast(l,fecha)    
        lt.deleteElement(llaves,pos2)        
        lt.deleteElement(llaves,pos2)
        
    print(l)

def cmpfun(date1,date2):
    if date1 == "" or date1 == None:
        date1 = 0
    if date2 == "" or date2 == None:
        date2 = 0

    return int(date1) < int(date2)


