# Gonzalo Peña Calero 1ºASIR

import json

#Leer fichero JSON
def leer_json(fichero):
    try:
        with open(fichero) as f: 
            marvel=json.load(f)
        return marvel
    except:
        print("No se puede leer el fichero")


def listar_personajes(marvel):
    lista=[]
    for marvel in marvel:
        lista.append(marvel.get("name"))
    return (set(lista))

def contar_historias(marvel):
    historias=[]
    for personaje in marvel:
        for historia in personaje(marvel.get("name")):
            historias.append(historia["stories"].get["name"])
    return len(historias)

def mostrar_comics(personajes,comics,nombre,marvel):
    personaje=[]
    comics = []
    for personajes in marvel:
        if personajes["name"] == nombre:
            for comic in personajes.get("comics"):
                personaje.append(personajes.get("name"))
                comics.append(comic("items").get("name"))
    return personaje,(set(comics))

def mostrar_personajes(evento,marvel,nombre):
    lista=[]
    for events in marvel:
        if evento.get("events") == nombre:
            return events in evento.get("name")
    return lista

def mostrar_personajes_2(comics,marvel,nombre):
    lista=[]
    for comics in marvel:
        if comics.get("comics") == nombre:
           return comics in comics.get("name").items()
    return lista
