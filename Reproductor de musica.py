# !/usr/bin/python
# -*- coding: UTF-8 -*-

#Library call
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from mutagen.mp3 import MP3
from PIL import Image,ImageTk
import pygame as py
import os.path
import glob


# Definición de ventana
window = tk.Tk()
window.title("Basado en Python tkinter Mp3 Player 1.0")
window.geometry("820x550")
window.attributes("-alpha",0.91)
window.iconbitmap("album_72px_1181645_easyicon.net.ico")

# Importar por lotes canciones locales
realpath = os.path.realpath(__file__) # Camino absoluto actual
dirname = os.path.dirname(realpath)
extension = 'mp3'
file_list = glob.glob('*.'+extension) #Volver a una lista
#playlist
aulist = []
aulist.extend(file_list) #Stitching to playlist
print(aulist)
#Lista de duración de la canción
aulen = []
for tik in range(len(aulist)):    
    audio = MP3(aulist[tik])
    aulen.append(audio.info.length)
print(aulen)


#ilustración
im1=Image.open("Gramophone.jpg")
im1 = im1.resize((400,400))
img1=ImageTk.PhotoImage(im1)
imLabel1=tk.Label(window,image=img1,height=400, width=500).pack()
im2=Image.open("welcome.gif")
im2 = im2.resize((200,50))
img2=ImageTk.PhotoImage(im2)
imLabel2=tk.Label(window,image=img2,width=200, height=40 ).place(x=615,y=1)


# Visualización de lista de reproducción
scr1 = scrolledtext.ScrolledText(window, bg="white", width=18, height=10,font=("Times New Roman",13))
# Cuadro de texto desplazable (ancho, alto (el alto debe ser el número de líneas), estilo de fuente)
scr1.place(x=0, y=0) # Desplazamiento de la posición del cuadro de texto en la página
for num in range(len(aulist)):
    scr1.insert(tk.INSERT, '\n%d. %s\n' % (num+1, aulist[num]))
scr2 = scrolledtext.ScrolledText(window, bg="white", width=18, height=15,font=("Times New Roman",13))
scr2.insert(tk.INSERT, 'Reproducir registro: \ n'  )
scr2.place(x=0, y=220)
#Opciones desplegables
cmb = ttk.Combobox(window, width=22)
cmb['value'] = aulist
cmb.current(0)
cmb.place(x=629,y=50)

def re_set():
    delete_it()
    realpath = os.path.realpath(__file__)  # Ruta absoluta actual
    dirname = os.path.dirname(realpath)
    extension = 'mp3'
    file_list = glob.glob('*.' + extension)  # Devolver una lista
    # lista de reproducción
    global aulist
    aulist = []
    aulist.extend(file_list)  # Empalme a lista de reproducción
    for k in range(len(aulist)):
        scr1.insert(tk.INSERT, '\n%s:\n'%aulist[k])
    print("¡Reimportación exitosa!",aulist)


#Variables globales
count = 0
flag = False
#Función principal #Play
def replay():
    # Inicialización
    py.mixer.init()
    # Carga de archivos
    global count
    global flag
    if len(aulist) == 0:
        flag = True
    if flag == False:
        flag = True
        # Reproducir El primero es el valor de reproducción: -1 significa que el single actual se reproduce en un bucle, y el segundo parámetro significa el tiempo para comenzar a reproducir.
        py.mixer.music.load(aulist[count])
        py.mixer.music.play(-1, 0.3)
        scr2.insert(tk.INSERT, '%s\n\n' % aulist[count])
        print("Jugando ahora:", aulist[count])
    else:
        flag = False
        py.mixer.music.pause()

#Realize reencarnation cut song
def last_one():
    global count
    global flag
    if count != 0:
        count -= 1
        flag = False
        replay()
    else:
        flag = False
        count = len(aulist)-1
        replay()


def next_one():
    global count
    global flag
    if count != len(aulist)-1:
        count += 1
        flag = False
        replay()
    else:
        flag = False
        count = 0
        replay()


hit_it = False
def pause():
    global hit_it
    if hit_it == False:
        hit_it = True
        py.mixer.music.pause()
    else:
        hit_it = False
        py.mixer.music.unpause()


