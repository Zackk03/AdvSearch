#!/usr/bin/python3
import platform, urllib.parse
from googlesearch import search
import os, webbrowser, time, signal, sys

about = """
 █████╗ ██████╗ ██╗   ██╗███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗██║   ██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
███████║██║  ██║██║   ██║███████╗█████╗  ███████║██████╔╝██║     ███████║
██╔══██║██║  ██║╚██╗ ██╔╝╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
██║  ██║██████╔╝ ╚████╔╝ ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
╚═╝  ╚═╝╚═════╝   ╚═══╝  ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
 Auth: Erick García M.                                    Github: Zackk03
~-==============================---[ About ]---==============================-~
Advance Search (ADVSearch) es una herramienta desarrollada para automatizar 
las búsquedas avanzadas con el motor de búsqueda Chrome, perteneciente a Google, 
donde a través de los Dorks, podemos filtrar y/o entoncontrar resultados con 
información interesante y/o sensible. ¡Usen con esta herramienta con cuidado! 
con esta pueden encontrar información útil o crítica. ¡Sean Éticos! 

Nota: Si no elige una búsqueda, dominio o IP, los resultados pueden ser más efectivos 
y a la vez generales, pero es posible de que no encuentres muchos resultados.

 ~-> Para más información >> https://www.exploit-db.com/google-hacking-database
 ~-> Para salir "Ctrl + C"


"""

# menu de opciones a las categorias de busqueda
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

# Handle Function >> Salida Forzosa
def handle(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Salida Forzosa
signal.signal(signal.SIGINT, handle)

# Constante de la URL
URL = "https://www.google.com/search?q="

# Función que contiene lo principal del programa
def main():

    # Sobre la herramienta
    clear()
    print(about)
    
    # Dominio o Dirección IP que será buscada
    busqueda = input("Búsqueda, Dominio o IP >> ")

    # Selección de las distintas categorias del menú
    clear()
    print(menu)
    opt = int(input("Ingrese una opción >> "))

# ""

    # Arbol de decisiones
    if opt == 1:
        if busqueda == "":
            print("\n\n[!] No se ha introducido nada para buscarse de manera específica\nPor favor ingrese la información requerida...\n")
            time.sleep(4)
            main()
        else:
            webbrowser.open_new_tab(URL + urllib.parse.quote(f'"{busqueda}" intext:{busqueda} intitle:{busqueda}'))
        main()

    if opt == 2:
        if busqueda == "":
            webbrowser.open_new_tab(URL + urllib.parse.quote("intitle:index of"))
        else:
            webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" intitle:"index.of"'))
        main()

    elif opt == 3:
        if busqueda == "":
            webbrowser.open_new_tab(URL + urllib.parse.quote("ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:cgf | ext:txt | ext:ora | ext:ini"))
        else:
            webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:cgf | ext:txt | ext:ora | ext:ini'))
        main()

    elif opt == 4:
        if busqueda == "":
            webbrowser.open_new_tab(URL + urllib.parse.quote("ext:sql | ext:db | ext:dbf | ext:mdb"))
        else:
            webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" ext:sql | ext:db | ext:dbf | ext:mdb'))
        main()

    elif opt == 5:
        if busqueda == "":
            webbrowser.open_new_tab(URL + urllib.parse.quote("ext:log"))
        else:
            webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" ext:log'))
        main()

    elif opt == 6:
        if busqueda == "":
            webbrowser.open_new_tab(URL + urllib.parse.quote("inurl:login | admin | user | cpanel | account | moderator | /cp | admin/default.aspx | http"))
        else:
            webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" inurl:login | admin | user | cpanel | account | moderator | /cp | admin/default.aspx | http'))
        main()

    elif opt == 7:
        if busqueda == "":
            webbrowser.open_new_tab(URL + urllib.parse.quote('intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning:mysql_connect()" | intext:"Warning:mysql_query()" | intext:"Warning:pg_connect()"'))
        else:
            webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning:mysql_connect()" | intext:"Warning:mysql_query()" | intext:"Warning:pg_connect()"'))
        main()

    elif opt == 8:
        if busqueda == "":
            webbrowser.open_new_tab(URL + urllib.parse.quote("ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"))
        else:
            webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"'))
        main()

    elif opt == 9:
        if busqueda == "":
            webbrowser.open_new_tab(URL + urllib.parse.quote("intext:pass.txt | password.zip | password.txt | index of | password | passwd | pwd | /pfx-password.txt | pw | username | SECRET_KEY | user"))
        else:
            webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" intext:pass.txt | password.zip | password.txt | index of | password | passwd | pwd | /pfx-password.txt | pw | username | SECRET_KEY | user | "'))
        main()

    elif opt == 10:
        if busqueda == "":
            webbrowser.open_new_tab(URL + urllib.parse.quote('intitle:"NETSurveillance WEB" | "jaeger UI" | "routeros" | "ZAP Scanning Report" "Alert Detail" | "Skipfish - scan results browse" | "Scan coverage information" AND "List of tests" ext:PDF | "Nikto Report" | "traefik" | "OpenNMS web console"'))
        else:
            webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" intitle:"NETSurveillance WEB" | "jaeger UI" | "routeros" | "ZAP Scanning Report" "Alert Detail" | "Skipfish - scan results browse" | "Scan coverage information" AND "List of tests" ext:PDF | "Nikto Report" | "traefik" | "OpenNMS web console"'))
        main()

    elif opt == 11:
        if busqueda == "":
            webbrowser.open_new_tab(URL + urllib.parse.quote('intitle:"index of" | "access_token.json" | "index of" intext:human resources | "index of" intext:"Apache/2.2.3" | "index of" "release.sh" | "index of" "deploy.sh" | "index of" "setup.sh" | "index of" "configure.sh" | "index of" "*db.sh" | "index of" "after.sh" | "index of" "phonepe" "wp-content" | "index of smtp"'))
        else:
            webbrowser.open_new_tab(URL + urllib.parse.quote(f'site:"{busqueda}" intitle:"index of" | "access_token.json" | "index of" intext: human resources | "index of" intext:"Apache/2.2.3" | "index of" "release.sh" | "index of" "deploy.sh" | "index of" "setup.sh" | "index of" "configure.sh" | "index of" "*db.sh" | "index of" "after.sh" | "index of" "phonepe" "wp-content" | "index of smtp"'))
        main()
        
    # Salida del programa
    elif opt == 12:
        main()

# Inicialización del programa
if __name__=="__main__":
    main()