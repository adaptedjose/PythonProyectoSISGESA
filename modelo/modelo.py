#Funciones
import sys
import os
import hashlib
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("utils\\manejoErrores.py"), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("persistencia\persistencia.py"), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("utils\asistencia.py"), '..')))
from utils.manejoErrores import opcionMenuValida1, leerEnteroPositivo, leerString, leerGenero
from utils.asistencia import registroAsistenciaLlegada, registroAsistenciaSalida
from persistencia.persistencia import guardar, cargar

#Despedir usuario
def despedirUsuario():
    print("-" * 30)
    print("-" * 30)
    print(" Gracias por usar el sistema SISGESA ")
    print("-" * 30)
    print(" Cerrando sesión ")
    print("-" * 30)
    print("-" * 30)
    esperarTiempo(50_000)

#Salir del sistema
def salidaSistema():
    salida = leerEnteroPositivo(" >> Para salir del sistema ingrese 1, ingrese 2 para volver al menú principal de SISGESA: ")
    if salida == 1:
        return True
    elif salida == 2:
        return False
    else:
        print(" Por favor ingrese una opción válida... ")

#Inicio sesión
def inicioSesion():
    bienvenidaUsuario()
    while True:
        with open("modelo\cifrado.json") as f:
            datos = json.load(f)
            credencialesAcceso = {}
            credencialesAcceso["usuario"] = leerString("Por favor ingrese su usuario: ")
            credencialesAcceso["contra"] = leerString("Por favor ingrese su contraseña: ")
            datos["contrasena2"] = credencialesAcceso["contra"]
            guardar(datos, "modelo\cifrado.json")
            False

        cifrarContrasenas() #Terminado

        if comparacionContra() == True:
            break

#Cifrar contraseña
def cifrarContrasenas():
    while True: 
        with open("modelo\cifrado.json") as f:
            datos = json.load(f)
            contra1 = datos["contrasena1"] #Contraseña estándar
            hashv1 = contra1
            sha256_obj = hashlib.sha256()
            sha256_obj.update(hashv1.encode("utf-8")) 
            hashv1_hexdigest = str(sha256_obj.hexdigest())
            datos["contrasena1cifrada"] = hashv1_hexdigest
            contra2 = datos["contrasena2"] #Contraseña ingresada por el usuario
            hashv2 = contra2
            sha256_obj2 = hashlib.sha256()
            sha256_obj2.update(hashv2.encode("utf-8")) 
            hashv2_hexdigest = str(sha256_obj2.hexdigest())
            datos["contrasena2cifrada"] = hashv2_hexdigest
            guardar(datos, "modelo\cifrado.json")
            False
            break

#Cambio de contraseña 
def cambioContraseña():
    with open("modelo\cifrado.json") as f:
            datos = json.load(f)
            contraseñaInicial = datos["contrasena1"]
            cambioContraInicial = leerString(" Por favor ingrese su nueva contraseña: ")
            datos["contrasena1"] = cambioContraInicial
            guardar(datos, "modelo\cifrado.json")
            return print(" La contraseña ha sido modificada ")

#Comparación de contraseña
def comparacionContra():
    with open("modelo\cifrado.json") as f:
        datos = json.load(f)
        contra1cifrada = datos["contrasena1cifrada"]
        contra2cifrada = datos["contrasena2cifrada"]
        if contra1cifrada == contra2cifrada:
            print("-" * 30)
            print(" Contraseña correcta ")
            print("-" * 30)
            return True
        else:
            print("-" * 30)
            print(" Contraseña incorrecta ")
            print("-" * 30)
            return False

#Bienvenida usuario
def bienvenidaUsuario():
    print(" BIENVENIDO AL SISTEMA 'SISGESA' ")
    print("-" * 30)

#Esperar tiempo
def esperarTiempo(segundos):
    for s in range(segundos * 1000):
        pass

#Mostrar menú
def mostrarMenu():
        print(">> Por favor elija una opción del menú: ", end="\n")
        print("-" * 30)
        print(" 1. Registro de grupos")
        print(" 2. Registro de módulos")
        print(" 3. Registro de estudiantes")
        print(" 4. Registro de docentes")
        print(" 5. Registro de asistencia")
        print("-" * 30)
        print(" 6. Consultas de información")
        print(" 7. Generación de informes")
        print("-" * 30)
        print(" 8. Cambio de contraseña")
        print("-" * 30)
        print(" 9. Salida del sistema")
        print("-" * 30)
        
