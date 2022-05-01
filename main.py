import sys
import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import webbrowser
from Lexico import Analizador
from Sintactico import Sintactico
from Tabla import Tablita, Tablita_1
from TypeToken import TypeToken
from ayuda import lectura



def salir_interfaz():
    sys.exit()


def buscar_usu():
    webbrowser.open('Manual de Usuario.pdf') 
    print("Manual de Usuarios")

def buscar_tec():
    webbrowser.open('Manual Tecnico.pdf') 
    print("Manual Técnico")


def enviar_men():
    aux = lectura()
    texto = textt1.get(1.0,'end')
    textt.insert(tk.INSERT,texto)
    textt2.insert(tk.INSERT,texto)
    lexico = Analizador(texto)
    lexico.ImprimirTo()
    lexico.ImprimirEr()
    sintactico = Sintactico(lexico.tokens)
    for j in range(len(lexico.tokens)):
        if lexico.tokens[j].tipo == TypeToken.RESULTADO.name:
            cadena1= str(lexico.tokens[j+1].lexema)
            cadena2= str(lexico.tokens[j+3].lexema)
            cadena3 = str(lexico.tokens[j+5].lexema)
            for k in range(len(aux)):
                if str(aux[k].temporada) == cadena3:
                    if str(aux[k].local) == cadena1 and str(aux[k].visitante)==cadena2:
                        textt.insert(tk.INSERT,"El resultado de este partido fue: "+cadena1+" "+str(aux[k].mar_l) + " VS "+cadena2+" "+str(aux[k].mar_v)+"\n")
        if lexico.tokens[j].tipo == TypeToken.JORNADA.name:
            cadena1 = str(lexico.tokens[j+1].lexema)
            cadena2 = str(lexico.tokens[j+3].lexema)
            archivo = str(lexico.tokens[j+5].lexema)
            textt.insert(tk.INSERT,"Generando archivo de resultados jornada: "+cadena1+" Temporada: "+ cadena2)
            f = open(archivo+'.html','w')
            f.write("<!doctype html>")
            f.write("<html lang=\"en\">")
            f.write("<head>")
            f.write("<!-- Required meta tags -->")
            f.write(" <meta charset=\"utf-8\">")
            f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
            f.write("<!-- Bootstrap CSS -->")
            f.write("<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We\" crossorigin=\"anonymous\">")
            f.write("<title>Reporte Jornada</title>")
            f.write("<style>table, th, td {border: 1px solid black; text-align: center}""</style>")
            f.write("</head>")
            f.write("<body>")
            f.write("<H1 style=\"color:white; background-color:teal\">\n<center> REPORTE JORNADA</center>\n</H1>\n")
            f.write("<h3>Roberto Gómez - 202000544</h3>")
            f.write("<center><table><tr><th>Posicion</th><th>Temporada</th><th>Local</th><th>Marcador Local</th><th>Visitante</th><th>Marcador Visitante</th></tr>")
            k=1
            for x in range(len(aux)):
                if str(aux[x].temporada) == cadena2:
                    if str(aux[x].jornada) == cadena1:
                        f.write("<tr class=\"table-primary\">")
                        f.write("<center><td><h4>"+ str(k) +"</h4></td>"+"<td><h4>" +str(aux[x].fecha) +"</h4></td>"+"<td><h4>"+ str(aux[x].local)+"</h4></td>"+"<td><h4>"+ str(aux[x].mar_l)+"</h4></td>"+ "<td><h4>"+str(aux[x].visitante)+"</h4></td>"+ "<td><h4>"+str(aux[x].mar_v)+"</h4></td></center>")
                        f.write("</tr>")
                k+=1
            f.write("</table></center>")
            f.write("<!-- Optional JavaScript; choose one of the two! -->")
            f.write("<tr class=\"table-primary\">")
            f.write(" <!-- Option 1: Bootstrap Bundle with Popper -->")
            f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj\" crossorigin=\"anonymous\"></script>")
            f.write("<!-- Option 2: Separate Popper and Bootstrap JS -->")
            f.write(" <!--")
            f.write("<script src=\"https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js\" integrity=\"sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp\" crossorigin=\"anonymous\"></script>")
            f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js\" integrity=\"sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/\" crossorigin=\"anonymous\"></script>")
            f.write("-->")
            f.write("</body>")
            f.write("</html>")
            f.close()
        if lexico.tokens[j].tipo == TypeToken.GOLES.name:
            c =str(lexico.tokens[j+1].lexema)
            cadena1 = str(lexico.tokens[j+2].lexema)
            cadena2= str(lexico.tokens[j+4].lexema)
            if c == "LOCAL":
                total = 0
                for i in range(len(aux)):
                    if str(aux[i].temporada) == cadena2:
                        if cadena1 == str(aux[i].local):
                            total += int(aux[i].mar_l)
                textt.insert(tk.INSERT,"Los goles anotados por el: "+cadena1+" del local en la temporada: "+cadena2+" fueron: "+str(total)+"\n")
            if c == "VISITANTE":
                total = 0
                for i in range(len(aux)):
                    if str(aux[i].temporada) == cadena2:
                        if cadena1 == str(aux[i].visitante):
                            total += int(aux[i].mar_v)
                textt.insert(tk.INSERT,"Los goles anotados por el: "+cadena1+" del vistante en la temporada: "+cadena2+" fueron: "+str(total)+"\n")
            if c == "TOTAL":
                total = 0
                total1=0
                for i in range(len(aux)):
                    if str(aux[i].temporada) == cadena2:
                        if cadena1 == str(aux[i].local):
                            total += int(aux[i].mar_l)
                        elif cadena1 == str(aux[i].visitante):
                            total1 += int(aux[i].mar_v) 
                textt.insert(tk.INSERT,"Los goles anotados por el: "+cadena1+" en total en la temporada: "+cadena2+" fueron: "+str(total+total1)+"\n")
        if lexico.tokens[j].tipo == TypeToken.PARTIDOS.name:
            cadena1= str(lexico.tokens[j+1].lexema)
            cadena2= str(lexico.tokens[j+3].lexema)
            archivo = str(lexico.tokens[j+5].lexema)
            j_i = int(lexico.tokens[j+7].lexema)
            j_f=int(lexico.tokens[j+9].lexema)
            textt.insert(tk.INSERT,"Generando archivo de resultados del: "+cadena1+" temporada: "+cadena2+ " Jornada Inicial: "+str(j_i)+" Jornada Final: " + str(j_f)+"\n")
            f = open(archivo+'.html','w')
            f.write("<!doctype html>")
            f.write("<html lang=\"en\">")
            f.write("<head>")
            f.write("<!-- Required meta tags -->")
            f.write(" <meta charset=\"utf-8\">")
            f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
            f.write("<!-- Bootstrap CSS -->")
            f.write("<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We\" crossorigin=\"anonymous\">")
            f.write("<title>Reporte Partidos</title>")
            f.write("<style>table, th, td {border: 1px solid black; text-align: center}""</style>")
            f.write("</head>")
            f.write("<body>")
            f.write("<H1 style=\"color:white; background-color:teal\">\n<center> REPORTE PARTIDOS</center>\n</H1>\n")
            f.write("<h3>Roberto Gómez - 202000544</h3>")
            f.write("<center><table><tr><th>Posicion</th><th>Local</th><th>Marcador Local</th><th>Visitante</th><th>Marcador Visitante</th></tr>")
            k=1
            for x in range(len(aux)):
                if str(aux[x].temporada) == cadena2:
                    if int(aux[x].jornada) >= j_i and int(aux[x].jornada) <= j_f:
                        if str(aux[x].local) == cadena1:
                            f.write("<tr class=\"table-primary\">")
                            f.write("<center><td><h4>"+ str(k) +"</h4></td>"+"<td><h4>" +cadena1 +"</h4></td>"+"<td><h4>"+ str(aux[x].mar_l)+"</h4></td>"+"<td><h4>"+str(aux[x].visitante)+"</h4></td>"+ "<td><h4>"+str(aux[x].mar_v)+"</h4></td></center>")
                            f.write("</tr>")
                        if str(aux[x].visitante) == cadena1:
                            f.write("<tr class=\"table-primary\">")
                            f.write("<center><td><h4>"+ str(k) +"</h4></td>"+"<td><h4>" +str(aux[x].local) +"</h4></td>"+"<td><h4>"+ str(aux[x].mar_l)+"</h4></td>"+"<td><h4>"+cadena1+"</h4></td>"+ "<td><h4>"+str(aux[x].mar_v)+"</h4></td></center>")
                            f.write("</tr>")
                k+=1
            f.write("</table></center>")
            f.write("<!-- Optional JavaScript; choose one of the two! -->")
            f.write("<tr class=\"table-primary\">")
            f.write(" <!-- Option 1: Bootstrap Bundle with Popper -->")
            f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj\" crossorigin=\"anonymous\"></script>")
            f.write("<!-- Option 2: Separate Popper and Bootstrap JS -->")
            f.write(" <!--")
            f.write("<script src=\"https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js\" integrity=\"sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp\" crossorigin=\"anonymous\"></script>")
            f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js\" integrity=\"sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/\" crossorigin=\"anonymous\"></script>")
            f.write("-->")
            f.write("</body>")
            f.write("</html>")
            f.close()
        if lexico.tokens[j].tipo == TypeToken.TABLA_TEM.name:
            cadena2=str(lexico.tokens[j+2].lexema)
            archivo = str(lexico.tokens[j+4].lexema)
            a = []
            aux_equipo=[]
            total = []
            tabla=[]
            textt.insert(tk.INSERT,"Generando archivo de clasificacion de temporada: "+cadena2+"\n")
            f = open(archivo+'.html','w')
            f.write("<!doctype html>")
            f.write("<html lang=\"en\">")
            f.write("<head>")
            f.write("<!-- Required meta tags -->")
            f.write(" <meta charset=\"utf-8\">")
            f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
            f.write("<!-- Bootstrap CSS -->")
            f.write("<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We\" crossorigin=\"anonymous\">")
            f.write("<title>Reporte Temporada</title>")
            f.write("<style>table, th, td {border: 1px solid black; text-align: center}""</style>")
            f.write("</head>")
            f.write("<body>")
            f.write("<H1 style=\"color:white; background-color:teal\">\n<center> REPORTE TEMPORADA</center>\n</H1>\n")
            f.write("<h3>Roberto Gómez - 202000544</h3>")
            f.write("<center><table><tr><th>Posicion</th><th>Equipo</th><th>Puntaje</th></tr>")
            k=1
            for x in range(len(aux)):
                if str(aux[x].temporada) == cadena2:
                    if int(aux[x].mar_l) > int(aux[x].mar_v):
                        a.append(Tablita(aux[x].local,3))
                        a.append(Tablita(aux[x].visitante,0))
                    elif int(aux[x].mar_l) < int(aux[x].mar_v):
                        a.append(Tablita(aux[x].local,0))
                        a.append(Tablita(aux[x].visitante,3))
                    elif int(aux[x].mar_l) == int(aux[x].mar_v):
                        a.append(Tablita(aux[x].local,1))
                        a.append(Tablita(aux[x].visitante,1))

                    aux_equipo.append(aux[x].local)
            a.sort(key=lambda x:x.equipo, reverse=False)
            for bb in aux_equipo:
                if bb not in total:
                    total.append(bb)
            total.sort()
            suma = []       
            for x in total:
                for k in range(len(a)):
                    if x == str(a[k].equipo):
                        suma.append(a[k].puntos)
                        suma1 = sum(suma)
                    else:
                        
                        suma.clear() 
                tabla.append(Tablita_1(x,suma1))
            tabla.sort(key=lambda x:x.puntos, reverse=True)
            for i in range(len(tabla)):
                f.write("<tr class=\"table-primary\">")
                f.write("<center><td><h4>"+ str(i) +"</h4></td>"+"<td><h4>" +str(tabla[i].equipo) +"</h4></td>"+"<td><h4>"+ str(tabla[i].puntos)+"</h4></td></center>")
                f.write("</tr>")
            f.write("</table></center>")
            f.write("<!-- Optional JavaScript; choose one of the two! -->")
            f.write("<tr class=\"table-primary\">")
            f.write(" <!-- Option 1: Bootstrap Bundle with Popper -->")
            f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj\" crossorigin=\"anonymous\"></script>")
            f.write("<!-- Option 2: Separate Popper and Bootstrap JS -->")
            f.write(" <!--")
            f.write("<script src=\"https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js\" integrity=\"sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp\" crossorigin=\"anonymous\"></script>")
            f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js\" integrity=\"sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/\" crossorigin=\"anonymous\"></script>")
            f.write("-->")
            f.write("</body>")
            f.write("</html>")
            f.close()
        
        if lexico.tokens[j].tipo == TypeToken.TOP.name:
            l = 0
            v = 0
            total = 0
            c = str(lexico.tokens[j+1].lexema)
            cadena2 = str(lexico.tokens[j+3].lexema)
            cadena4 = int(lexico.tokens[j+5].lexema)
            a = []
            aux_equipo=[]
            total = []
            tabla=[]
            textt.insert(tk.INSERT,"Se generara un archivo top "+c+" Temporada "+cadena2)
            f = open('Top.html','w')
            f.write("<!doctype html>")
            f.write("<html lang=\"en\">")
            f.write("<head>")
            f.write("<!-- Required meta tags -->")
            f.write(" <meta charset=\"utf-8\">")
            f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
            f.write("<!-- Bootstrap CSS -->")
            f.write("<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We\" crossorigin=\"anonymous\">")
            f.write("<title>Reporte Top</title>")
            f.write("<style>table, th, td {border: 1px solid black; text-align: center}""</style>")
            f.write("</head>")
            f.write("<body>")
            f.write("<H1 style=\"color:white; background-color:teal\">\n<center> REPORTE TOP</center>\n</H1>\n")
            f.write("<h3>Roberto Gómez - 202000544</h3>")
            f.write("<center><table><tr><th>Posicion</th><th>Equipo</th><th>Punteo</th></tr>")
            k=1
            for x in range(len(aux)):
                if str(aux[x].temporada) == cadena2:
                    if int(aux[x].mar_l) > int(aux[x].mar_v):
                        a.append(Tablita(aux[x].local,3))
                        a.append(Tablita(aux[x].visitante,0))
                    elif int(aux[x].mar_l) < int(aux[x].mar_v):
                        a.append(Tablita(aux[x].local,0))
                        a.append(Tablita(aux[x].visitante,3))
                    elif int(aux[x].mar_l) == int(aux[x].mar_v):
                        a.append(Tablita(aux[x].local,1))
                        a.append(Tablita(aux[x].visitante,1))
                    aux_equipo.append(aux[x].local)

            a.sort(key=lambda x:x.equipo, reverse=False)
            for bb in aux_equipo:
                if bb not in total:
                    total.append(bb)
            total.sort()
            suma = []       
            for x in total:
                for k in range(len(a)):
                    if x == str(a[k].equipo):
                        suma.append(a[k].puntos)
                        suma1 = sum(suma)
                    else:
                        
                        suma.clear() 
                tabla.append(Tablita_1(x,suma1))
            if c == "SUPERIOR":
                tabla.sort(key=lambda x:x.puntos, reverse=True)
                for z in range(cadena4):
                    f.write("<tr class=\"table-primary\">")
                    f.write("<center><td><h4>"+ str(z) +"</h4></td>"+"<td><h4>" +str(tabla[z].equipo) +"</h4></td>"+"<td><h4>"+ str(tabla[z].puntos)+"</h4></td></center>")
                    f.write("</tr>")
                f.write("</table></center>")
                f.write("<!-- Optional JavaScript; choose one of the two! -->")
                f.write("<tr class=\"table-primary\">")
                f.write(" <!-- Option 1: Bootstrap Bundle with Popper -->")
                f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj\" crossorigin=\"anonymous\"></script>")
                f.write("<!-- Option 2: Separate Popper and Bootstrap JS -->")
                f.write(" <!--")
                f.write("<script src=\"https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js\" integrity=\"sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp\" crossorigin=\"anonymous\"></script>")
                f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js\" integrity=\"sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/\" crossorigin=\"anonymous\"></script>")
                f.write("-->")
                f.write("</body>")
                f.write("</html>")
                f.close()
            if c == "INFERIOR":
                tabla.sort(key=lambda x:x.puntos, reverse=False)
                for z in range(cadena4):
                    f.write("<tr class=\"table-primary\">")
                    f.write("<center><td><h4>"+ str(z) +"</h4></td>"+"<td><h4>" +str(tabla[z].equipo) +"</h4></td>"+"<td><h4>"+ str(tabla[z].puntos)+"</h4></td></center>")
                    f.write("</tr>")
                f.write("</table></center>")
                f.write("<!-- Optional JavaScript; choose one of the two! -->")
                f.write("<tr class=\"table-primary\">")
                f.write(" <!-- Option 1: Bootstrap Bundle with Popper -->")
                f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj\" crossorigin=\"anonymous\"></script>")
                f.write("<!-- Option 2: Separate Popper and Bootstrap JS -->")
                f.write(" <!--")
                f.write("<script src=\"https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js\" integrity=\"sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp\" crossorigin=\"anonymous\"></script>")
                f.write("<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js\" integrity=\"sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/\" crossorigin=\"anonymous\"></script>")
                f.write("-->")
                f.write("</body>")
                f.write("</html>")
                f.close()
        if lexico.tokens[j].tipo == TypeToken.ADIOS.name:
            messagebox.showinfo(message="ADIOS",title="Despedida")
            sys.exit()

