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