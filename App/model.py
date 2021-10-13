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
    catalog["artists"] = mp.newMap(numelements = 2000, maptype="PROBING", loadfactor= 0.75 )
    catalog["artworks"] = mp.newMap(numelements = 2000, maptype="PROBING", loadfactor= 0.75 )
    catalog["Medios"] = mp.newMap(numelements = 2000, maptype="PROBING", loadfactor= 0.75 )
    catalog["Nacionalidades"] = mp.newMap(numelements = 2000, maptype="PROBING", loadfactor= 0.75 )
    return catalog 

# Funciones para agregar informacion a los catalogos
def addArtists(catalog,artist):
    mp.put(catalog["artists"], artist["ConstituentID"], artist)

def addArtworks(catalog,artwork):
    mp.put(catalog["artists"], artwork["ObjectID"], artwork)

    
def addMeduim(catalog, artwork):  
    presente = mp.contains(catalog["Medios"], artwork["Medium"])
    if not presente:
        lista = lt.newList()
        lt.addLast(lista, artwork["Title"])
        mp.put(catalog["Medios"], artwork["Medium"], lista)
    else:
        lista = mp.get(catalog["Medios"], artwork["Medium"])["value"]
        lt.addLast(lista, artwork["Title"])
        mp.put(catalog["Medios"], artwork["Medium"], lista)



# Funciones utilizadas para comparar elementos dentro de una lista


#Funciones de los requerimientos