#Registro de grupos
def registroGrupos(libreria):
    if "grupos" not in libreria:
        libreria["grupos"] = {}
    grupos = libreria["grupos"]
    print("-" * 30)
    print(" BIENVENIDO AL REGISTRO DE GRUPOS. ")
    while True:
        submenuRegistroGrupos()
        opcMenu = opcionMenuValida1(">> Por favor elija una opción del menú: \n", (1, 3))
        match opcMenu:
            case 1:
                codigosGrupo = leerEnteroPositivo("Por favor ingrese el CÓDIGO del grupo: ")
                if "codigoGrupo" not in grupos:
                    nombresGrupo = leerString(" Por favor ingrese el NOMBRE del grupo :")
                    siglasGrupo = leerString(" Por favor ingrese la SIGLA del grupo :")

                    grupo = {
                        "codigoGrupo" : codigosGrupo,
                        "nombreGrupo" : nombresGrupo,
                        "siglasGrupo" : siglasGrupo
                    }

                    grupos[codigosGrupo] = grupo
                    
                    guardar(libreria, "modelo\data.json")
                    True
            case 2:
                print(" 2. Visualización de grupos registrados ")
                verGrupos = grupo["codigoGrupo"]
                print("Los grupos registrados hasta el momento son: ", int(len(verGrupos)))
                submenuRegistroGrupos()
                True
            case 3:
                print(" Volviendo al menú principal de 'SISGESA'... ")
                esperarTiempo(50_000)
                False
                break
                
#Submenú función registroGrupos       
def submenuRegistroGrupos():
    print("-" * 30)
    print("-" * 30)
    print(" OPCIONES DEL REGISTRO DE GRUPOS")
    print("-" * 30)
    print(" 1. Registro de grupo ")
    print("-" * 30)
    print(" 2. Visualización de grupos registrados ")
    print("-" * 30)
    print(" 3. Volver al menú principal de 'SISGESA' ")
    print("-" * 30)
    print("-" * 30)            
            
#Registro módulos
def registroModulos(libreria):
    if "modulos" not in libreria:
        libreria["modulos"] = {}
    modulos = libreria["modulos"]
    print("-" * 30)
    print(" BIENVENIDO A LA OPCIÓN DE REGISTRO Y MANEJO DE MÓDULOS. ")
    while True:
        submenuRegistroModulos()
        opcMenu = opcionMenuValida1(">> Por favor elija una opción del menú: \n", (1, 3))
        match opcMenu:
            case 1:
                codigosModulo = leerEnteroPositivo(" Por favor ingrese el CÓDIGO del módulo: ")
                if "codigoModulo" not in modulos:
                    nombreModulo = leerString(" Por favor ingrese el NOMBRE del módulo :")
                    duracionModulo = leerEnteroPositivo(" Por favor ingrese la DURACIÓN del módulo (En semanas): ")

                    modulo = {
                        "codigosModulo" : codigosModulo,
                        "nombresModulo" : nombreModulo,
                        "duracionModulo" : duracionModulo
                    }

                    modulos[codigosModulo] = modulo

                    guardar(libreria, "modelo\data.json")
                    True
            case 2:
                print(" 2. Visualización de módulos registrados ")
                verModulos = modulos["codigosModulo"]
                print("Los módulos registrados hasta el momento son: ", int(len(verModulos)))
                submenuRegistroModulos()
                True
            case 3:
                print(" Volviendo al menú principal de 'SISGESA'... ")
                esperarTiempo(50_000)
                False
                break
            
#Submenú de la función registroModulos               
def submenuRegistroModulos():
    print("-" * 30)
    print("-" * 30)
    print(" OPCIONES DEL REGISTRO Y MANEJO DE MÓDULOS.")
    print("-" * 30)
    print(" 1. Registro de módulo ")
    print("-" * 30)
    print(" 2. Visualización de módulos registrados ")
    print("-" * 30)
    print(" 3. Volver al menú principal de 'SISGESA' ")
    print("-" * 30)
    print("-" * 30)
    
