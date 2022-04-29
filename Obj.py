class Obj:
    def __init__(self,fecha, temporada, jornada, local, visitante,mar_l, mar_v):
        self.fecha = fecha
        self.temporada = temporada
        self.jornada = jornada
        self.local = local
        self.visitante = visitante
        self.mar_l = mar_l
        self.mar_v = mar_v

    def __repr__(self):
        return f'\n Fecha {self.fecha} Temporada {self.temporada} Jornada {self.jornada} Local {self.local} Visitante {self.visitante} Marcador Local {self.mar_l} Marcador Visitante {self.mar_v}'
    