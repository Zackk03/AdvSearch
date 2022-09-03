#!/usr/bin/python3
import platform, urllib.parse
from turtle import st
from GoogleSearchModule import search
import os, webbrowser, time, signal, sys

# ---------->>> Pantalla princial del programa <<<----------#
about = """
 █████╗ ██████╗ ██╗   ██╗███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
███████║██║  ██║██║   ██║███████╗█████╗  ███████║██████╔╝██║     ███████║
██╔══██║██║  ██║╚██╗ ██╔╝╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
██║  ██║██████╔╝ ╚████╔╝ ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
 Auth: Erick García M.                                   Github: Zackk03
~-==============================---[ About ]---==============================-~
Advance Search (ADVSearch) es una herramienta desarrollada para automatizar 
las búsquedas avanzadas con el motor de búsqueda Chrome, perteneciente a Google, 
donde a través de los Dorks, podemos filtrar y/o entoncontrar resultados con 
información interesante y/o sensible. ¡Usen con esta herramienta con cuidado! 
con esta pueden encontrar información útil o crítica. ¡Sean Éticos! 

Nota: Si no elige una búsqueda, dominio o IP, los resultados pueden ser más efectivos 
y a la vez generales, pero es posible de que no encuentres muchos resultados.

Nota: Los resultados son reportados tanto por web como por consola. Los resultados
por consola se limitan a 25, por cuestión de sobrecarga de peticiones.

 ~-> Para más información >> https://www.exploit-db.com/google-hacking-database
 ~-> Canal de Youtube >> https://www.youtube.com/channel/UCeJOzCokicB8RWXmckFBKNg
 ~-> Para salir "Ctrl + C"


"""

# ---------->>> Categorias <<<----------#
menu = """
~-==================[Categorias de Búsqueda]==================-~

1  ~-> Búsquedas Concretas/Específicas.
2  ~-> Directorios con información sensible.
3  ~-> Archivos de Configuración.
4  ~-> Archivos de Bases de Datos.
5  ~-> Archivos Logs.
6  ~-> Páginas de login.
7  ~-> Errores de SQL.
8  ~-> Documentos expuestos públicamente.
9  ~-> Archivos con contraseñas.
10 ~-> Redes e información vulnerada.
11 ~-> Información valiosa.
12 ~-> Regresar.


"""

# Función para salir de los distintos sistemas operativos
def clear():
    if platform.system() == 'Linux':
        os.system("clear")
    elif platform.system() == 'Windows':
        os.system("cls")
    elif platform.system() == 'Darwin':
        os.system("clear")

