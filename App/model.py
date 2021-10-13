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
def newCatalog(tipolista: str):
    catalog = {'artists': None,
               'artworks': None,
               }
    catalog["artists"] = lt.newList(tipolista,cmpfunction= compareartists)
    catalog["artworks"] = mp.newMap(numelements = 10000, maptype="CHAINING", loadfactor= 4.0, comparefunction= comparemedium )
    return catalog 

# Funciones para agregar informacion al catalogo
def addArtwork(catalog, artwork):  
    mp.put(catalog["artworks"], artwork["Medium"], artwork)
def addArtists(catalog,artist):
    lt.addLast(catalog["artists"], artist)

# Funciones utilizadas para comparar elementos dentro de una lista
def comparemedium(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if id == identry:
        return 0
    elif id > identry:
        return 1
    else:
        return -1
        
def compareartists(artistname1, artist):
    if (artistname1.lower() in artist['ConstituentID'].lower()):
        return 0
    return 1

#Funciones de los requerimientos

def nmasantiguas(catalog, medio):
    x= mp.get(catalog["artworks"], medio)
    x = me.getValue(x)
    print (x)
    x = ms.sort(x,cmpfunctionantiguedad)
    return x