# Control de barra de progreso 1
scale1 = tk.Scale(window, from_=0, to=int(max(aulen)), orient='horizonta', tickinterval=50, length=400)
scale1.place(x=208, y=405)
def jump_to1():
    global count
    py.mixer.init()
    py.mixer.music.load(aulist[count])
    py.mixer.music.play(-1, scale1.get())
    print("Saltar a:% d segundos"%scale1.get()) # Superar la duración de la canción actual se reproduce automáticamente desde el principio


#List elige cortar canción
def sel_t():
    global count
    py.mixer.init()
    for num in range(len(aulist)):
        if cmb.get() == aulist[num]:
            count = num
    py.mixer.music.load(aulist[count])
    py.mixer.music.play(-1, 0.3)
    scr2.insert(tk.INSERT, '%s\n\n' % aulist[count])
    print("Reproduciendo actualmente:% s"%cmb.get())


#Lista de reproducción personalizada
scr3 = scrolledtext.ScrolledText(window, bg="white", width=18, height=18,font=("Times New Roman",13))
scr3.place(x=625, y=130)


#Añadir a lista personalizada
def add_to():
    global aulist
    scr3.insert(tk.INSERT, "%s\n\n"%cmb.get())
    aulist.append(cmb.get())
    scr1.insert(tk.INSERT, "\n%s\n"%cmb.get())
    print("¡Agregado exitosamente!", aulist)


#etiqueta
text1 = tk.Text(window, bg = 'white', width=23,height=1)
text1.insert(tk.INSERT, "Mi lista de reproducción") #INSERT índice indica la posición actual del cursor de inserción
text1.place(x=0, y=0)
text2 = tk.Text(window, bg = '#CCCCFF', width=14,height=1)
text2.insert(tk.INSERT, "Lista de reproducción personalizada") #INSERT índice indica la posición actual del cursor de inserción
text2.place(x=660, y=110)


def delete_it():
    global aulist
    global count
    count = 0
    aulist = []
    scr1.delete('1.0','end')
    scr3.delete('1.0', 'end')
    print("¡La biblioteca de música se ha vaciado!")


# Diseño de control
photo1 = tk.PhotoImage(file='play.gif')
btn1 = tk.Button(window, text="Jugar", font = ("Clásico Yahei", 12), image=photo1, height=50, width=50, bg="#66CCFF", command = replay)
btn1.place(x=380,y=470)
photo2 = tk.PhotoImage(file='last.gif')
btn2 = tk.Button(window, text="Anterior",image = photo2,height=30, width=30, bg="#33CCFF", anchor='center', command = last_one)
btn2.place(x=320,y=480)
photo3 = tk.PhotoImage(file='next.gif')
btn3 = tk.Button(window, text="siguiente canción",image = photo3,height=30, width=30, bg="#00CCFF", command = next_one)
btn3.place(x=455,y=480)
btn4 = tk.Button(window, text="se acabó el tiempo", font = ("Clásico Yahei", 10), height=1, width=3, bg="#00CCFF", command = pause)
btn4.place(x=510,y=485)
btn5 = tk.Button(window, text="Pasemos a", font = ("Clásico Yahei", 10), height=1, width=3, bg="#00CCFF", command =jump_to1)
btn5.place(x=270,y=485)
btn6 = tk.Button(window, text="Seleccione", font = ("Clásico Yahei", 10), height=1, width=3, bg="white", command =sel_t)
btn6.place(x=695,y=80)
btn7 = tk.Button(window, text="Añadir", font = ("Clásico Yahei", 10), height=1, width=3, bg="#CCCCFF", command =add_to)
btn7.place(x=640,y=485)
btn8 = tk.Button(window, text="Restablecer biblioteca musical", font = ("Clásico Yahei", 10), height=1, width=7, bg="#CCCCFF", command =delete_it)
btn8.place(x=700,y=485)
btn9 = tk.Button(window, text="Actualizar biblioteca musical", font = ("Clásico Yahei", 10), height=1, width=7, bg="#CCCCFF", command =re_set)
btn9.place(x=50,y=515)

window.mainloop()

