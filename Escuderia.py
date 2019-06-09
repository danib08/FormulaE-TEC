"""
Archivo Escuderia
Python 3.7.3

Clase Escuderia
Atributos:
    nombre (string)
    logo (string)
    ubicacion (string)
    patrocinadores (lista de strings)
    pilotos (lista de instancias de la clase Piloto)
    auto_actual (instancia de la clase Automovil)
    historico (lista de instancias de la clase Piloto)

Metodos:
    indice_escud():
        retorna en indice ganador de la escuderia

    set_logo(nuevo_logo):
        E: nuevo_logo
        S: cambia self.logo a nuevo_logo
        R: string

    set_patrocinadores(patr):
        E: patr
        S: cambia self.patrocinadores a patr
        R: lista
"""

class Escuderia:
    def __init__(self, nombre, logo, ubicacion, patrocinadores, pilotos, auto_actual, historico):
        self.nombre = nombre
        self.logo = logo
        self.ubicacion = ubicacion
        self.patrocinadores = patrocinadores
        self.pilotos = pilotos
        self.historico = historico
        self.auto_actual = auto_actual

    def indice_escud(self):
        victorias = 0
        competencias = 0
        for piloto in self.pilotos:
            victorias += piloto.victorias
            competencias += piloto.cant_compet
        ige = victorias / competencias
        return ige

    def set_logo(self, nuevo_logo):
        if isinstance(nuevo_logo, str):
            self.logo = nuevo_logo
        else:
            return "Error"

    def set_patrocinadores(self, patr):
        if isinstance(patr, list):
            self.patrocinadores = patr
        else:
            return "Error"
