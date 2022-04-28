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

    def Match(self, tip):
        if self.preanalisis != tip:
            print(str(self.lista[self.posicion].tipo), "-- Sintactico", "-- Se esperaba "+str(tip))
            self.errorSintactico = True
        if self.preanalisis != TypeToken.ULTIMO.name:
            self.posicion += 1
            self.preanalisis = self.lista[self.posicion].tipo
        if self.preanalisis == TypeToken.ULTIMO.name:
            print("Se ha finalizado el análisis sintáctico")

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
        self.Match(TypeToken.RESULTADO.name)
        self.Match(TypeToken.CADENA.name)
        self.Match(TypeToken.VS.name)
        self.Match(TypeToken.CADENA.name)
        self.Match(TypeToken.TEMPORADA.name)
        self.Match(TypeToken.FECHA.name)
    
    def Jornada(self):
       self.Match(TypeToken.JORNADA.name)
       self.Match(TypeToken.NUMERO.name)
       self.Match(TypeToken.TEMPORADA.name)
       self.Match(TypeToken.FECHA.name)
       self.Match(TypeToken.F.name)
       self.Match(TypeToken.PALABRAS.name)

    def Goles(self):
        self.Match(TypeToken.GOLES.name)
        self.Match(TypeToken.C_GOLES.name)
        self.Match(TypeToken.CADENA.name)
        self.Match(TypeToken.TEMPORADA.name)
        self.Match(TypeToken.FECHA.name)
    
    def Tabla_Temp(self):
        self.Match(TypeToken.TABLA_TEM.name)
        self.Match(TypeToken.TEMPORADA.name)
        self.Match(TypeToken.FECHA.name)
        self.Match(TypeToken.F.name)
        self.Match(TypeToken.PALABRAS.name)
    
    def Partidos(self):
        self.Match(TypeToken.PARTIDOS.name)
        self.Match(TypeToken.CADENA.name)
        self.Match(TypeToken.TEMPORADA.name)
        self.Match(TypeToken.FECHA.name)
        self.Match(TypeToken.F.name)
        self.Match(TypeToken.PALABRAS.name)
        self.Match(TypeToken.JI.name)
        self.Match(TypeToken.NUMERO.name)
        self.Match(TypeToken.JF.name)
        self.Match(TypeToken.NUMERO.name)

    def Top(self):
        self.Match(TypeToken.TOP.name)
        self.Match(TypeToken.C_TOP.name)
        self.Match(TypeToken.TEMPORADA.name)
        self.Match(TypeToken.FECHA.name)
        self.Match(TypeToken.N.name)
        self.Match(TypeToken.NUMERO.name)
    
    def Adios(self):
        self.Match(TypeToken.ADIOS.name)
    
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