#Registro de estudiantes
def registroEstudiantes(libreria):
    if "estudiantes" not in libreria:
        libreria["estudiantes"] = {}
    estudiantes = libreria["estudiantes"]
    print("-" * 30)
    print(" BIENVENIDO A LA OPCIÓN DE REGISTRO DE ESTUDIANTES. ")
    while True:
        submenuRegistroEstudiantes()
        opcMenu = opcionMenuValida1(">> Por favor elija una opción del menú: \n", (1, 3))
        match opcMenu:
            case 1:
                codigosEstudiantes = leerEnteroPositivo(" Por favor ingrese el CÓDIGO del estudiante: ")
                if "codigoEstudiantes" not in estudiantes:
                    nombresEstudiantes = leerString(" Por favor ingrese el NOMBRE del estudiante :")
                    sexosEstudiantes = leerGenero("Por favor ingrese el SEXO del estudiante (M o F): ")
                    edadesEstudiantes = leerEnteroPositivo(" Por favor ingrese la EDAD del estudiante: ")
                    
                    estudiante = {
                        "codigosEstudiantes" : codigosEstudiantes,
                        "nombresEstudiantes" : nombresEstudiantes,
                        "sexosEstudiantes" : sexosEstudiantes,
                        "edadesEstudiantes" : edadesEstudiantes
                    }

                    estudiantes[codigosEstudiantes] = estudiante
                    
                    guardar(libreria, "modelo\data.json")
                    True
            case 2:
                print(" 2. Visualización de estudiantes registrados ")
                verEstudiantes = estudiantes["codigoEstudiantes"]
                print("Los estudiantes registrados hasta el momento son: ", int(len(verEstudiantes)))
                submenuRegistroEstudiantes()
                True
            case 3:
                print(" Volviendo al menú principal de 'SISGESA'... ")
                esperarTiempo(50_000)
                False
                break
        
#Submenu de la función registroEstudiantes             
def submenuRegistroEstudiantes():
    print("-" * 30)
    print("-" * 30)
    print(" OPCIONES ")
    print("-" * 30)
    print(" 1. Registro de estudiantes ")
    print("-" * 30)
    print(" 2. Visualización de estudiantes registrados ")
    print("-" * 30)
    print(" 3. Volver al menú principal de 'SISGESA' ")
    print("-" * 30)
    print("-" * 30)
    
#Registro de docentes
def registroDocentes(libreria):
    if "docentes" not in libreria:
        libreria["docentes"] = {}
    docentes = libreria["docentes"]
    print("-" * 30)
    print(" BIENVENIDO A LA OPCIÓN DE REGISTRO DE DOCENTES. ")
    while True:
        submenuRegistroDocentes()
        opcMenu = opcionMenuValida1(">> Por favor elija una opción del menú: \n", (1, 3))
        match opcMenu:
            case 1:
                cedulasDocentes = leerEnteroPositivo(" Por favor ingrese la cédula del docente: ")
                if "cedulaDocentes" not in docentes:
                    nombresDocentes = leerString(" Por favor ingrese el NOMBRE del docente:")
                    modulosDocentes = leerString(" Por favor ingrese los módulos del docente: ")
            
                    docente = {
                        "cedulaDocentes" : cedulasDocentes, 
                        "nombresDocentes" : nombresDocentes,
                        "modulosDocentes" : modulosDocentes
                    }

                    docentes[cedulasDocentes] = docente

                    guardar(libreria, "modelo\data.json")
                    True
            case  2:
                print(" 2. Visualización de docentes registrados ")
                verDocentes = docentes["cedulasDocentes"]
                print("Los docentes registrados hasta el momento son: ", int(len(verDocentes)))
                submenuRegistroDocentes()
                True
            case  3:
                print("** Volviendo al menú principal de 'SISGESA'... ")
                esperarTiempo(50_000)
                False
                break
        
#Submenu de la función registroDocentes            
def submenuRegistroDocentes():
    print("-" * 30)
    print("-" * 30)
    print(" OPCIONES ")
    print("-" * 30)
    print(" 1. Registro de docentes ")
    print("-" * 30)
    print(" 2. Visualización de docentes y sus módulos registrados ")
    print("-" * 30)
    print(" 3. Volver al menú principal de 'SISGESA' ")
    print("-" * 30)
    print("-" * 30)

