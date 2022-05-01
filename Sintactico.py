from Token import Token
from TypeToken import TypeToken
class Sintactico:
    preanalisis = TypeToken.DESCONOCIDO
    posicion = 0
    lista = []
    errorSintactico = False

    def __init__(self, lista):
        self.errorSintactico = False
        self.lista = lista
        self.lista.append(Token("#", TypeToken.ULTIMO.name, 0, 0))
        self.posicion = 0
        self.preanalisis = self.lista[self.posicion].tipo
        self.Inicio()

    def Emparejamiento(self, tip):
        f = open('ReporteSintactico.html','w')
        f.write("<!doctype html>")
        f.write("<html lang=\"en\">")
        f.write("<head>")
        f.write("<!-- Required meta tags -->")
        f.write(" <meta charset=\"utf-8\">")
        f.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
        f.write("<!-- Bootstrap CSS -->")
        f.write("<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We\" crossorigin=\"anonymous\">")
        f.write("<title>Reporte Sintactico</title>")
        f.write("<style>table, th, td {border: 1px solid black; text-align: center}""</style>")
        f.write("</head>")
        f.write("<body>")
        f.write("<H1 style=\"color:white; background-color:teal\">\n<center> REPORTE SINTACTICO</center>\n</H1>\n")
        f.write("<h3>Roberto Gómez - 202000544</h3>")
        f.write("<center><table><tr><th>Es</th><th>Se Esperaba</th></tr>")
        if self.preanalisis != tip:
            f.write("<tr class=\"table-primary\">")
            print(str(self.lista[self.posicion].tipo), "-- Sintactico", "-- Se esperaba "+str(tip))
            f.write("<center><td><h4>"+ str(self.lista[self.posicion].tipo) +"</h4></td>"+"<td><h4>" +str(tip) +"</h4></td></center>")
            f.write("</tr>")
            self.errorSintactico = True
        if self.preanalisis != TypeToken.ULTIMO.name:
            self.posicion += 1
            self.preanalisis = self.lista[self.posicion].tipo
        if self.preanalisis == TypeToken.ULTIMO.name:
            print("Se ha finalizado el análisis sintáctico")
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
            
    def Inicio(self):
        print("-- Inicio análisis sintactico --")
        if TypeToken.RESULTADO.name == self.preanalisis:
            self.Resultado()
            self.Repetir()
        elif TypeToken.JORNADA.name == self.preanalisis:
            self.Jornada()
            self.Repetir()
        elif TypeToken.GOLES.name == self.preanalisis:
            self.Goles()
            self.Repetir()
        elif TypeToken.TABLA_TEM.name == self.preanalisis:
            self.Tabla_Temp()
            self.Repetir()
        elif TypeToken.PARTIDOS.name == self.preanalisis:
            self.Partidos()
            self.Repetir()
        elif TypeToken.TOP.name == self.preanalisis:
            self.Top()
            self.Repetir()
        elif TypeToken.ADIOS.name == self.preanalisis:
            self.Adios()
            self.Repetir()
    
    def Resultado(self):
        self.Emparejamiento(TypeToken.RESULTADO.name)
        self.Emparejamiento(TypeToken.CADENA.name)
        self.Emparejamiento(TypeToken.VS.name)
        self.Emparejamiento(TypeToken.CADENA.name)
        self.Emparejamiento(TypeToken.TEMPORADA.name)
        self.Emparejamiento(TypeToken.FECHA.name)
    
    def Jornada(self):
       self.Emparejamiento(TypeToken.JORNADA.name)
       self.Emparejamiento(TypeToken.NUMERO.name)
       self.Emparejamiento(TypeToken.TEMPORADA.name)
       self.Emparejamiento(TypeToken.FECHA.name)
       self.Emparejamiento(TypeToken.F.name)
       self.Emparejamiento(TypeToken.PALABRAS.name)

    def Goles(self):
        self.Emparejamiento(TypeToken.GOLES.name)
        self.Emparejamiento(TypeToken.C_GOLES.name)
        self.Emparejamiento(TypeToken.CADENA.name)
        self.Emparejamiento(TypeToken.TEMPORADA.name)
        self.Emparejamiento(TypeToken.FECHA.name)
    
    def Tabla_Temp(self):
        self.Emparejamiento(TypeToken.TABLA_TEM.name)
        self.Emparejamiento(TypeToken.TEMPORADA.name)
        self.Emparejamiento(TypeToken.FECHA.name)
        self.Emparejamiento(TypeToken.F.name)
        self.Emparejamiento(TypeToken.PALABRAS.name)
    
    def Partidos(self):
        self.Emparejamiento(TypeToken.PARTIDOS.name)
        self.Emparejamiento(TypeToken.CADENA.name)
        self.Emparejamiento(TypeToken.TEMPORADA.name)
        self.Emparejamiento(TypeToken.FECHA.name)
        self.Emparejamiento(TypeToken.F.name)
        self.Emparejamiento(TypeToken.PALABRAS.name)
        self.Emparejamiento(TypeToken.JI.name)
        self.Emparejamiento(TypeToken.NUMERO.name)
        self.Emparejamiento(TypeToken.JF.name)
        self.Emparejamiento(TypeToken.NUMERO.name)

    def Top(self):
        self.Emparejamiento(TypeToken.TOP.name)
        self.Emparejamiento(TypeToken.C_TOP.name)
        self.Emparejamiento(TypeToken.TEMPORADA.name)
        self.Emparejamiento(TypeToken.FECHA.name)
        self.Emparejamiento(TypeToken.N.name)
        self.Emparejamiento(TypeToken.NUMERO.name)
    
    def Adios(self):
        self.Emparejamiento(TypeToken.ADIOS.name)
    
    def Repetir(self):
        if TypeToken.RESULTADO.name == self.preanalisis:
            self.Resultado()
            self.Repetir()
        elif TypeToken.JORNADA.name == self.preanalisis:
            self.Jornada()
            self.Repetir()
        elif TypeToken.GOLES.name == self.preanalisis:
            self.Goles()
            self.Repetir()
        elif TypeToken.TABLA_TEM.name == self.preanalisis:
            self.Tabla_Temp()
            self.Repetir()
        elif TypeToken.PARTIDOS.name == self.preanalisis:
            self.Partidos()
            self.Repetir()
        elif TypeToken.TOP.name == self.preanalisis:
            self.Top()
            self.Repetir()
        elif TypeToken.ADIOS.name == self.preanalisis:
            self.Adios()
            self.Repetir()