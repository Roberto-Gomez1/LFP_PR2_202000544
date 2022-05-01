from Token import Token
from TypeToken import TypeToken
from tkinter import messagebox
import webbrowser

class Analizador:
    tipo = TypeToken.DESCONOCIDO
    lexema = ''
    tokens= []
    estado = 1
    fila = 1
    columna = 0
    generar = False
    def __init__(self, entrada):
        self.estado = 1
        self.lexema = ''
        self.tokens = []
        self.fila = 1
        self.columna = 0
        self.generar = True
        tipos = Token("lexema", -1, -1, -1)

        entrada = entrada + '#'
        actual = ''
        longitud = len(entrada)

        for i in range(longitud):
            actual = entrada[i]
            
            if self.estado == 1:
                if actual.isalpha():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual.isdigit():
                    self.estado = 4
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual == "<":
                    self.estado = 5
                    self.columna += 1
                    #self.lexema += actual
                    continue
                elif actual == "-":
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual == '"':
                    self.estado = 3
                    self.columna += 1
                    #self.lexema += actual
                    continue
                elif actual == ' ':
                    self.columna +=1
                    self.estado = 1
                elif actual == '\n':
                    self.fila += 1
                    self.estado = 1
                    self.columna = 1
                elif actual =='\r':
                    self.estado = 1
                elif actual == '\t':
                    self.columna += 5
                    self.estado = 1
                elif actual == '#' and i ==longitud - 1:
                    print('Analisis terminado')
                else:
                    self.lexema += actual
                    self.AgregarToken(TypeToken.DESCONOCIDO.name)
                    self.columna += 1
                    self.generar = False
                
            
            elif self.estado == 2:
                if actual.isalpha():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    continue
                else:
                    if self.Reservada():
                        self.AgregarToken(self.tipo.name)
                        i -= 1
                        continue
                    else:
                        self.AgregarToken(TypeToken.PALABRAS.name)
                        i -= 1
                        continue   

            elif self.estado == 3:
                if actual != '"':
                    self.estado = 3
                    self.columna += 1
                    self.lexema += actual
                    continue
                elif actual == '"':
                    self.estado = 4
                    self.columna += 1
                    #self.lexema += actual
                    self.AgregarToken(TypeToken.CADENA.name)
                    continue
            if self.estado == 5:
                if actual != ">":
                    self.estado = 5
                    self.columna += 1
                    self.lexema += actual
                elif actual == ">":
                    self.estado = 6
                    self.columna += 1
                    #self.lexema += actual
                    self.AgregarToken(TypeToken.FECHA.name)
                    continue

            if self.estado == 4:
                if actual.isdigit():
                    self.estado = 4
                    self.columna += 1
                    self.lexema += actual
                    continue
                else: 
                    self.AgregarToken(TypeToken.NUMERO.name)
                    i -= 1
                    continue

    def AgregarToken(self,tipo):
        self.tokens.append(Token(self.lexema, tipo, self.fila, self.columna))
        self.lexema = ""
        self.estado = 1
        self.tipo = TypeToken.DESCONOCIDO

    def Reservada(self):
        palabra = self.lexema.upper();
        #lista_palabras = ['RESULTADO', 'VS','TEMPORADA','JORNADA','GOLES', 'LOCAL', 'VISITANTE','TOTAL','TABLA_TEMPORADA','PARTIDOS','TOP','SUPERIOR','INFERIOR','ADIOS','F','JI','JF']
        if palabra == 'RESULTADO':
            self.tipo = TypeToken.RESULTADO  
            return True
        if palabra == 'VS':
            self.tipo = TypeToken.VS 
            return True
        if palabra == 'TEMPORADA':
            self.tipo = TypeToken.TEMPORADA
            return True
        if palabra == 'JORNADA':
            self.tipo = TypeToken.JORNADA
            return True
        if palabra == 'GOLES':
            self.tipo = TypeToken.GOLES
            return True
        if palabra == 'LOCAL':
            self.tipo = TypeToken.C_GOLES
            return True
        if palabra == 'VISITANTE':
            self.tipo = TypeToken.C_GOLES
            return True
        if palabra == 'TOTAL':
            self.tipo = TypeToken.C_GOLES
            return True
        if palabra == 'TABLA':
            self.tipo = TypeToken.TABLA_TEM
            return True
        if palabra == 'PARTIDOS':
            self.tipo = TypeToken.PARTIDOS
            return True
        if palabra == 'TOP':
            self.tipo = TypeToken.TOP
            return True
        if palabra == 'SUPERIOR':
            self.tipo = TypeToken.C_TOP
            return True
        if palabra == 'INFERIOR':
            self.tipo = TypeToken.C_TOP
            return True
        if palabra == 'ADIOS':
            self.tipo = TypeToken.ADIOS
            return True
        if palabra == '-F':
            self.tipo = TypeToken.F
            return True
        if palabra == '-N':
            self.tipo = TypeToken.N
            return True
        if palabra == '-JI':
            self.tipo = TypeToken.JI
            return True
        if palabra == '-JF':
            self.tipo = TypeToken.JF
            return True
        return False

    def ImprimirTo(self):
        print("---Tokens---")
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if str(x.tipo) != "DESCONOCIDO":
                print(x.lexema," --> ",str(x.tipo),' --> ',str(x.fila), ' --> ',str(x.columna))

    def ImprimirEr(self):
        print("---TokensErrores---")
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if str(x.tipo) == "DESCONOCIDO":
                print(str(x.lexema)," --> ",str(x.fila), ' --> ',str(x.columna),'--> Error Lexico')

    def Limpiar_Error(self):
        self.tokens.clear()
    
    def Limpiar_Token(self):
        self.tokens.clear()

    def guardarDatos(self):
        tipos = Token("lexema", -1, -1, -1)
        for x in range(len(self.tokens)):
            aux = self.tokens[x].getLexema()
            aux1 = aux.replace('"','').lower()
            if aux1 == 'etiqueta':
                aux_tipo = "etiqueta"
                aux_valor = self.tokens[x+3].getLexema().replace('"',"")
                #self.lista.append(lista(aux_tipo,aux_valor,"","","",""))
            elif aux1 == "texto":
                aux_tipo = 'texto'
                aux_valor = self.tokens[x+3].getLexema().replace('"',"")
                aux_fondo = self.tokens[x+6].getLexema().replace('"',"")
                #print(aux_fondo)
                #self.lista.append(lista(aux_tipo,aux_valor,aux_fondo,"","",""))
            elif aux1 == "grupo-radio":
                aux_valores=[]
                aux_tipo = 'grupo-radio'
                aux_nombre = self.tokens[x+3].getLexema().replace('"',"")
                contador = x+7
                if self.tokens[contador].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador].getLexema().replace("'",""))
                if self.tokens[contador+2].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+2].getLexema().replace("'",""))
                if self.tokens[contador+4].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+4].getLexema().replace("'",""))
                if self.tokens[contador+6].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+6].getLexema().replace("'",""))
                if self.tokens[contador+8].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+8].getLexema().replace("'",""))
                if self.tokens[contador+10].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+10].getLexema().replace("'",""))
                if self.tokens[contador+12].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+12].getLexema().replace("'",""))
                if self.tokens[contador+14].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+14].getLexema().replace("'",""))
                if self.tokens[contador+16].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+16].getLexema().replace("'",""))
                if self.tokens[contador+18].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+18].getLexema().replace("'",""))
                #if self.tokens[contador+20].tipo == tipos.CADENA_SIMPLE:
                    #aux_valores.append(self.tokens[contador+20].getLexema().replace("'",""))
                #print(aux_valores)
                #self.lista.append(lista(aux_tipo,"","",aux_nombre,aux_valores,""))
            elif aux1 == "grupo-option":
                aux_valores=[]
                aux_tipo = 'grupo-option'
                aux_nombre = self.tokens[x+3].getLexema().replace('"',"")
                contador = x+7
                if self.tokens[contador].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador].getLexema().replace("'",""))
                if self.tokens[contador+2].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+2].getLexema().replace("'",""))
                if self.tokens[contador+4].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+4].getLexema().replace("'",""))
                if self.tokens[contador+6].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+6].getLexema().replace("'",""))
                if self.tokens[contador+8].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+8].getLexema().replace("'",""))
                if self.tokens[contador+10].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+10].getLexema().replace("'",""))
                if self.tokens[contador+12].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+12].getLexema().replace("'",""))
                if self.tokens[contador+14].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+14].getLexema().replace("'",""))
                if self.tokens[contador+16].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+16].getLexema().replace("'",""))
                if self.tokens[contador+18].tipo == tipos.CADENA_SIMPLE:
                    aux_valores.append(self.tokens[contador+18].getLexema().replace("'",""))
                #if self.tokens[contador+20].tipo == tipos.CADENA_SIMPLE:
                    #aux_valores.append(self.tokens[contador+20].getLexema().replace("'",""))
                #print(aux_valores)
                #self.lista.append(lista(aux_tipo,"","",aux_nombre,aux_valores,""))
            elif aux1 == "boton":
                aux_tipo ='boton'
                aux_valor = self.tokens[x+3].getLexema().replace('"',"")
                aux_evento = self.tokens[x+6].getLexema().replace('"',"")
                print(aux_evento)
                #self.lista.append(lista(aux_tipo,aux_valor,"","","",aux_evento))
    def reporteTokens(self):

        print("Se ha generado el reporte")
        f = open('ReporteTokens.html','w')
        f.write("<!doctype html>")
        f.write("<html lang=\"en\">")
        f.write("<head>")
        f.write("<!-- Required meta tags -->")
        f.write(" <meta charset=\"utf-8\">")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
        f.write("<!-- Bootstrap CSS -->")
        f.write("<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We\" crossorigin=\"anonymous\">")
        f.write("<title>Reporte Tokens</title>")
        f.write("<style>table, th, td {border: 1px solid black; text-align: center}""</style>")
        f.write("</head>")
        f.write("<body>")
        f.write("<H1 style=\"color:white; background-color:teal\">\n<center> REPORTE TOKENS</center>\n</H1>\n")
        f.write("<h3>Roberto Gómez - 202000544</h3>")
        f.write("<center><table><tr><th>Posicion</th><th>Lexema</th><th>Token</th><th>Fila</th><th>Columna</th></tr>")
        j=1
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if x.tipo != "DESCONOCIDO":
                f.write("<tr class=\"table-primary\">")
                f.write("<center><td><h4>"+ str(j) +"</h4></td>"+"<td><h4>" +str(x.lexema) +"</h4></td>"+"<td><h4>"+ str(x.tipo)+"</h4></td>"+"<td><h4>"+ str(x.fila)+"</h4></td>"+ "<td><h4>"+str(x.columna)+"</h4></td></center>")
                f.write("</tr>")
            j+=1
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

    def reporteErorres(self):
        print("Se ha generado el reporte")
        f = open('ReporteErrores.html','w')
        f.write("<!doctype html>")
        f.write("<html lang=\"en\">")
        f.write("<head>")
        f.write("<!-- Required meta tags -->")
        f.write(" <meta charset=\"utf-8\">")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
        f.write("<!-- Bootstrap CSS -->")
        f.write("<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We\" crossorigin=\"anonymous\">")
        f.write("<title>Reporte Errores</title>")
        f.write("<style>table, th, td {border: 1px solid black; text-align: center}""</style>")
        f.write("</head>")
        f.write("<body>")
        f.write("<H1 style=\"color:white; background-color:teal\">\n<center> REPORTE ERRORES</center>\n</H1>\n")
        f.write("<h3>Roberto Gómez - 202000544</h3>")
        f.write("<center><table><tr><th>Posicion</th><th>Lexema</th><th>Token</th><th>Fila</th><th>Columna</th></tr>")
        j=1
        tipos = Token("lexema", -1, -1, -1)
        for x in self.tokens:
            if x.tipo == "DESCONOCIDO":
                f.write("<tr class=\"table-primary\">")
                f.write("<center><td><h4>"+ str(j) +"</h4></td>"+"<td><h4>" +str(x.lexema) +"</h4></td>"+"<td><h4>"+ str(x.tipo)+"</h4></td>"+"<td><h4>"+ str(x.fila)+"</h4></td>"+ "<td><h4>"+str(x.columna)+"</h4></td></center>")
                f.write("</tr>")
            j+=1
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