def leerCodModulo(libreria, codigoModulo):
    if "modulos" not in libreria or codigoModulo not in libreria["modulos"]:
        print(f" El módulo con código {codigoModulo} no existe. ")
        return None
    
    modulo = libreria["modulos"][codigoModulo]

    return modulo

def leerCodEst(libreria, codigoEstudiante):
    if "estudiantes" not in libreria or codigoEstudiante not in libreria["estudiantes"]:
        print(f"El estudiante con código {codigoEstudiante} no existe.")
        return None
    
    estudiante = libreria["estudiantes"][codigoEstudiante]

    return estudiante

def submenuRegistroAsistencia(libreria, arch):
    print("-" * 30)
    print("-" * 30)
    print(" OPCIONES ")
    print("-" * 30)
    print(" 1. Registro de asistencia de llegada. ")
    print("-" * 30)
    print(" 2. Registro de asistencia de salida. ")
    print("-" * 30)
    print(" 3. Volver al menú principal de 'SISGESA' ")
    print("-" * 30)
    print("-" * 30)
    opcMenu = opcionMenuValida1(" >> Por favor ingrese una opción del menú", [1,2])
    match opcMenu:
        case 1:
            registroAsistenciaLlegada(libreria, arch)
        case 2:
            registroAsistenciaSalida(libreria, arch)
        case _:
            print(" >>Error. Por favor ingrese una opción válida. ")

def consultasRegistroGrupos(libreria):
    if "grupos" not in libreria or not libreria["grupos"]:
        print("No hay grupos registrados.")
        return
    
    grupos = libreria["grupos"]
    print("Códigos de grupos registrados:", grupos)
    
    for codigosGrupo in grupos:
        print(f"Código del grupo: {codigosGrupo}")
    
    print(f"Total de grupos registrados: {len(grupos)}")

def consultasRegistroModulos(libreria):
    if "modulos" not in libreria or not libreria["modulos"]:
        print("No hay modulos registrados.")
        return
    
    modulos = libreria["modulos"]
    print("Códigos de modulos registrados:", modulos)
    
    for codigosModulo in modulos:
        print(f"Código del grupo: {codigosModulo}")
    
    print(f"Total de grupos registrados: {len(modulos)}")

def consultasRegistroEstudiantes(libreria):
    if "estudiantes" not in libreria or not libreria["estudiantes"]:
        print("No hay estudiantes registrados.")
        return
    
    estudiantes = libreria["estudiantes"]
    print("Códigos de modulos registrados:", estudiantes)
    
    for codigosEstudiantes in estudiantes:
        print(f"Código del grupo: {codigosEstudiantes}")
    
    print(f"Total de grupos registrados: {len(estudiantes)}")

def consultasRegistroDocentes(libreria):
    if "docentes" not in libreria or not libreria["dcoentes"]:
        print("No hay docentes registrados.")
        return
    
    docentes = libreria["dcocentes"]
    print("Códigos de modulos registrados:", docentes)
    
    for cedulasDocentes in docentes:
        print(f"Código del grupo: {cedulasDocentes}")
    
    print(f"Total de grupos registrados: {len(docentes)}")

def submenuConsultasCodigo(libreria):
    print("-" * 30)
    print("-" * 30)
    print(" OPCIONES ")
    print("-" * 30)
    print(" 1. Consulta registro grupos. ")
    print("-" * 30)
    print(" 2. Consulta registro modulos. ")
    print("-" * 30)
    print(" 3. Consulta registro estudiantes. ")
    print("-" * 30)
    print(" 4. Consulta registro docentes. ")
    print("-" * 30)
    print("-" * 30)
    opcMenu = opcionMenuValida1(" >> Por favor ingrese una opción del menú", [1,4])
    match opcMenu:
        case 1:
            consultasRegistroGrupos(libreria)
        case 2:
            consultasRegistroModulos(libreria)
        case 3:
            consultasRegistroEstudiantes(libreria)
        case 4:
            consultasRegistroDocentes(libreria)
        case _:
            print(" >>Error. Por favor ingrese una opción válida. ")

