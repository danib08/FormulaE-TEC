"""
Archivo Main
Python 3.7.3

Imports:
"""
import tkinter as tk
import tkinter.messagebox
from Instancias import *
from WifiClient import NodeMCU
from threading import Thread
from time import sleep

# ****************** Variables ******************
button_font = ("Verdana", 12) # Fuente para lables/botones
small_font = ("Verdana", 10)  # Fuente para lables
escud_menu = suning  # Escuderia a ser ensenada en el menu


# ****************** Manejo de archivos de texto ******************

# Archivo del logo de la escuderia del menu
set_logo = open("Archivos de texto/logo.txt", "r") # Se abre para ser leido
set1 = set_logo.read()  # Se guarda el logo en una variable
set_logo.close()   # Se cierra el archivo
escud_menu.set_logo(set1)  # Se guarda el atributo logo de la escuderia del menu

# Archivo de los patrocinadores de la escuderia del menu
set_sponsors = open("Archivos de texto/sponsors.txt", "r") # Se abre para ser leido
set2 = set_sponsors.read().split("#") # Se guardan los patrocinadores en una variable como una lista de cada uno
set_sponsors.close()  # Se cierra el archivo
escud_menu.set_patrocinadores(set2)  # Se guarda el atributo patrocinadores de la escuderia del menu

# Archivo de los pilotos
set_pilotos = open("Archivos de texto/pilotos.txt", "r")  # Se abre para ser leido
lista_p = set_pilotos.read().split("#") # Lista donde cada elemento representa un piloto
set_pilotos.close() # Se cierra el archivo

# Setting de los pilotos
i = 0 # contador
for p in lista_p:    # se itera sobre cada 'piloto' en la lista
    tmp = p.split("*")  # se separa cada atributo del piloto en una lista
    # Se guarda cada atributo del piloto
    pilotos[i].set_nombre(tmp[0])
    pilotos[i].set_edad(int(tmp[1]))
    pilotos[i].set_nacionalidad(tmp[2])
    pilotos[i].set_temporada(int(tmp[3]))
    pilotos[i].set_cant_compet(int(tmp[4]))
    pilotos[i].set_cant_vict(int(tmp[5]))
    pilotos[i].set_cant_destacadas(int(tmp[6]))
    pilotos[i].set_cant_fallidas(int(tmp[7]))
    i += 1 # Se aumenta el contador


# Archivo de los automoviles
set_autos = open("Archivos de texto/autos.txt", "r")  # Se abre para ser leido
lista_a = set_autos.read().split("#") # Lista donde cada elemento representa un automovil
set_autos.close()  # Se cierra el archivo

# Setting de los automoviles
j = 0 # contador
for a in lista_a:   # se itera sobre cada 'automovil' en la lista
    tmp = a.split("*")  # se separa cada atributo del automovil en una lista
    # Se guarda cada atributo del automovil
    autos[j].set_marca(tmp[0])
    autos[j].set_modelo(tmp[1])
    autos[j].set_pais(tmp[2])
    autos[j].set_temporada(int(tmp[3]))
    autos[j].set_cant_baterias(int(tmp[4]))
    autos[j].set_cant_pilas(int(tmp[5]))
    autos[j].set_tension(int(tmp[6]))
    autos[j].set_estado(tmp[7])
    autos[j].set_consumo(float(tmp[8]))
    autos[j].set_nivel_bateria(int(tmp[9]))
    autos[j].set_peso(int(tmp[10]))
    autos[j].set_eficiencia(float(tmp[11]))
    j += 1 # Se aumenta el contador

# ****************** Variables Test Drive ******************
pwm = 0  # Variable traccion
direc = 0  # Variable direccion
luz_der = 0  # Variable luz_derecha
der_flag = False  # Variable flag para la luz derecha (maneja que sea intermitente)
luz_izq = 0  # Variable luz izquierda
izq_flag = False  # Variable flag para la luz izquierda (maneja que sea intermitente)
luz_fro = 0  # Variable luz frontales
luz_tra = 0  # Variable luz traseras
ldr = 0  # Variable de luz
bat = autos[0].nivel_bateria  # Variable nivel de bateria

# ****************** Cliente NodeMCU ******************
myCar = NodeMCU()
myCar.start()

# ****************** Funciones ******************
"""
Funcion ir_a_about
E: -
S: se muestra el frame del about y desaparecen los demas
R: -
"""
def ir_a_about():
    menu.grid_forget()
    tabla_p.grid_forget()
    grid_pilotos.grid_forget()
    tabla_a.grid_forget()
    grid_autos.grid_forget()
    test_drive.grid_forget()
    about.grid(row=0, column=0)


"""
Funcion ir_a_menu
E: -
S: se muestra el frame del menu y desaparecen los demas
R: -
"""
def ir_a_menu():
    about.grid_forget()
    tabla_p.grid_forget()
    grid_pilotos.grid_forget()
    tabla_a.grid_forget()
    grid_autos.grid_forget()
    test_drive.grid_forget()
    menu.grid(row=0, column=0)


"""
Funcion ir_a_tabla_p
E: -
S: se muestran los frames tabla_p y grid_pilotos, y desaparecen los demas
R: -
"""
def ir_a_tabla_p():
    menu.grid_forget()
    about.grid_forget()
    tabla_a.grid_forget()
    grid_autos.grid_forget()
    test_drive.grid_forget()
    tabla_p.grid(row=0, column=0)
    grid_pilotos.grid(row=7, column=0, columnspan=8)


"""
Funcion ir_a_tabla_a
E: -
S: se muestran los frames tabla_a y grid_autos, y desaparecen los demas
R: -
"""
def ir_a_tabla_a():
    menu.grid_forget()
    about.grid_forget()
    tabla_p.grid_forget()
    grid_pilotos.grid_forget()
    test_drive.grid_forget()
    tabla_a.grid(row=0, column=0)
    grid_autos.grid(row=7, column=0, columnspan=5)


"""
Funcion ir_a_test_drive
E: -
S: se muestra el frame del test_drive y desaparecen los demas
R: -
"""
def ir_a_test_drive():

    menu.grid_forget()
    about.grid_forget()
    tabla_p.grid_forget()
    grid_pilotos.grid_forget()
    tabla_a.grid_forget()
    grid_autos.grid_forget()
    test_drive.grid(row=0, column=0)


