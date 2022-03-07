# Gonzalo Peña Calero 1ºASIR

from funcionesJSON import *

marvel=leer_json("marvel.json")

menu='''
1. Listar personajes
2. Contar historias
3. Pedir personaje y mostrar comics
4. Pedir evento y y mostrar personaje
5. Pedir comic y ver si lo hay en algún personaje
0. Salir'''

print(menu)
opcion=int(input("Seleccione opción [0-5]: "))
while opcion != 0:
    if opcion == 1:
        personajes = listar_personajes(marvel)
        for personaje in zip (personajes):
            print (personaje[0])
        

    elif opcion == 2:
        contar = contar_historias(marvel)
        if contar > 0:
            print ("Existen un total de", contar,"personajes.")
    

    elif opcion == 3:
        nombre = input("¿Qué personaje desea buscar?: ")
        personaje,comics = mostrar_comics(personajes,comics,marvel,nombre)
        if len(personaje) ==0:
            print("El personaje introducido no se encuentra.")
        else:
            personaje,comics in zip (personaje,comics)
            print ("Nombre del personaje: ", personaje)
            print ("Comics: ")
            print(comics)
   
    elif opcion == 4:
        evento = input("¿Qué evento desea buscar?: ")
        eventos = mostrar_personajes(evento,marvel)
        if len(personaje) ==0:
            print("El evento introducido no se encuentra.")
        else:
            eventos in zip (evento,marvel)
            print (eventos)
    
    else:
        print ("Opción no válida. Introdúzcala de nuevo.")
    print(menu)
    opcion=int(input("Seleccione opción [0-5]: "))
print("Adios.")
        