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


from DISClib.DataStructures.arraylist import newList
from DISClib.DataStructures.chaininghashtable import keySet
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
from datetime import date, datetime
import time

# Construccion de modelos
def newCatalog():
    catalog = {'artists': None,
               'artworks': None,
               }
    catalog["artists"] = mp.newMap(numelements = 1100, maptype="PROBING", loadfactor= 0.75 ) #ID-InfoArtists
    catalog["artworks"] = mp.newMap(numelements = 3000, maptype="PROBING", loadfactor= 0.75 ) 
    catalog["aw"] = mp.newMap(numelements = 3000, maptype="PROBING", loadfactor= 0.75 ) #ID-InfoArtworks
    catalog["Medios"] = mp.newMap(numelements = 2000, maptype="PROBING", loadfactor= 0.75 ) #Medio-TitleObras
    catalog["Nacionalidades"] = mp.newMap(numelements = 400, maptype="PROBING", loadfactor= 0.75 ) # Nat-IDs
    catalog["Obras"] = mp.newMap(numelements = 200, maptype="PROBING", loadfactor= 0.80 ) #TitleObra-Fecha
    catalog["NacimientoArtistas"] = mp.newMap(numelements=1667, maptype="PROBING", loadfactor= 0.5) #BeginDate-InfoArtistas
    catalog["DateAcquired"] = mp.newMap(numelements= 191, maptype="PROBING", loadfactor= 0.5) #DateAquired-InfoArtistas
    catalog["Medartist"]= mp.newMap(numelements=1667, maptype="PROBING", loadfactor= 0.5) #ID-Medios
    catalog["ids"] = mp.newMap(numelements=2000, maptype="PROBING", loadfactor= 0.5) #Name_ID
    catalog["Nat"] = mp.newMap(numelements=2000, maptype="PROBING", loadfactor= 0.5) #ID-Nat
    catalog["ID"] = lt.newList(datastructure="ARRAY_LIST") #Todos los ids de artworks
    catalog["ArtNat"] = mp.newMap(numelements=400, maptype="PROBING", loadfactor= 0.5) #Nat-IDs
    catalog["N"] = mp.newMap(numelements=400, maptype="PROBING", loadfactor= 0.5)
    return catalog 

# Funciones para agregar informacion a los catalogos
def addArtists(catalog,artist):
    obras = lt.newList(datastructure="ARRAY_LIST")
    artist["Obras"] = obras
    mp.put(catalog["artists"], artist["ConstituentID"], artist)
    addNationalitys(catalog,artist)
    addBeginDate(catalog,artist)
    
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

def a(catalog, artwork):   
    listaartistas = artwork["ConstituentID"].strip("[]")  
    listaartistas = listaartistas.replace(" ","")
    listaartistas = listaartistas.split(",")
    
    for artista in listaartistas:     
        presente = mp.contains(catalog["aw"], int(artista))
        if presente:
            l = mp.get(catalog["aw"],int(artista))["value"]
            lt.addLast(l, artwork)
            mp.put(catalog["aw"],int(artista),l)
        else:
            l = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(l, artwork)
            mp.put(catalog["aw"], int(artista),l)
  

      
  
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
        mp.put(catalog["Nacionalidades"], artist["Nationality"], lista)



def n(catalog, artwork):      
    presente = mp.contains(catalog["N"], artwork["Nationality"])
    if presente:
        l = mp.get(catalog["N"], artwork["Nationality"])["value"]
        lt.addLast(l, artwork)
        mp.put(catalog["N"],artwork["Nationality"],l)
    else:
        l = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(l, artwork)
        mp.put(catalog["N"], artwork["Nationality"],l)

def printNats(catalog, Nat):
    ids = mp.get(catalog["ArtNat"],Nat)["value"]
    
    for i in range(0,2):
        obras = mp.get(catalog["aw"],ids["elements"][i])["value"]
        for i in lt.iterator(obras):
            
            print("|"+i["Title"].center(105)+" | "+ i["Date"].center(13)+" | "+i["Medium"].center(15)+" | "+" | ")
            print("+"+("-"*217)+"+")
            