"""
Funcion info_escuderia
E: -
S: se guarda la info de la escuderia del menu en una variable 'info' y se muestra en una messagebox
R: -
"""
def info_escuderia():
    sponsors = ""
    ult_pat = len(escud_menu.patrocinadores) - 1

    # Se crea un str con los patrocinadores
    for i in range(len(escud_menu.patrocinadores)):
        sponsors += escud_menu.patrocinadores[i]
        if i != ult_pat:
            sponsors += ", "

    pilotos = ""
    ult_pil = len(escud_menu.pilotos) - 1

    # Se crea un str con los pilotos
    for i in range(len(escud_menu.pilotos)):
        pilotos += escud_menu.pilotos[i].nombre
        if i != ult_pil:
            pilotos += ", "

    # Se elabora un str con toda la informacion
    info = "Nombre: %s \nTemporada: 2019 \nUbicación: %s \nPatrocinadores: %s \nPilotos: %s \nAutomóvil actual: " \
           "%s (%s) \nIGE: %s" % (escud_menu.nombre, escud_menu.ubicacion, sponsors, pilotos,
                                  escud_menu.auto_actual.modelo, escud_menu.auto_actual.estado,
                                  escud_menu.indice_escud())
    # Se muestra toda la info de la escuderia
    tkinter.messagebox.showinfo("Información de la escudería", info)


"""
Funcion editar_escud
E: -
S: se abre un Toplevel para editar el logo y los patrocinadores de la escuderia del menu
R: -
"""
def editar_escud():
    tkinter.messagebox.showinfo("Ayuda", "Visite la ventana About para conocer más sobre cómo editar correctamente "
                                "la escudería.")
    top = tk.Toplevel(bg="chocolate1")
    top.title("Editar")
    top.resizable(width=False, height=False)

    label1 = tk.Label(top, text="Logo:", font=small_font, bg="chocolate1")
    label2 = tk.Label(top, text="Patrocinadores:", font=small_font, bg="chocolate1")

    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)

    entry1 = tk.Entry(top)
    entry2 = tk.Entry(top)

    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    # Boton para editar el logo
    button_top_1 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="linen", activebackground="firebrick1",
                             borderwidth=5, relief="ridge", command=lambda: editar_logo(entry1.get()))
    # Boton para editar los patrocinadores
    button_top_2 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="linen", activebackground="firebrick1",
                             borderwidth=5, relief="ridge", command=lambda: editar_patrocinadores(entry2.get()))
    button_top_1.grid(row=0, column=2)
    button_top_2.grid(row=1, column=2)


"""
Funcion editar_logo
E: logo (string)
S: se hace un set_logo() de la escuderia con el valor ingresado y se guarda en el archivo de texto
R: -
"""
def editar_logo(logo):
    logo_text = open("Archivos de texto/logo.txt", "w") # Se abre para escribir
    logo_text.write(logo)  # Se escribe el logo ingresado
    logo_text.close()  # Se cierra el archivo
    escud_menu.set_logo(logo)  # Se guarda el nuevo atributo logo


"""
Funcion editar_patrocinadores
E: patrocinadores (string)
S: se hace un set_patrocinadores () de la escuderia con el valor ingresado y se guarda en el archivo de texto
R: -
"""
def editar_patrocinadores(patrocinadores):
    sponsors_text = open("Archivos de texto/sponsors.txt", "w") # Se abre para escribir
    sponsors_text.write(patrocinadores) # Se escriben los patrocinadores ingresados y separados po '#'
    sponsors_text.close() # Se cierra el archivo
    lista = patrocinadores.split("#") # Se separan los patrocinadores en una lista
    escud_menu.set_patrocinadores(lista)   # Se guarda el nuevo atributo patrocinadores


"""
Funcion ayuda
E: -
S: muestra informacion sobre como editar correctamente todo en la interfaz
R: -
"""
def ayuda():
    tkinter.messagebox.showinfo("¿Cómo editar?", "Para editar el logo simplemente ingrese el nombre de la imagen con su"
                                " extensión .png y haga click en el botón 'Editar'. La imagen debe estar guardada en la"
                                " dirección 'Formula E-Tec/Images/Logos'. \n\nPara editar los patrocinadores, ingréselos"
                                " separados por '#', de otra manera no funcionará.  \n\nPara editar los pilotos, ingrese"
                                " el número del piloto, siendo 1 el de más arriba y 10 el de más abajo. De la misma "
                                "manera con los automóviles. Luego ingrese el valor deseado en la casilla.")


"""
Funcion rgp_asc
E: -
S: ordena la lista de pilotos de manera ascendente segun el rendimiento global
R: -
"""
def rgp_asc():
    # Algoritmo de Selection Sort
    for i in range(len(pilotos) - 1):
        minIndex = i
        for j in range(i + 1, len(pilotos)):
            if pilotos[j].rend_global() < pilotos[minIndex].rend_global():
                minIndex = j
        if minIndex != i:
            tmp = pilotos[i]
            pilotos[i] = pilotos[minIndex]
            pilotos[minIndex] = tmp
    grid_p(-10) # Se llama a la funcion que coloca a los pilotos en pantalla


"""
Funcion rgp_des
E: -
S: ordena la lista de pilotos de manera descendente segun el rendimiento global
R: -
"""
def rgp_des():
    # Algoritmo de Selection Sort
    for i in range(len(pilotos) - 1):
        maxIndex = i
        for j in range(i + 1, len(pilotos)):
            if pilotos[j].rend_global() > pilotos[maxIndex].rend_global():
                maxIndex = j
        if maxIndex != i:
            tmp = pilotos[i]
            pilotos[i] = pilotos[maxIndex]
            pilotos[maxIndex] = tmp
    grid_p(1) # Se llama a la funcion que coloca a los pilotos en pantalla


"""
Funcion rep_asc
E: -
S: ordena la lista de pilotos de manera ascendente segun el rendimiento especifico
R: -
"""
def rep_asc():
    # Algoritmo de Selection Sort
    for i in range(len(pilotos) - 1):
        minIndex = i
        for j in range(i + 1, len(pilotos)):
            if pilotos[j].rend_espec() < pilotos[minIndex].rend_espec():
                minIndex = j
        if minIndex != i:
            tmp = pilotos[i]
            pilotos[i] = pilotos[minIndex]
            pilotos[minIndex] = tmp
    grid_p(-10) # Se llama a la funcion que coloca a los pilotos en pantalla


"""
Funcion rep_des
E: -
S: ordena la lista de pilotos de manera descendente segun el rendimiento especifico
R: -
"""
def rep_des():
    # Algoritmo de Selection Sort
    for i in range(len(pilotos) - 1):
        maxIndex = i
        for j in range(i + 1, len(pilotos)):
            if pilotos[j].rend_espec() > pilotos[maxIndex].rend_espec():
                maxIndex = j
        if maxIndex != i:
            tmp = pilotos[i]
            pilotos[i] = pilotos[maxIndex]
            pilotos[maxIndex] = tmp
    grid_p(1) # Se llama a la funcion que coloca a los pilotos en pantalla