# Handle Function >> Salida Forzosa (CTRL + C)
def handle(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Salida Forzosa
signal.signal(signal.SIGINT, handle)

# ---------->>> Constante de la URL <<<-----------
URL = "https://www.google.com/search?q="

# ---------->>> Función que contiene lo principal del programa <<<----------#
def main():
    
    # Contador de los resultados por consola
    n = 1

    # ---------->>> Sobre la herramienta <<<----------#
    clear()
    print(about)
    
    # ---------->>> Búsqueda, Dominio o Dirección IP <<<----------#
    busqueda = input("Búsqueda, Dominio o IP >> ")

    # ---------->>> Categorias <<<----------#
    clear()
    print(menu)
    opt = int(input("Ingrese una opción >> "))

    # ---------->>> Arbol de decisiones <<<----------#
    # Búsquedas de información de manera concreta

    # Controlador de errores
    try:
        # Información Concreta
        if opt == 1:
            # Error al no introducir nada y Búsqueda vacia
            if busqueda == "":
                print("\n\n[!] No se ha introducido nada para buscarse de manera específica\n    Por favor ingrese la información requerida...\n")
                time.sleep(4)
                main()
            else:
                # Consulta a la web 
                webbrowser.open_new_tab(URL + urllib.parse.quote(f'"{busqueda}" intext:"{busqueda}" intitle:"{busqueda}"'))
                
                # Consulta a la web reportada por consola
                query=search(f'"{busqueda}" intext:"{busqueda}" intitle:"{busqueda}"', num=10, stop=25)
                
                print(f"\n[INFO] Resultados de la búsqueda sobre >> {busqueda}\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "informacion_concreta.txt"
                archivo = open(nombre_archivo, "w")

                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")

                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("informacion_concreta.txt")
                    input("\n[!] Pulse Enter para regresar...")
            
            # Regresa        
            main()

        # Directorios con Información Sensible
        elif opt == 2:

            # Búsqueda vacia
            if busqueda == "":
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote("intitle:index of"))
                
                # Consulta a la web reportada por consola
                query=search("intitle:index of", num=10, stop=25)

                print(f"\n[INFO] Resultados de la búsqueda sobre Directorios con información Sensible\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "direc_sensibles.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("direc_sensibles.txt")
                    input("\n[!] Pulse Enter para regresar...")
            else:
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" intitle:index of'))
                
                # Consulta a la web reportada por consola
                query=search(f'site:"{busqueda}" intitle:index of', num=10)
                print(f"\n[INFO] Resultados de la búsqueda sobre >> {busqueda}\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "direc_sensibles_busq.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("direc_sensibles_busq.txt")
                    input("\n[!] Pulse Enter para regresar...")
            # Regresa        
            main()

        # Archivos de Configuración
        elif opt == 3:

            # Búsqueda vacia
            if busqueda == "":
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote("ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:cgf | ext:txt | ext:ora | ext:ini"))
                
                # Consulta a la web reportada por consola
                query=search("ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:cgf | ext:txt | ext:ora | ext:ini", num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre Archivos de Configuración\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "archivos_conf.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("archivos_conf.txt")
                    input("\n[!] Pulse Enter para regresar...")
            else:
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:cgf | ext:txt | ext:ora | ext:ini'))
                
                # Consulta a la web reportada por consola
                query=search(f'site:"{busqueda}" ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:cgf | ext:txt | ext:ora | ext:ini', num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre >> {busqueda}\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "archivos_conf_busq.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("archivos_conf_busq.txt")
                    input("\n[!] Pulse Enter para regresar...")
            # Regresa
            main()

        # Archivos de Bases de Datos
        elif opt == 4:

            # Búsqueda vacia
            if busqueda == "":
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote("ext:sql | ext:db | ext:dbf | ext:mdb"))
                
                # Consulta a la web reportada por consola
                query=search("ext:sql | ext:db | ext:dbf | ext:mdb", num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre Archivos de Bases de Datos\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "archivos_DB.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("archivos_DB.txt")
                    input("\n[!] Pulse Enter para regresar...")
            else:
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" ext:sql | ext:db | ext:dbf | ext:mdb'))
                
                # Consulta a la web reportada por consola
                query=search(f'site:"{busqueda}" ext:sql | ext:db | ext:dbf | ext:mdb', num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre >> {busqueda}\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "archivos_DB_busq.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("archivos_DB_busq.txt")
                    input("\n[!] Pulse Enter para regresar...")
            # Regresa
            main()

        # Archivos Logs
        elif opt == 5:

            # Búsqueda vacia
            if busqueda == "":
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote("ext:log"))
                
                # Consulta a la web reportada por consola
                query=search("ext:log", num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre Archivos Logs\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "archivos_logs.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("archivos_logs.txt")
                    input("\n[!] Pulse Enter para regresar...")
            else:
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" ext:log'))
                
                # Consulta a la web reportada por consola
                query=search(f'site:"{busqueda}" ext:log', num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre >> {busqueda}\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "archivos_logs_busq.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("archivos_logs_busq.txt")
                    input("\n[!] Pulse Enter para regresar...")
            # Regresa
            main()
        
        # Páginas de Login
        elif opt == 6:

            # Búsqueda vacia
            if busqueda == "":
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote("inurl:login | admin | user | cpanel | account | moderator | /cp | admin/default.aspx | http"))
                
                # Consulta a la web reportada por consola
                query=search("inurl:login | admin | user | cpanel | account | moderator | /cp | admin/default.aspx | http", num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre Páginas de Login\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "paginas_login.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("paginas_login.txt")
                    input("\n[!] Pulse Enter para regresar...")
            else:
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" inurl:login | admin | user | cpanel | account | moderator | /cp | admin/default.aspx | http'))
                
                # Consulta a la web reportada por consola
                query=search(f'site:"{busqueda}" inurl:login | admin | user | cpanel | account | moderator | /cp | admin/default.aspx | http', num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre >> {busqueda}\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "paginas_login_busq.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("paginas_login_busq.txt")
                    input("\n[!] Pulse Enter para regresar...")
            # Regresa
            main()

        # Errores de SQL
        elif opt == 7:

            # Búsqueda vacia
            if busqueda == "":
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote('intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning:mysql_connect()" | intext:"Warning:mysql_query()" | intext:"Warning:pg_connect()"'))
                
                # Consulta a la web reportada por consola
                query=search('intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning:mysql_connect()" | intext:"Warning:mysql_query()" | intext:"Warning:pg_connect()"', num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre Errores de SQL\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "errores_SQL.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("errores_SQL.txt")
                    input("\n[!] Pulse Enter para regresar...")
            else:
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning:mysql_connect()" | intext:"Warning:mysql_query()" | intext:"Warning:pg_connect()"'))
                
                # Consulta a la web reportada por consola
                query=search(f'site:"{busqueda}" intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning:mysql_connect()" | intext:"Warning:mysql_query()" | intext:"Warning:pg_connect()"', num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre >> {busqueda}\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "errores_SQL_busq.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("errores_SQL_busq.txt")
                    input("\n[!] Pulse Enter para regresar...")
            # Regresa
            main()

        # Documentos Expuestos Públicamente
        elif opt == 8:

            # Búsqueda vacia
            if busqueda == "":
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote("ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"))
                
                # Consulta a la web reportada por consola
                query=search("ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv", num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre Documentos Expuestos Públicamente\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "doc_exp_pub.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("doc_exp_pub.txt")
                    input("\n[!] Pulse Enter para regresar...")
            else:
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"'))
                
                # Consulta a la web reportada por consola
                query=search(f'site:"{busqueda}" ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"', num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre >> {busqueda}\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "doc_exp_pub_busq.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("doc_exp_pub_busq.txt")
                    input("\n[!] Pulse Enter para regresar...")
            # Regresa
            main()

        # Archivos con Contraseñas
        elif opt == 9:

            # Búsqueda vacia
            if busqueda == "":
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote("intext:pass.txt | password.zip | password.txt | index of | password | passwd | pwd | /pfx-password.txt | pw | username | SECRET_KEY | user"))
                
                # Consulta a la web reportada por consola
                query=search("intext:pass.txt | password.zip | password.txt | index of | password | passwd | pwd | /pfx-password.txt | pw | username | SECRET_KEY | user", num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre Archivos con Contraseñas\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "archivos_contraseñas.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("archivos_contraseñas.txt")
                    input("\n[!] Pulse Enter para regresar...")
            else:
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" intext:pass.txt | password.zip | password.txt | index of | password | passwd | pwd | /pfx-password.txt | pw | username | SECRET_KEY | user | "'))
                
                # Consulta a la web reportada por consola
                query=search(f'site:"{busqueda}" intext:pass.txt | password.zip | password.txt | index of | password | passwd | pwd | /pfx-password.txt | pw | username | SECRET_KEY | user | "', num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre >> {busqueda}\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "archivos_contraseñas_busq.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("archivos_contraseñas_busq.txt")
                    input("\n[!] Pulse Enter para regresar...")
            # Regresa
            main()

        # Redes e información Vulnerada
        elif opt == 10:

            # Búsqueda vacia
            if busqueda == "":
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote('intitle:"NETSurveillance WEB" | "jaeger UI" | "routeros" | "ZAP Scanning Report" "Alert Detail" | "Skipfish - scan results browse" | "Scan coverage information" AND "List of tests" ext:PDF | "Nikto Report" | "traefik" | "OpenNMS web console"'))
                print(f"\n[INFO] Resultados de la búsqueda sobre Redes e información Vulnerada\n")
                
                # Consulta a la web reportada por consola
                query=search('intitle:"NETSurveillance WEB" | "jaeger UI" | "routeros" | "ZAP Scanning Report" "Alert Detail" | "Skipfish - scan results browse" | "Scan coverage information" AND "List of tests" ext:PDF | "Nikto Report" | "traefik" | "OpenNMS web console"', num=10, stop=25)
                
                #Nombre del archivo a guardar
                nombre_archivo = "redes_infovuln.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("redes_infovuln.txt")
                    input("\n[!] Pulse Enter para regresar...")
            else:
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" intitle:"NETSurveillance WEB" | "jaeger UI" | "routeros" | "ZAP Scanning Report" "Alert Detail" | "Skipfish - scan results browse" | "Scan coverage information" AND "List of tests" ext:PDF | "Nikto Report" | "traefik" | "OpenNMS web console"'))
                
                # Consulta a la web reportada por consola
                query=search(f'site:"{busqueda}" intitle:"NETSurveillance WEB" | "jaeger UI" | "routeros" | "ZAP Scanning Report" "Alert Detail" | "Skipfish - scan results browse" | "Scan coverage information" AND "List of tests" ext:PDF | "Nikto Report" | "traefik" | "OpenNMS web console"', num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre >> {busqueda}\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "redes_infovuln_busq.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("redes_infovuln_busq.txt")
                    input("\n[!] Pulse Enter para regresar...")
            # Regresa
            main()

        # Información valiosa
        elif opt == 11:

            # Búsqueda vacia
            if busqueda == "":
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote('intitle:"index of" | "access_token.json" | "index of" intext:human resources | "index of" intext:"Apache/2.2.3" | "index of" "release.sh" | "index of" "deploy.sh" | "index of" "setup.sh" | "index of" "configure.sh" | "index of" "*db.sh" | "index of" "after.sh" | "index of" "phonepe" "wp-content" | "index of smtp"'))
                
                # Consulta a la web reportada por consola
                query=search('intitle:"index of" | "access_token.json" | "index of" intext:human resources | "index of" intext:"Apache/2.2.3" | "index of" "release.sh" | "index of" "deploy.sh" | "index of" "setup.sh" | "index of" "configure.sh" | "index of" "*db.sh" | "index of" "after.sh" | "index of" "phonepe" "wp-content" | "index of smtp"', num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre Información valiosa\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "info_valiosa.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("info_valiosa.txt")
                    input("\n[!] Pulse Enter para regresar...")
            else:
                # Consulta a la web
                webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" intitle:"index of" | "access_token.json" | "index of" intext: human resources | "index of" intext:"Apache/2.2.3" | "index of" "release.sh" | "index of" "deploy.sh" | "index of" "setup.sh" | "index of" "configure.sh" | "index of" "*db.sh" | "index of" "after.sh" | "index of" "phonepe" "wp-content" | "index of smtp"'))
                
                # Consulta a la web reportada por consola
                query=search(f'site:"{busqueda}" intitle:"index of" | "access_token.json" | "index of" intext: human resources | "index of" intext:"Apache/2.2.3" | "index of" "release.sh" | "index of" "deploy.sh" | "index of" "setup.sh" | "index of" "configure.sh" | "index of" "*db.sh" | "index of" "after.sh" | "index of" "phonepe" "wp-content" | "index of smtp"', num=10, stop=25)
                print(f"\n[INFO] Resultados de la búsqueda sobre >> {busqueda}\n")
                
                #Nombre del archivo a guardar
                nombre_archivo = "info_valiosa_busq.txt"
                archivo = open(nombre_archivo, "w")
                
                # Introducción de datos al archivo y reporte por consola
                for i in query:
                    print(f"Link {n} >> {i}")
                    archivo.write(f"Link {n} >> {i}\n")
                    n = n + 1
                print("\n\n[INFO] Estos han sido todos los resultados...\n.")
                
                # Para guardar si o no los resultados generados
                saveq = input("¿Desea guardar los resultados? [S/N] >> ")
                if saveq == "S" or saveq == "s":
                    print("[!] Guardando...")
                    time.sleep(2)   
                    archivo.close()
                else:
                    archivo.close()
                    os.remove("info_valiosa_busq.txt")
                    input("\n[!] Pulse Enter para regresar...")
            # Regresa
            main()
            
        # Salida del programa
        elif opt == 12:
            main()
        
        # Por si ingresan datos erroneos
        else: input("\n\n[!] Por favor introduzca una de las opciones disponibles [1-12]\n    Pulse Enter para reintentar...")
        main()
    # ---------->>> Control de errores 409 <<<----------#
    except:
        input("[!] Parece que ha excedido el límite de peticiones de búsqueda.\n    De todas maneras, los resultados los puede visualizar en el navegador.\n    Para visualizar las peticiones por consola, deberá esperar un momento\n    Pulse Enter para regresar...")
        main()

# ---------->>> Inicialización del programa <<<----------#
if __name__=="__main__":
    main()