def addBeginDate(catalog,artist):
    presente = mp.contains(catalog["NacimientoArtistas"], int(artist["BeginDate"]))
    if not presente:
        lista = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lista,artist)
        mp.put(catalog["NacimientoArtistas"], int(artist["BeginDate"]),lista)
    else: 
        lista = mp.get(catalog["NacimientoArtistas"], int(artist["BeginDate"]))["value"]
        lt.addLast(lista,artist)
        mp.put(catalog["NacimientoArtistas"],int(artist["BeginDate"]),lista)

def addDateAcquired(catalog, artwork):  
    if artwork["DateAcquired"] == "":
        artwork["DateAcquired"] = "0000"
    presente = mp.contains(catalog["DateAcquired"], artwork["DateAcquired"][0:4])
    if not presente:
            lista = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lista, artwork)
            mp.put(catalog["DateAcquired"], artwork["DateAcquired"][0:4], lista)
    else:
            lista = mp.get(catalog["DateAcquired"], artwork["DateAcquired"][0:4])["value"]
            lt.addLast(lista, artwork)
            mp.put(catalog["DateAcquired"], artwork["DateAcquired"][0:4],lista)

def ids(catalog, artist):
    mp.put(catalog["ids"], artist["DisplayName"], int(artist["ConstituentID"]))

def mediumartists(catalog, artworks):
    ids = artworks["ConstituentID"].strip("[]")
    ids = ids.split(",")
    for i in ids:
        i = i.strip()
        presente = mp.contains(catalog["Medartist"], int(i))
        if not presente:
            lista = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(lista, artworks["Medium"])
            mp.put(catalog["Medartist"], int(i),lista)
        else:
            lista = mp.get(catalog["Medartist"], int(i))["value"]
            lt.addLast(lista,artworks["Medium"])
            mp.put(catalog["Medartist"], int(i), lista)

def Nat(catalog, artist):
    n = artist["Nationality"]
    if n == "" or n == None:
        n = "Nationality unknown"
        mp.put(catalog["Nat"], int(artist["ConstituentID"]), n)
    else:
        mp.put(catalog["Nat"], int(artist["ConstituentID"]), n)

def NatArt(catalog, artworks):
    lista = catalog["ID"]
    ids = artworks["ConstituentID"].strip("[]")
    ids = ids.split(",")   
    for i in ids:
        id = i.strip()
        lt.addLast(lista, int(i))
    

def requerimiento4(catalog):
    lista = catalog["ID"]
    nat = catalog["Nat"]
    for i in lt.iterator(lista):
        n = mp.get(nat, i)["value"]
        presente = mp.contains(catalog["ArtNat"], n)
        if not presente:
            lista = lt.newList(datastructure="ARRAY_LIST")          
            lt.addLast(lista, i)
            mp.put(catalog["ArtNat"], n,lista)
        else:
            lista = mp.get(catalog["ArtNat"], n)["value"]
            lt.addLast(lista,i)
            mp.put(catalog["ArtNat"], n, lista)    
    valores = mp.valueSet(catalog["ArtNat"])
    sizes = lt.newList("ARRAY_LIST")

    for i in lt.iterator(valores):
        size = i["size"]       
        lt.addLast(sizes,size)
    
    orden = ms.sort(sizes, cmpfunctionrequerimiento3)
    llaves = mp.keySet(catalog["ArtNat"])
    s = lt.size(orden)  
    s = lt.size(orden)
    ret = lt.newList(datastructure="ARRAY_LIST")
    num = 0  
    while num < s:
        for i in lt.iterator(llaves):
            g = orden["elements"][num]                     
            f = mp.get(catalog["ArtNat"],i)["value"]            
            f = lt.size(f)
            k = mp.get(catalog["ArtNat"],i)["key"]
            
            if f == g:               
                lt.addLast(ret, k)
                lt.addLast(ret, f)                       
        num += 1
    return ret


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpfunctionrequerimiento1(date1,date2):
    date1 = int(date1["BeginDate"])
    date2 = int(date2["BeginDate"])
    return date1 < date2

def cmpfunctionrequerimiento2(date1,date2):
    date1 = datetime.strptime(date1["DateAcquired"], "%Y-%m-%d")
    date2 = datetime.strptime(date2["DateAcquired"], "%Y-%m-%d")
    return date1 < date2

def cmpfunctionrequerimiento3(med1,med2):
    return med1 > med2

#Funciones de los requerimientos

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