"""
Funcion grid_p
E: posicion (numero)
S: muestra a los pilotos en pantalla iterando sobre el grid
R: -
"""
def grid_p(pos):
    # Vacia el frame grid_pilotos antes de colocar los pilotos
    for widget in grid_pilotos.winfo_children():
        widget.destroy()

    # Itera sobre las filas del grid, de 0 a 9
    for i in range(10):
        # Crea lables con la informacion de cada piloto usando i como indice para la lista 'pilotos'
        rank = tk.Label(grid_pilotos, text=abs(pos), font=button_font, bg="lightblue")
        nombre = tk.Label(grid_pilotos, text=pilotos[i].nombre, font=button_font, bg="lightblue")
        edad = tk.Label(grid_pilotos, text=pilotos[i].edad, font=button_font, bg="lightblue")
        pais = tk.Label(grid_pilotos, text=pilotos[i].nacionalidad, font=button_font, bg="lightblue")
        temp = tk.Label(grid_pilotos, text=pilotos[i].temporada, font=button_font, bg="lightblue")
        comp = tk.Label(grid_pilotos, text=pilotos[i].cant_compet, font=button_font, bg="lightblue")
        rgp = tk.Label(grid_pilotos, text=pilotos[i].rend_global(), font=button_font, bg="lightblue")
        rep = tk.Label(grid_pilotos, text=pilotos[i].rend_espec(), font=button_font, bg="lightblue")

        # Coloca las labels en la fila correspondiente al i del momento
        rank.grid(row=i, column=0)
        nombre.grid(row=i, column=1)
        edad.grid(row=i, column=2)
        pais.grid(row=i, column=3)
        temp.grid(row=i, column=4)
        comp.grid(row=i, column=5)
        rgp.grid(row=i, column=6)
        rep.grid(row=i, column=7)

        pos += 1 # Se aumenta la posicion

    # Se crea y coloca una entry para luego editar algun piloto
    entry = tk.Entry(grid_pilotos)
    entry.grid(row=5, column=8)

    # Se crea y coloca un boton que llama a la funcion editar_piloto con el entry.get()
    editar = tk.Button(grid_pilotos, text="Editar", font=button_font, bg="deep sky blue", activebackground="cyan",
                       borderwidth=5, relief="ridge", command=lambda: editar_piloto(entry.get()))
    editar.grid(row=4, column=8)


"""
Funcion editar_piloto
E: j (string)
S: se crea un Toplevel con toda la info del piloto seleccionado y mecanismos para editar esta misma
R: el string debe ser un numero entero entre 1 y 10
"""
def editar_piloto(j):
    if j.isdigit() and 1 <= int(j) <= 10:
        tkinter.messagebox.showinfo("Ayuda", "Visite la ventana About para conocer más sobre cómo editar correctamente "
                                             "los pilotos.")
        top = tk.Toplevel(bg="lightblue")
        top.title("Editar")
        top.resizable(width=False, height=False)

        i = int(j) - 1  # indice del piloto en la lista 'pilotos'

        # Se crean labels con toda la info del piloto seleccionado
        label1 = tk.Label(top, text="Nombre: " + pilotos[i].nombre, font=small_font, bg="lightblue")
        label2 = tk.Label(top, text="Edad: " + str(pilotos[i].edad), font=small_font, bg="lightblue")
        label3 = tk.Label(top, text="Nacionalidad: " + pilotos[i].nacionalidad, font=small_font, bg="lightblue")
        label4 = tk.Label(top, text="Temporada: " + str(pilotos[i].temporada), font=small_font, bg="lightblue")
        label5 = tk.Label(top, text="Competencias: " + str(pilotos[i].cant_compet), font=small_font, bg="lightblue")
        label6 = tk.Label(top, text="Victorias: " + str(pilotos[i].victorias), font=small_font, bg="lightblue")
        label7 = tk.Label(top, text="Destacadas: " + str(pilotos[i].cant_destacadas), font=small_font, bg="lightblue")
        label8 = tk.Label(top, text="Fallidas: " + str(pilotos[i].cant_fallidas), font=small_font, bg="lightblue")

        # Se colocan las labels
        label1.grid(row=0, column=0)
        label2.grid(row=1, column=0)
        label3.grid(row=2, column=0)
        label4.grid(row=3, column=0)
        label5.grid(row=4, column=0)
        label6.grid(row=5, column=0)
        label7.grid(row=6, column=0)
        label8.grid(row=7, column=0)

        # Se crea un entry por cada label creado
        entry1 = tk.Entry(top)
        entry2 = tk.Entry(top)
        entry3 = tk.Entry(top)
        entry4 = tk.Entry(top)
        entry5 = tk.Entry(top)
        entry6 = tk.Entry(top)
        entry7 = tk.Entry(top)
        entry8 = tk.Entry(top)

        # Se colocan las entrys al lado de su label respectiva
        entry1.grid(row=0, column=1)
        entry2.grid(row=1, column=1)
        entry3.grid(row=2, column=1)
        entry4.grid(row=3, column=1)
        entry5.grid(row=4, column=1)
        entry6.grid(row=5, column=1)
        entry7.grid(row=6, column=1)
        entry8.grid(row=7, column=1)

        # Se crea un boton por cada entry creado, cada uno llama a la funcion editar_p_aux
        button_top_1 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="deep sky blue", activebackground="cyan",
                                 borderwidth=5, relief="ridge", command=lambda: editar_p_aux(1, i, entry1.get()))
        button_top_2 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="deep sky blue", activebackground="cyan",
                                 borderwidth=5, relief="ridge", command=lambda: editar_p_aux(2, i, entry2.get()))
        button_top_3 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="deep sky blue", activebackground="cyan",
                                 borderwidth=5, relief="ridge", command=lambda: editar_p_aux(3, i, entry3.get()))
        button_top_4 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="deep sky blue", activebackground="cyan",
                                 borderwidth=5, relief="ridge", command=lambda: editar_p_aux(4, i, entry4.get()))
        button_top_5 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="deep sky blue", activebackground="cyan",
                                 borderwidth=5, relief="ridge", command=lambda: editar_p_aux(5, i, entry5.get()))
        button_top_6 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="deep sky blue", activebackground="cyan",
                                 borderwidth=5, relief="ridge", command=lambda: editar_p_aux(6, i, entry6.get()))
        button_top_7 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="deep sky blue", activebackground="cyan",
                                 borderwidth=5, relief="ridge", command=lambda: editar_p_aux(7, i, entry7.get()))
        button_top_8 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="deep sky blue", activebackground="cyan",
                                 borderwidth=5, relief="ridge", command=lambda: editar_p_aux(8, i, entry8.get()))
        # Se colocan los botones al lado de su entry respectiva
        button_top_1.grid(row=0, column=2)
        button_top_2.grid(row=1, column=2)
        button_top_3.grid(row=2, column=2)
        button_top_4.grid(row=3, column=2)
        button_top_5.grid(row=4, column=2)
        button_top_6.grid(row=5, column=2)
        button_top_7.grid(row=6, column=2)
        button_top_8.grid(row=7, column=2)
    else:
        # Messagebox de error si no se cumple la restriccion de arriba
        tkinter.messagebox.showerror("Error", "Debe ingresar un entero de 1 a 10")


