import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("persistencia\persistencia.py"), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("modelo\modelo.py"), '..')))

from datetime import datetime, timedelta
from persistencia.persistencia import guardar, cargar

#Registro de asistencia
def registroAsistenciaLlegada(libreria, arch):
    from modelo.modelo import leerCodEst, leerCodModulo
    archivo = "modelo\data.json"
    libreria = cargar(archivo)

    codMod = leerCodModulo()
    if codMod in libreria["modulos"]:
        cod = leerCodEst()
        if cod in libreria["modulos"][codMod]["estudiantes"]:

            if "asistencia" not in libreria["modulos"][codMod]:
                libreria["modulos"][codMod]["asistencia"] = {}

            fecha = leerFecha()

            if fecha not in libreria["modulos"][codMod]["asistencia"]:
                libreria["modulos"][codMod]["asistencia"][fecha] = {}

            if cod in libreria["modulos"][codMod]["asistencia"][fecha]:
                print(" Ya se ha registrado la asistencia el día de hoy. ")
                input(" Presione cualquier tecla para volver al menú. ")
                return libreria
            
            horaEntrada = leerHora()

            libreria["modulos"][codMod]["asistencia"][fecha][cod] = {}
            libreria["modulos"][codMod]["asistencia"][fecha][cod]["Hora de llegada"] = horaEntrada

            guardar(libreria, archivo)

            print(" Asistencia registrada ")
        else:
            print(f" El estudiante {cod} no está inscrito en el módulo {codMod}. ")
    else:
        print(f" El módulo {codMod} no está inscrito en la base de datos. ")

    input(" Pulse cualquier tecla para volver al menú... ")
    return libreria

def registroAsistenciaSalida(libreria, arch):
    from modelo.modelo import leerCodEst, leerCodModulo
    archivo = "modelo\data.json"
    libreria = cargar(archivo)

    codMod = leerCodModulo()
    if codMod in libreria["modulos"]:
        cod = leerCodEst()
        if cod in libreria["modulos"][codMod]["Asistencia"]["estudiantes"]:
            if "asistencia" not in libreria["modulos"][codMod]:
                libreria["modulos"][codMod]["asistencia"] = {}

            fecha = leerFecha()

            if fecha not in libreria["modulos"][codMod]["asistencia"]:
                print(f" No se ha registrado asistenci para el estudiante {cod} en la fecha {fecha}. ")
                input(" Presione cualquier tecla para volver al menú. ")
                return libreria
            
            if cod not in libreria["modulos"][codMod]["asistencia"][fecha]:
                print(" No se ha registrado la hora de llegada para hoy. ")
                input(" Presione cualquier tecla para volver al menú. ")
                return libreria
            
            if "Hora de salida" in libreria["modulos"][codMod]["asistencia"][fecha][cod]:
                print(" Ya se ha registrado la hora de salida para hoy. ")
                input(" Presione cualquier tecla para volver al menú. ")
                return libreria
            
            horaSalida = leerHora()

            libreria["modulos"][codMod]["asistencia"][fecha][cod]["Hora de salida"] = horaSalida

            guardar(libreria, archivo)

            print(f"Hora de salida registrada asignada al {cod} en el modulo {codMod}. ")
        else:
            print(f"El código {cod} no está incrito en el módulo {codMod}")
    else:
        print(f"El código {codMod} no está incrito en la base de datos. ")

    input(" Presione cualquier tecla para volver al menú. ")
    return libreria

def leerFecha():
    fecha = datetime.now()
    return fecha.strftime("%Y-%m-%d %H:%M:%S")

def leerHora():
    hora_actual = datetime.now()
    return hora_actual.strftime("%H:%M:%S")