def requerimiento1(catalog, begin1, begin2):
    listaartistas= lt.newList(datastructure="ARRAY_LIST")
    for año in range(begin1,(begin2+1)):
        listaartistasmp=mp.get(catalog["NacimientoArtistas"], año)["value"]
        for agregar in lt.iterator(listaartistasmp):
            lt.addLast(listaartistas,agregar)
    numerototaldeartistas = lt.size(listaartistas)
    listaartistas = ms.sort(listaartistas,cmpfunctionrequerimiento1)
    sublista1 = lt.subList(listaartistas,1,3)
    sublista2 = lt.subList(listaartistas,(numerototaldeartistas-2),3)
    listarespuesta3y3 = lt.newList(datastructure="ARRAY_LIST")
    for artista in lt.iterator(sublista1):
        lt.addLast(listarespuesta3y3,artista)
    for artista in lt.iterator(sublista2):
        lt.addLast(listarespuesta3y3,artista)
    return (numerototaldeartistas,listarespuesta3y3)

def requerimiento2(catalog,begin,end):
    beginyear = int(begin[0:4])
    endyear= int(end[0:4])
    begin = datetime.strptime(begin,"%Y-%m-%d")
    end = datetime.strptime(end,"%Y-%m-%d")
    listaobras = lt.newList(datastructure="ARRAY_LIST")
    purchase = 0
    for year in range(beginyear,endyear+1):
        year = str(year)
        presente = mp.contains(catalog["DateAcquired"],year)
        if presente:
            year= mp.get(catalog["DateAcquired"], year)["value"]
            for obra in lt.iterator(year):
                if datetime.strptime(obra["DateAcquired"], "%Y-%m-%d") >= begin and datetime.strptime(obra["DateAcquired"], "%Y-%m-%d") <= end:
                    lt.addLast(listaobras,obra)
                    acomparar = obra["CreditLine"].lower()
                    acomparar = acomparar.find("purchase")
                    if acomparar != -1:
                        purchase += 1
    totalobras = lt.size(listaobras)
    listaobras = ms.sort(listaobras,cmpfunctionrequerimiento2)
    sublista1 = lt.subList(listaobras,1,3)
    sublista2 = lt.subList(listaobras,(totalobras-2),3)
    listarespuesta3y3 = lt.newList(datastructure="ARRAY_LIST")
    for artista in lt.iterator(sublista1):
        lt.addLast(listarespuesta3y3,artista)
    for artista in lt.iterator(sublista2):
        lt.addLast(listarespuesta3y3,artista)
    return (totalobras,purchase,listarespuesta3y3)

def requerimiento3(catalog,artist):
    id = mp.get(catalog["ids"], artist)["value"]   
    meds = mp.get(catalog["Medartist"], id)["value"]
    return(id,meds)
   
def topMeds(medios):
    map = mp.newMap(numelements=50, maptype="PROBING", loadfactor= 0.5)
    for i in lt.iterator(medios):
        presente = mp.contains(map, i)
        if not presente:
            count = 1
            mp.put(map, i,count)
        else:
            count = mp.get(map, i)["value"]
            count += 1
            mp.put(map, i,count)
    return map

def orden(map):
    llaves = mp.keySet(map)
    valores = mp.valueSet(map)
    lista = lt.newList(datastructure="ARRAY_LIST")
    size = mp.size(llaves)
    sub = lt.subList(valores, 0, size)
    orden = ms.sort(sub,cmpfunctionrequerimiento3)
    for i in lt.iterator(orden):
        
        pos = lt.isPresent(valores, i)
        key = lt.getElement(llaves,pos)
        lt.addLast(lista, key)
        lt.addLast(lista, i)

        lt.deleteElement(valores, pos)
        lt.deleteElement(llaves, pos)
    return (size, lista) 

#artwork["DateAcquired"] = datetime.strptime(artwork["DateAcquired"], "%Y-%m-%d")

def printArtMed(catalog, id, med):
    obras = mp.get(catalog["aw"],id)["value"]
    print(" ")
    print("+"+("-"*217)+"+")
    print("|" + "Title".center(105)+" | "+ "Date".center(13)+" | "+"Medium".center(15)+" | "+"Dimensions".center(74)+" | ")
    print("+"+("-"*217)+"+")
    for i in lt.iterator(obras):
        if i["Medium"] == med:
           
            print("|"+i["Title"].center(105)+" | "+ i["Date"].center(13)+" | "+i["Medium"].center(15)+" | "+i["Dimensions"].center(74)+" | ")
            print("+"+("-"*217)+"+")
    