"""
Funcion editar_p_aux
E: atrib (numero), i (indice), entry
S: segun el atrib, se hace un set del piloto en la posicion 'i' con el entry
R: -
"""
def editar_p_aux(atrib, i, entry):
    if atrib == 1:
        pilotos[i].set_nombre(entry)
    elif atrib == 2:
        pilotos[i].set_edad(entry)
    elif atrib == 3:
        pilotos[i].set_nacionalidad(entry)
    elif atrib == 4:
        pilotos[i].set_temporada(entry)
    elif atrib == 5:
        pilotos[i].set_cant_compet(entry)
    elif atrib == 6:
        pilotos[i].set_cant_vict(entry)
    elif atrib == 7:
        pilotos[i].set_cant_destacadas(entry)
    else:
        pilotos[i].set_cant_fallidas(entry)


"""
Funcion efic_asc
E: -
S: ordena la lista de autos de manera ascendente segun la eficiencia
R: -
"""
def efic_asc():
    # Algoritmo de Selection Sort
    for i in range(len(autos) - 1):
        minIndex = i
        for j in range(i + 1, len(autos)):
            if autos[j].eficiencia > autos[minIndex].eficiencia:
                minIndex = j
        if minIndex != i:
            tmp = autos[i]
            autos[i] = autos[minIndex]
            autos[minIndex] = tmp
    grid_a() # Se llama a la funcion que coloca los autos en pantalla


"""
Funcion efic_des
E: -
S: ordena la lista de autos de manera descendente segun la eficiencia
R: -
"""
def efic_des():
    # Algoritmo de Selection Sort
    for i in range(len(autos) - 1):
        maxIndex = i
        for j in range(i + 1, len(autos)):
            if autos[j].eficiencia < autos[maxIndex].eficiencia:
                maxIndex = j
        if maxIndex != i:
            tmp = autos[i]
            autos[i] = autos[maxIndex]
            autos[maxIndex] = tmp
    grid_a() # Se llama a la funcion que coloca los autos en pantalla


"""
Funcion grid_a
E: -
S: muestra a los autos en pantalla iterando sobre el grid
R: -
"""
def grid_a():
    # Vacia el frame grid_autos antes de colocar los pilotos
    for widget in grid_autos.winfo_children():
        widget.destroy()

    # Itera sobre las filas del grid, de 0 a 4
    for i in range(5):
        # Crea lables con la informacion de cada automovil usando i como indice para la lista 'autos'
        marca = tk.Label(grid_autos, text=autos[i].marca, font=button_font, bg="tan1")
        modelo = tk.Label(grid_autos, text=autos[i].modelo, font=button_font, bg="tan1")
        temporada = tk.Label(grid_autos, text=autos[i].temporada, font=button_font, bg="tan1")
        eficiencia = tk.Label(grid_autos, text=autos[i].eficiencia, font=button_font, bg="tan1")
        # Coloca las labels en la fila correspondiente al i del momento
        marca.grid(row=i, column=0)
        modelo.grid(row=i, column=1)
        temporada.grid(row=i, column=2)
        eficiencia.grid(row=i, column=3)

    # Se crea y coloca una entry para luego editar algun automovil
    entry = tk.Entry(grid_autos)
    entry.grid(row=2, column=8)

    # Se crea y coloca un boton que llama a la funcion editar_auto con el entry.get()
    editar = tk.Button(grid_autos, text="Editar", font=button_font, bg="sienna3", activebackground="darkorange1",
                       borderwidth=5, relief="ridge", command=lambda: editar_auto(entry.get()))
    editar.grid(row=3, column=8)