def report_error():
    texto = textt2.get(1.0,'end')
    lexico = Analizador(texto)
    lexico.reporteErorres()

def log_error():
    texto = textt1.get(1.0,'end')
    lexico = Analizador(texto)
    lexico.Limpiar_Error()
    textt2.delete(1.0,'end')

def log_token():
    texto = textt1.get(1.0,'end')
    lexico = Analizador(texto)
    lexico.Limpiar_Token()
    textt2.delete(1.0,'end')

def boton_cargaArchivo_command():
    textt1.delete(1.0,'end')

def report_token():
    texto = textt2.get(1.0,'end')
    lexico = Analizador(texto)
    lexico.reporteTokens()

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

textt2 = tk.Text(root)
textt2["font"] = fuente
textt2.place(x=955,y=525,width= 550, height=40)

cArchivo=tk.Button(root)
cArchivo["font"] = fuente
cArchivo["justify"] = "center"
cArchivo["text"] = "Borrar"
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
#limpiar_tok["command"] = guardar_Archivo 

reporte_t=tk.Button(root)
reporte_t["font"] = fuente
reporte_t["justify"] = "center"
reporte_t["text"] = "Reporte de tokens"
reporte_t.place(x=640,y=240,width=140,height=50)
reporte_t["command"] = report_token 

limpiar_err=tk.Button(root)
limpiar_err["font"] = fuente
limpiar_err["justify"] = "center"
limpiar_err["text"] = "Limpiar Log Errores"
limpiar_err.place(x=640,y=170,width=140,height=50)
#limpiar_err["command"] = guardar_Archivo 

reporte_e=tk.Button(root)
reporte_e["font"] = fuente
reporte_e["justify"] = "center"
reporte_e["text"] = "Reporte de errores"
reporte_e.place(x=640,y=100,width=140,height=50)
reporte_e["command"] = report_error 

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
