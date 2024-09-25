import pprint
import json
import os
from pathlib import Path

#Guardar algo y pasarselo al json, luego cerrarlo
def guardar(lib, arch):
    with open(arch, "w") as fd:
        json.dump(lib, fd)#json Dump se usa para guardar algo en un JSON

    if not fd.closed:
        fd.close()

#Función para cargar algo de un archivo y cerrarlo
def cargar(arch):
    archivo = Path(arch)
    lib = {}
    if archivo.is_file(): # True: si existe y es un archivo
        try:
            with open(arch, "r") as fd:
                lib = json.load(fd)

            if not fd.closed:
                fd.close()
        except Exception as e:
            print(">>> Error al abrir el archivo.\n" + str(e))
    else:
        print(">>> Error. El archivo no existe.")
        input(">>> Presione cualquier tecla para continuar...")

    return lib