"""
Funcion editar
E: j (string)
S: se crea un Toplevel con toda la info del auto seleccionado y mecanismos para editar esta misma
R: el string debe ser un numero entero entre 1 y 5
"""
def editar_auto(j):
    if j.isdigit() and 1 <= int(j) <= 5:
        tkinter.messagebox.showinfo("Ayuda", "Visite la ventana About para conocer más sobre cómo editar correctamente "
                                             "los autos.")
        top = tk.Toplevel(bg="tan1")
        top.title("Editar")
        top.resizable(width=False, height=False)

        i = int(j) - 1  # indice del automovil en la lista 'autos'

        # Se crean labels con toda la info del automovil seleccionado
        label1 = tk.Label(top, text="Marca: " + autos[i].marca, font=small_font, bg="tan1")
        label2 = tk.Label(top, text="Modelo: " +autos[i].modelo, font=small_font, bg="tan1")
        label3 = tk.Label(top, text="País: " + autos[i].pais, font=small_font, bg="tan1")
        label4 = tk.Label(top, text="Temporada: " + str(autos[i].temporada), font=small_font, bg="tan1")
        label5 = tk.Label(top, text="Baterías: " + str(autos[i].cant_baterias), font=small_font, bg="tan1")
        label6 = tk.Label(top, text="Pilas: " + str(autos[i].cant_pilas), font=small_font, bg="tan1")
        label7 = tk.Label(top, text="Tensión: " + str(autos[i].tension), font=small_font, bg="tan1")
        label8 = tk.Label(top, text="Estado: " + str(autos[i].estado), font=small_font, bg="tan1")
        label9 = tk.Label(top, text="Consumo: " + str(autos[i].consumo), font=small_font, bg="tan1")
        #label8 = tk.Label(top, text="Luz: " + str(pilotos[i].cant_fallidas), font=small_font, bg="lightblue")
        label10 = tk.Label(top, text="Nivel batería: " + str(autos[i].nivel_bateria) + "%", font=small_font, bg="tan1")
        label11 = tk.Label(top, text="Peso: " + str(autos[i].peso), font=small_font, bg="tan1")
        label12 = tk.Label(top, text="Eficiencia: " + str(autos[i].eficiencia), font=small_font, bg="tan1")

        # Se colocan las labels
        label1.grid(row=0, column=0)
        label2.grid(row=1, column=0)
        label3.grid(row=2, column=0)
        label4.grid(row=3, column=0)
        label5.grid(row=4, column=0)
        label6.grid(row=5, column=0)
        label7.grid(row=6, column=0)
        label8.grid(row=7, column=0)
        label9.grid(row=8, column=0)
        label10.grid(row=9, column=0)
        label11.grid(row=10, column=0)
        label12.grid(row=11, column=0)

        # Se crea un entry por cada label creado
        entry1 = tk.Entry(top)
        entry2 = tk.Entry(top)
        entry3 = tk.Entry(top)
        entry4 = tk.Entry(top)
        entry5 = tk.Entry(top)
        entry6 = tk.Entry(top)
        entry7 = tk.Entry(top)
        entry8 = tk.Entry(top)
        entry9 = tk.Entry(top)
        entry10 = tk.Entry(top)
        entry11 = tk.Entry(top)
        entry12 = tk.Entry(top)

        # Se colocan las entrys al lado de su label respectiva
        entry1.grid(row=0, column=1)
        entry2.grid(row=1, column=1)
        entry3.grid(row=2, column=1)
        entry4.grid(row=3, column=1)
        entry5.grid(row=4, column=1)
        entry6.grid(row=5, column=1)
        entry7.grid(row=6, column=1)
        entry8.grid(row=7, column=1)
        entry9.grid(row=8, column=1)
        entry10.grid(row=9, column=1)
        entry11.grid(row=10, column=1)
        entry12.grid(row=11, column=1)

        # Se crea un boton por cada entry creado, cada uno llama a la funcion editar_a_aux
        button_top_1 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="sienna3", activebackground="darkorange1",
                                 borderwidth=5, relief="ridge", command=lambda: editar_a_aux(1, i, entry1.get()))
        button_top_2 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="sienna3", activebackground="darkorange1",
                                 borderwidth=5, relief="ridge", command=lambda: editar_a_aux(2, i, entry2.get()))
        button_top_3 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="sienna3", activebackground="darkorange1",
                                 borderwidth=5, relief="ridge", command=lambda: editar_a_aux(3, i, entry3.get()))
        button_top_4 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="sienna3", activebackground="darkorange1",
                                 borderwidth=5, relief="ridge", command=lambda: editar_a_aux(4, i, entry4.get()))
        button_top_5 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="sienna3", activebackground="darkorange1",
                                 borderwidth=5, relief="ridge", command=lambda: editar_a_aux(5, i, entry5.get()))
        button_top_6 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="sienna3", activebackground="darkorange1",
                                 borderwidth=5, relief="ridge", command=lambda: editar_a_aux(6, i, entry6.get()))
        button_top_7 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="sienna3", activebackground="darkorange1",
                                 borderwidth=5, relief="ridge", command=lambda: editar_a_aux(7, i, entry7.get()))
        button_top_8 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="sienna3", activebackground="darkorange1",
                                 borderwidth=5, relief="ridge", command=lambda: editar_a_aux(8, i, entry8.get()))
        button_top_9 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="sienna3", activebackground="darkorange1",
                                 borderwidth=5, relief="ridge", command=lambda: editar_a_aux(9, i, entry9.get()))
        button_top_10 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="sienna3", activebackground="darkorange1",
                                 borderwidth=5, relief="ridge", command=lambda: editar_a_aux(10, i, entry10.get()))
        button_top_11 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="sienna3", activebackground="darkorange1",
                                 borderwidth=5, relief="ridge", command=lambda: editar_a_aux(11, i, entry11.get()))
        button_top_12 = tk.Button(top, text="Editar", font=("Verdana", 10), bg="sienna3", activebackground="darkorange1",
                                 borderwidth=5, relief="ridge", command=lambda: editar_a_aux(12, i, entry12.get()))
        # Se colocan los botones al lado de su entry respectiva
        button_top_1.grid(row=0, column=2)
        button_top_2.grid(row=1, column=2)
        button_top_3.grid(row=2, column=2)
        button_top_4.grid(row=3, column=2)
        button_top_5.grid(row=4, column=2)
        button_top_6.grid(row=5, column=2)
        button_top_7.grid(row=6, column=2)
        button_top_8.grid(row=7, column=2)
        button_top_9.grid(row=8, column=2)
        button_top_10.grid(row=9, column=2)
        button_top_11.grid(row=10, column=2)
        button_top_12.grid(row=11, column=2)
    else:
        # Messagebox de error si no se cumple la restriccion de arriba
        tkinter.messagebox.showerror("Error", "Debe ingresar un entero de 1 a 5")


"""
Funcion editar_a_aux
E: atrib (numero), i (indice), entry
S: segun el atrib, se hace un set del auto en la posicion 'i' con el entry
R: -
"""
def editar_a_aux(atrib, i, entry):
    if atrib == 1:
        autos[i].set_marca(entry)
    elif atrib == 2:
        autos[i].set_modelo(entry)
    elif atrib == 3:
        autos[i].set_pais(entry)
    elif atrib == 4:
        autos[i].set_temporada(entry)
    elif atrib == 5:
        autos[i].set_cant_baterias(entry)
    elif atrib == 6:
        autos[i].set_cant_pilas(entry)
    elif atrib == 7:
        autos[i].set_tension(entry)
    elif atrib == 8:
        autos[i].set_estado(entry)
    elif atrib == 9:
        autos[i].set_consumo(entry)
    elif atrib == 10:
        autos[i].set_nivel_bateria(entry)
    elif atrib == 11:
        autos[i].set_peso(entry)
    else:
        autos[i].set_eficiencia(entry)

"""
Funcion forward
E: pwm 
S: incrementa pwm y luego envia este valor para mover el vehiculo hacia delante
R: -
"""
def forward():
    global pwm
    if pwm <= 0:
        pwm = 100
    elif pwm <= 500:
        pwm += 75
    elif pwm <= 700:
        pwm += 50
    elif pwm <= 950:
        pwm += 25
    else:
        pwm = 1000
    v_pwm.set("PWM:{}".format(pwm))
    myCar.send('pwm:{};'.format(pwm))

"""
Funcion backward
E: pwm
S: disminuye pwm y luego envia este valor para mover el vehiculo hacia atras
R: -
"""
def backward():
    global pwm
    if pwm >= 0:
        pwm = -100
    elif pwm >= -500:
        pwm -= 75
    elif pwm >= -700:
        pwm -= 50
    elif pwm >= -950:
        pwm -= 25
    else:
        pwm = -1000
    v_pwm.set("PWM:{}".format(pwm))
    lback()
    myCar.send('pwm:{};'.format(pwm))

"""
Funcion stop
E: pwm
S: Actualiza pwm a 0 y envia este valor para detener el vehiculo
R: -
"""
def stop():
    global pwm
    if pwm != 0:
        pwm = 0
    myCar.send('pwm:0;')
    lback()
    v_pwm.set("PWM:{}".format(pwm))


"""
Funcion right
E: direc
S: Actualiza direc a 1 y envia este valor para girar el vehiculo a la derecha
R: -
"""
def right():
    global direc
    if direc != 1:
        direc = 1
    myCar.send('dir:1;')

