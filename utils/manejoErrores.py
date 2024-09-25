#Funciones
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("modelo\\modelo.py"), '..')))

def opcionMenuValida1(mensaje, rango):
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion < rango[0] or opcion > rango[1]:
                print(" Error. Opción no válida. ")
                input(">> Presione cualquier tecla para volver al menú... ")
                continue
            return opcion
        except ValueError:
                print(" Error. Opción no válida. ")
                input(">> Presione cualquier tecla para volver al menú... ")
                
def leerEnteroPositivo(msg):
    while True:
        try:
            num = int(input(msg))
            if num <= 0:
                print(" Error. Por favor ingrese un número postivo.\n")
            else:
                return num
        except ValueError:
            print(" Error. Sólo se permiten números enteros. Inténtelo de nuevo por favor..\n")

def leerString(msg):
    while True:
        str = input(msg)
        if str.isalpha() and str.strip():
            return str
        else:
            print(">> Error. Sólo se permiten caracteres. Inténtelo de nuevo por favor. ")
                
def leerGenero(msg):
    from modelo.modelo import esperarTiempo
    while True:
        genero = input(msg)        
        try:
            if genero in ['M', 'm', 'F', 'f']:
                return genero
            else:
                print("Por favor ingrese un sexo válido ")
                esperarTiempo(30_000)
                continue
        except ValueError:
            print(" Error. Sólo se permiten caracteres. Inténtelo de nuevo por favor..\n")

