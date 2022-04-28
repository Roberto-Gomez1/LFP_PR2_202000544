import sys
import csv
from Obj import Obj
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
import webbrowser
from Lexico import Analizador
from Sintactico import Sintactico

def boton_cargaArchivo_command():
    data = []
    with open('LaLigaBot-LFP.csv') as a:
        reader = csv.reader(a)
        for aa in reader:
            data.append(Obj(aa[0],aa[1],aa[2],aa[3],aa[4],aa[5],aa[6]))
        print(repr(data))

def salir_interfaz():
    sys.exit()


def buscar_usu():
    webbrowser.open('Manual de Usuario.pdf') 
    print("Manual de Usuarios")

def buscar_tec():
    webbrowser.open('Manual Tecnico.pdf') 
    print("Manual Técnico")

def guardar_Archivo():
    Tk().withdraw()
    filedir = filedialog.askopenfilename(filetypes=[("Archivo data","*.form")])
    texto = textt.get(1.0,'end')
    with open(filedir,"r+",encoding = "utf-8") as f:
        f.truncate(0)
        f.write(texto)

def enviar_men():
    texto = textt1.get(1.0,'end')
    textt1.delete(1.0,'end')
    textt.insert(tk.INSERT,texto)
    lexico = Analizador(texto)
    lexico.Imprimir()
    lexico.ImprimirErrores()
    sintactico = Sintactico(lexico.tokens)
    

root =Tk()
root.title('Menu')
fuente = tkFont.Font(family='Arial', size = 12)

fram = ttk.Frame(root)
framee = ttk.Frame(fram, width=800, height=600)


textt = tk.Text(root)
textt["font"] = fuente
textt.place(x=75,y=75,width= 550, height=440)

textt.insert(tk.INSERT, "Bienvenido a la Liga Bot, Ingrese un comando\n")

textt1 = tk.Text(root)
textt1["font"] = fuente
textt1.place(x=75,y=525,width= 550, height=40)

cArchivo=tk.Button(root)
cArchivo["font"] = fuente
cArchivo["justify"] = "center"
cArchivo["text"] = "Analizar"
cArchivo.place(x=75,y=10,width=140,height=50)
cArchivo["command"] = boton_cargaArchivo_command 

salir = tk.Button(root)
salir["font"] = fuente
salir["justify"] = "center"
salir["text"] = "Salir del Sistema"
salir.place(x=640,y=10,width=140,height=50)
salir["command"] = salir_interfaz 

label = tk.Label(root)
label["font"] = fuente
label["justify"] = "center"
label["text"] = "Opciones"
label.place(x=680,y=70,width= 70, height=20)


limpiar_tok=tk.Button(root)
limpiar_tok["font"] = fuente
limpiar_tok["justify"] = "center"
limpiar_tok["text"] = "Limpiar Log Tokens"
limpiar_tok.place(x=640,y=310,width=140,height=50)
limpiar_tok["command"] = guardar_Archivo 

reporte_t=tk.Button(root)
reporte_t["font"] = fuente
reporte_t["justify"] = "center"
reporte_t["text"] = "Reporte de tokens"
reporte_t.place(x=640,y=240,width=140,height=50)
reporte_t["command"] = guardar_Archivo 

limpiar_err=tk.Button(root)
limpiar_err["font"] = fuente
limpiar_err["justify"] = "center"
limpiar_err["text"] = "Limpiar Log Errores"
limpiar_err.place(x=640,y=170,width=140,height=50)
limpiar_err["command"] = guardar_Archivo 

reporte_e=tk.Button(root)
reporte_e["font"] = fuente
reporte_e["justify"] = "center"
reporte_e["text"] = "Reporte de errores"
reporte_e.place(x=640,y=100,width=140,height=50)
reporte_e["command"] = guardar_Archivo 

generar=tk.Button(root)
generar["font"] = fuente
generar["justify"] = "center"
generar["text"] = "Manual de Usuario"
generar.place(x=640,y=450,width=140,height=50)
generar["command"] = buscar_usu 


generar2=tk.Button(root)
generar2["font"] = fuente
generar2["justify"] = "center"
generar2["text"] = "Manual Tecnico"
generar2.place(x=640,y=380,width=140,height=50)
generar2["command"] = buscar_tec 

enviar=tk.Button(root)
enviar["font"] = fuente
enviar["justify"] = "center"
enviar["text"] = "Enviar"
enviar.place(x=640,y=520,width=140,height=50)
enviar["command"] =enviar_men


fram.pack()
framee.pack()


root.mainloop()