"""
Funcion left
E: direc
S: Actualiza direc a -1 y envia este valor para girar el vehiculo a la izquierda
R: -
"""
def left():
    global direc
    if direc != -1:
        direc = -1
    myCar.send('dir:-1;')

"""
Funcion straight
E: direc
S: Actualiza direc a 0 y envia este valor para no girar el vehiculo
R: -
"""
def straight():
    global direc
    if direc != 0:
        direc = 0
    myCar.send('dir:0;')

"""
Funcion lback
E: luz_tra, pwm
S: Prende o apaga las luces traseras, si pwm es <= 0 siempre estan encendidas
R: -
"""
def lback():
    global luz_tra
    global pwm
    if luz_tra == 0 or pwm <= 0:
        luz_tra = 1
    else:
        luz_tra = 0
    myCar.send('lb:{};'.format(luz_tra))

"""
Funcion lfront
E: luz_fro, ldr
S: Prende o apaga las luces frontales, si ldr es igual a 0 siempre estan encendidas
R: -
"""
def lfront():
    global luz_fro
    global ldr
    if luz_fro == 0 or ldr == 0:
        luz_fro = 1
    else:
        luz_fro = 0
    myCar.send('lf:{};'.format(luz_fro))

"""
Funcion lright
E: luz_der, der_flag 
S: Prende (intermitente) o apaga la luz derecha
R: -
"""
def lright():
    global luz_der
    global der_flag
    while der_flag == True:
        if luz_der == 0:
            luz_der = 1
        else:
            luz_der = 0
        myCar.send('lr:{};'.format(luz_der))
        sleep(1)
    luz_der = 0
    myCar.send('lr:{};'.format(luz_der))
    der_flag = False

"""
Funcion press_lright
E: der_flag
S: Crea un thread que maneja la luz derecha
R: -
"""
def press_lr():
    global der_flag
    if der_flag == False:
        der_flag = True
        lrt = Thread(target=lright)
        lrt.start()

    else:
        der_flag = False

"""
Funcion lleft
E: luz_izq, izq_flag
S: Prende (intermitente) o apaga la luz izquierda
R: -
"""
def lleft():
    global luz_izq
    global izq_flag
    while izq_flag == True:
        if luz_izq == 0:
            luz_izq = 1
        else:
            luz_izq = 0
        myCar.send('ll:{};'.format(luz_izq))
        sleep(1)
    luz_izq = 0
    myCar.send('ll:{};'.format(luz_izq))
    izq_flag = False

"""
Funcion press_ll
E: izq_flag
S: Crea un thread que maneja la luz izquierda
R: -
"""
def press_ll():
    global izq_flag
    if izq_flag == False:
        izq_flag = True
        llt = Thread(target=lleft)
        llt.start()
    else:
        izq_flag = False

"""
Funcion light
E: ldr
S: Manejo manual de light, ya que siempre se mantiene en 1 desde Arduino.
R: -
"""
def light():
    global ldr
    if ldr != 0:
        ldr = 0
        ldr_image.configure(image=ldr_moon)
        ldr_image.image = ldr_moon
    else:
        ldr = 1
        ldr_image.configure(image=ldr_sun)
        ldr_image.image = ldr_sun


"""
Funcion battery
E: Envia un comando para recibir el nivel de bateria actual.
S: Nivel de bateria nuevo
R: -
"""
def battery():
    myCar.send("sense;")
    bat = myCar.read()
    autos[0].set_nivel_bateria(bat)
    if bat <= 30:
        autos[0].set_estado("Descargado")

"""
Funcion celebration
E: pwm
S: Movimiento de celebracion del piloto.
"""
def celebration():
    global pwm
    pwm = 1000
    right()
    forward()
    sleep(2)
    stop()
    sleep(0.1)
    pwm = -1000
    left()
    backward()
    sleep(3)
    stop()
    straight()

"""
Funcion special
E: pwm, dir
S: Movimiento especial del carro.
R: -
"""
def special():
    myCar.send("circle:1;")


# ****************** Frames ******************
root = tk.Tk() # Ventana principial
root.title("Fórmula E-Tec")
root.resizable(False, False)

# ----- MENU -----
menu = tk.Frame(root, width=1000, height=600)  # frame del menu
menu.grid(row=0, column=0)

canvas_menu = tk.Canvas(menu, width=1000, height=600)  # canvas del menu
canvas_menu.place(x=0, y=0)

bg_menu = tk.PhotoImage(file="Images/bg_menu.png")  # fondo del menu
canvas_menu.create_image(500, 300, image=bg_menu)

logo_location = "Images/Logos/" + escud_menu.logo  # logo de la escuderia a mostrar
logo_interfaz = tk.PhotoImage(file=logo_location)
canvas_menu.create_image(500, 300, image=logo_interfaz)

# Botones del menu a diferentes frames
button_menu_1 = tk.Button(menu, text="Mostrar info", font=button_font, bg="orange", activebackground="brown2",
                          borderwidth=5, relief="ridge", command=info_escuderia)
button_menu_2 = tk.Button(menu, text="Editar info", font=button_font, bg="orange", activebackground="brown2",
                          borderwidth=5, relief="ridge", command=editar_escud)
button_menu_3 = tk.Button(menu, text="About", font=button_font, bg="orange", activebackground="brown2",
                          borderwidth=5, relief="ridge", command=ir_a_about)
button_menu_4 = tk.Button(menu, text="Pilotos", font=button_font, bg="orange", activebackground="brown2",
                          borderwidth=5, relief="ridge", command=ir_a_tabla_p)
button_menu_5 = tk.Button(menu, text="Automóviles", font=button_font, bg="orange", activebackground="brown2",
                          borderwidth=5, relief="ridge", command=ir_a_tabla_a)
button_menu_6 = tk.Button(menu, text="Test Drive", font=button_font, bg="orange", activebackground="brown2",
                          borderwidth=5, relief="ridge", command=ir_a_test_drive)
# Se colocan los botones
button_menu_1.place(x=20, y=20)
button_menu_2.place(x=20, y=65)
button_menu_3.place(x=900, y=20)
button_menu_4.place(x=896, y=60)
button_menu_5.place(x=875, y=100)
button_menu_6.place(x=880, y=140)

# ----- ABOUT -----
about = tk.Frame(root, width=1000, height=600) # frame del about

canvas_about = tk.Canvas(about, width=1000, height=600) # canvas del about
canvas_about.place(x=0, y=0)

bg_about = tk.PhotoImage(file="Images/bg_about.png")  # fondo del about
canvas_about.create_image(500, 300, image=bg_about)

dani = tk.PhotoImage(file="Images/dani.png")   # imagen de Dani
canvas_about.create_image(630, 300, image=dani)

