#Importación de módulos usados en el menú principal
from modelo.modelo import bienvenidaUsuario, mostrarMenu, registroGrupos, registroModulos, registroEstudiantes, registroDocentes, inicioSesion, cambioContraseña, salidaSistema, despedirUsuario, submenuRegistroAsistencia, submenuConsultasCodigo
from utils.manejoErrores import opcionMenuValida1
from persistencia.persistencia import cargar

#archivo = "opcion2\\archivo.txt"
libreria = {}
archivo1 = "modelo\data.json"
libreria = cargar(archivo1)
archivo2 = "modelo\cifrado.json"

#Programa principal
while True:
    inicioSesion()
    bienvenidaUsuario()
    mostrarMenu()
    opc = opcionMenuValida1(">> Por favor ingrese una opción del menú: ", (1, 9))
    match opc:
        case 1:
            libreria = registroGrupos(libreria)
        case 2:
            libreria = registroModulos(libreria)
        case 3:
            libreria = registroEstudiantes(libreria)
        case 4:
            libreria = registroDocentes(libreria)
        case 5:
            #submenuRegistroAsistencia(libreria, archivo1)
            pass
        case 6:
            #submenuConsultasCodigo(libreria)
            pass
        case 7:
            pass
        case 8:
            cambioContraseña()
        case 9:
            if salidaSistema() == True:
                False
                despedirUsuario()
                break
            else:
                True
        case _:
            print(" Por favor ingrese una opción válida... ")