jean = tk.PhotoImage(file="Images/jean.png")   # imagen de Jean
canvas_about.create_image(700, 400, image=jean)

# Botones del about (al menu y ayuda)
button_about_1 = tk.Button(about, text="Regresar al Menú", font=button_font, bg="sea green",
                           activebackground="spring green", borderwidth=5, relief="ridge", command=ir_a_menu)
button_about_2 = tk.Button(about, text="Ayuda", font=button_font, bg="sea green", activebackground="spring green",
                           borderwidth=5, relief="ridge", command=ayuda)
# Se colocan los botones
button_about_1.place(x=830, y=10)
button_about_2.place(x=5, y=10)

# Labels del mabout
label_about_1 = tk.Label(about, text="Instituto Tecnológico de Costa Rica", font=button_font, bg="medium sea green")
label_about_2 = tk.Label(about, text="Carrera: Ingeniería en Computadores", font=button_font, bg="medium sea green")
label_about_3 = tk.Label(about, text="Curso: Taller de Programación", font=button_font, bg="medium sea green")
label_about_4 = tk.Label(about, text="Grupo: 01", font=button_font, bg="medium sea green")
label_about_5 = tk.Label(about, text="Profesor: Jeff Schmidt Peralta", font=button_font, bg="medium sea green")
label_about_6 = tk.Label(about, text="Autores", font=button_font, bg="medium sea green")
label_about_7 = tk.Label(about, text="Daniela Brenes Otárola - Carnet: 2019042386", font=button_font, bg="medium sea green")
label_about_8 = tk.Label(about, text="Jean Franco Góndrez Villafuerte - Carnet: 2017111537", font=button_font, bg="medium sea green")
label_about_9 = tk.Label(about, text="País de Producción: Costa Rica", font=button_font, bg="white")
label_about_10 = tk.Label(about, text="Versión 1.0.0", font=button_font, bg="white")
label_about_11 = tk.Label(about, text="hola jeff te quiero mucho", font=("Verdana", 6), bg="white")
# Se colocan las labels
label_about_1.place(x=350, y=30)
label_about_2.place(x=343, y=60)
label_about_3.place(x=370, y=90)
label_about_4.place(x=450, y=120)
label_about_5.place(x=370, y=150)
label_about_6.place(x=460, y=230)
label_about_7.place(x=200, y=300)
label_about_8.place(x=200, y=380)
label_about_9.place(x=0, y=570)
label_about_10.place(x=880, y=570)
label_about_11.place(x=850, y=270)

# ----- TABLA DE PILOTOS -----
tabla_p = tk.Frame(root, bg="lightblue") # frame de la tabla_p

# Botones de la tabla_p (ir al menu, ordenar los pilotos)
button_tabla_p_1 = tk.Button(tabla_p, text="Regresar al Menú", font=button_font, bg="deep sky blue",
                             activebackground="cyan", borderwidth=5, relief="ridge", command=ir_a_menu)
button_tabla_p_2 = tk.Button(tabla_p, text="RGP+", font=button_font, bg="deep sky blue",
                             activebackground="cyan", borderwidth=5, relief="ridge", command=rgp_asc)
button_tabla_p_3 = tk.Button(tabla_p, text="RGP-", font=button_font, bg="deep sky blue",
                             activebackground="cyan", borderwidth=5, relief="ridge", command=rgp_des)
button_tabla_p_4 = tk.Button(tabla_p, text="REP+", font=button_font, bg="deep sky blue",
                             activebackground="cyan", borderwidth=5, relief="ridge", command=rep_asc)
button_tabla_p_5 = tk.Button(tabla_p, text="REP-", font=button_font, bg="deep sky blue",
                             activebackground="cyan", borderwidth=5, relief="ridge", command=rep_des)
# Se colocan los botones
button_tabla_p_1.grid(row=0, column=8)
button_tabla_p_2.grid(row=0, column=0)
button_tabla_p_3.grid(row=0, column=1)
button_tabla_p_4.grid(row=0, column=2)
button_tabla_p_5.grid(row=0, column=3)

# Labels de la tabla_p
label_tabla_p_1 = tk.Label(tabla_p, text="Pos", font=small_font, bg="deepskyblue3")
label_tabla_p_2 = tk.Label(tabla_p, text="Nombre", font=small_font, bg="deepskyblue3")
label_tabla_p_3 = tk.Label(tabla_p, text="Edad", font=small_font, bg="deepskyblue3")
label_tabla_p_4 = tk.Label(tabla_p, text="Nacionalidad", font=small_font, bg="deepskyblue3")
label_tabla_p_5 = tk.Label(tabla_p, text="Temp", font=small_font, bg="deepskyblue3")
label_tabla_p_6 = tk.Label(tabla_p, text="Comp", font=small_font, bg="deepskyblue3")
label_tabla_p_7 = tk.Label(tabla_p, text="RGP", font=small_font, bg="deepskyblue3")
label_tabla_p_8 = tk.Label(tabla_p, text="REP", font=small_font, bg="deepskyblue3")

#Se colocan las labels
label_tabla_p_1.place(x=0, y=40)
label_tabla_p_2.place(x=35, y=40)
label_tabla_p_3.place(x=95, y=40)
label_tabla_p_4.place(x=140, y=40)
label_tabla_p_5.place(x=230, y=40)
label_tabla_p_6.place(x=273, y=40)
label_tabla_p_7.place(x=388, y=40)
label_tabla_p_8.grid(row=1, column=4)


# ----- TABLA DE PILOTOS HIJA -----
grid_pilotos = tk.Frame(tabla_p, bg="lightblue") # frame de la tabla_p hija


# ----- TABLA DE AUTOMOVILES -----
tabla_a = tk.Frame(root, bg="tan1")  # frame de la tabla_a

# Botones de la tabla_a (menu, ordenar autos)
button_tabla_a_1 = tk.Button(tabla_a, text="Regresar al Menú", font=button_font, bg="sienna3",
                             activebackground="darkorange1", borderwidth=5, relief="ridge", command=ir_a_menu)
button_tabla_a_2 = tk.Button(tabla_a, text="Eficiencia+", font=button_font, bg="sienna3",
                             activebackground="darkorange1", borderwidth=5, relief="ridge", command=efic_asc)
button_tabla_a_3 = tk.Button(tabla_a, text="Eficiencia-", font=button_font, bg="sienna3",
                             activebackground="darkorange1", borderwidth=5, relief="ridge", command=efic_des)
# Se colocan los botones
button_tabla_a_1.grid(row=0, column=8)
button_tabla_a_2.grid(row=0, column=0)
button_tabla_a_3.grid(row=0, column=1)

# Labels de la tabla_a
label_tabla_a_1 = tk.Label(tabla_a, text="Marca", font=small_font, bg="indian red")
label_tabla_a_2 = tk.Label(tabla_a, text="Modelo", font=small_font, bg="indian red")
label_tabla_a_3 = tk.Label(tabla_a, text="Temp", font=small_font, bg="indian red")
label_tabla_a_4 = tk.Label(tabla_a, text="Eficiencia", font=small_font, bg="indian red")

# Se colocan las labels
label_tabla_a_1.place(x=25, y=40)
label_tabla_a_2.place(x=170, y=40)
label_tabla_a_3.place(x=270, y=40)
label_tabla_a_4.grid(column=2, row=1)


# ----- TABLA DE AUTOMOVILES HIJA -----
grid_autos = tk.Frame(tabla_a, bg="tan1") # frame de la tabla_a hija

canvas_grid_a = tk.Canvas(grid_autos, width=1000, height=600) # canvas de la tabla_a hija
canvas_grid_a.place(x=0, y=0)


# ----- TEST DRIVE -----
test_drive = tk.Frame(root, width=1000, height=600, bg="hotpink") # frame del test drive

canvas_test_drive = tk.Canvas(test_drive, width=1000, height=600)
canvas_test_drive.place(x=0, y=0)

bg_test = tk.PhotoImage(file="Images/bg_test.png")
canvas_test_drive.create_image(500, 300, image = bg_test)

ldr_sun = tk.PhotoImage(file="Images/ldr_sun.png")
ldr_moon = tk.PhotoImage(file="Images/ldr_moon.png")

#Variable text test drive, se usa para tener texto cambiante en Tkinter
v_pwm = tk.StringVar()
v_pwm.set("PWM:{}".format(pwm))

# Labels del test drive
label_test_1 = tk.Label(test_drive, textvariable=v_pwm, font=small_font, bg="PaleGreen1")
label_test_2 = tk.Label(test_drive, text=pilotos[0].nombre, font=small_font, bg="SteelBlue1")
label_test_3 = tk.Label(test_drive, text=pilotos[0].nacionalidad, font=small_font, bg="SteelBlue1")
label_test_4 = tk.Label(test_drive, text="Bateria:{}%".format(bat), font=small_font, bg="Green")
ldr_image = tk.Label(canvas_test_drive, image=ldr_sun)

# Se colocan las labels
label_test_1.place(x=470, y=400)
label_test_2.place(x=470, y=50)
label_test_3.place(x=470, y=100)
label_test_4.place(x=600, y=50)
ldr_image.place(x=50, y=50)


# Botones del test drive
button_test_1 = tk.Button(test_drive, text="Regresar al menú", font=button_font, command=ir_a_menu)
button_test_2 = tk.Button(test_drive, text="Adelante", font=button_font, command=forward, bg="PaleGreen1")
button_test_3 = tk.Button(test_drive, text="Atras", font=button_font, command=backward, bg="PaleGreen1")
button_test_4 = tk.Button(test_drive, text="Detenerse", font=button_font, command=stop, bg="PaleGreen1")
button_test_5 = tk.Button(test_drive, text="Derecha", font=button_font, command=right, bg="DarkOliveGreen1")
button_test_6 = tk.Button(test_drive, text="Izquierda", font=button_font, command=left, bg="DarkOliveGreen1")
button_test_7 = tk.Button(test_drive, text="Recto", font=button_font, command=straight, bg="DarkOliveGreen1")
button_test_8 = tk.Button(test_drive, text="Luz Frontal", font=button_font, command=lfront, bg="Snow")
button_test_9 = tk.Button(test_drive, text="Luz Trasera", font=button_font, command=lback, bg="Red")
button_test_10 = tk.Button(test_drive, text="Luz Derecha", font=button_font, command=press_lr, bg="Yellow")
button_test_11 = tk.Button(test_drive, text="Luz Izquierda", font=button_font, command=press_ll, bg="Yellow")
button_test_12 = tk.Button(test_drive, text="Dia/Noche", font=button_font, command=light, bg="DeepSkyBlue")
button_test_13 = tk.Button(test_drive, text="Celebracion", font=button_font, command=celebration, bg="Khaki")
button_test_14 = tk.Button(test_drive, text="Movimiento Especial", font=button_font, command=special, bg="Khaki")

# Se colocan los botones
button_test_1.place(x=800, y=10)
button_test_2.place(x=350, y=430)
button_test_3.place(x=470, y=430)
button_test_4.place(x=550, y=430)
button_test_5.place(x=350, y=530)
button_test_6.place(x=450, y=530)
button_test_7.place(x=575, y=530)
button_test_8.place(x=50, y=430)
button_test_9.place(x=50, y=530)
button_test_10.place(x=800, y=430)
button_test_11.place(x=800, y=530)
button_test_12.place(x=150, y=50)
button_test_13.place(x=780, y=200)
button_test_14.place(x=750, y=250)

# Se empieza la ventana de tkinter
root.mainloop()


# ****************** Manejo de archivos de texto ******************
biblia_p = ""   # string para los pilotos

for i in range(10):
    for p in pilotos:
        if p.x == i:  # revisa si el marcador del piloto (nunca cambia) coincide con el i
            # se agregan los datos del piloto
            biblia_p += p.nombre + "*" + str(p.edad) + "*" + p.nacionalidad + "*" + str(p.temporada) + "*" + \
                      str(p.cant_compet) + "*" + str(p.victorias) + "*" + str(p.cant_destacadas) + "*" + str(p.cant_fallidas)
            if i != 9:
                biblia_p += "#" # indica que el piloto termina

atributos_p = open("Archivos de texto/pilotos.txt", "w")  # Se abre el archivo para escribir en el
atributos_p.write(biblia_p)  # Se escribe la info de todos los pilotos
atributos_p.close()  # Se cierra el archivo


biblia_a = ""  # string para los automoviles
for i in range(5):
    for a in autos:
        if a.x == i:  # revisa si el marcador del automovil (nunca cambia) coincide con el i
            # se agregan los datos del automovil
            biblia_a += a.marca + "*" + a.modelo + "*" + a.pais + "*" + str(a.temporada) + "*" + str(a.cant_baterias) +\
                        "*" + str(a.cant_pilas) + "*" + str(a.tension) + "*" + a.estado + "*" + str(a.consumo) + "*" + \
                        str(a.nivel_bateria) + "*" + str(a.peso) + "*" + str(a.eficiencia)
            if  i != 4:
                biblia_a += "#" # indica que el automovil termina

atributos_a = open("Archivos de texto/autos.txt", "w")  # Se abre el archivo para escribir en el
atributos_a.write(biblia_a) # Se escribe la info de todos los autos
atributos_a.close()  # Se cierra el archivo