"""
Archivo Piloto
Python 3.7.3

Clase Piloto
Atributos:
    nombre (string)
    edad (int)
    nacionalidad (string)
    temporada (int)
    cant_compet (int)
    cant_vict (int)
    victorias (int)
    cant_destacadas (int)
    cant_fallidas (int)
    x (int) Marcador para el archivo de texto

Métodos:
    rend_global():
        retorna el rendimiento global del piloto
    rend_espec():
        retorna el rendimiento específico del piloto

    set_nombre(nombre):
        E: nombre
        S: cambia self.nombre a nombre
        R: string

    set_edad(edad):
        E: edad
        S: cambia self.edad a edad
        R: int

    set_nacionalidad(nacionalidad):
        E: nacionalidad
        S: cambia self.nacionalidad a nacionalidad
        R: string

    set_temporada(temporada):
        E: temporada
        S: cambia self.temporada a temporada
        R: int

    set_cant_compet(cant_compet):
        E: cant_compet
        S: cambia self.cant_compet a cant_compet
        R: int

    set_cant_vict(cant_vict):
        E: cant_vict
        S: cambia self.victorias a cant_vict
        R: int

    set_cant_destacadas(destacadas):
        E: destacadas
        S: cambia self.cant_destacadas a destacadas
        R: int

    set_cant_fallidas(fallidas):
        E: fallidas
        S: cambia self.cant_fallidas a fallidas
        R: int
"""


class Piloto:
    def __init__(self, nombre, edad, nacionalidad, temporada, cant_compet, cant_vict, cant_destacadas, cant_fallidas, x):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.temporada = temporada
        self.cant_compet = cant_compet
        self.victorias = cant_vict
        self.cant_destacadas = cant_destacadas
        self.cant_fallidas = cant_fallidas
        self. x = x


    def rend_global(self):
        rgp = (self.cant_destacadas / (self.cant_compet - self.cant_fallidas)) * 100
        return rgp

    def rend_espec(self):
        rep = (self.victorias / (self.cant_compet - self.cant_fallidas)) * 100
        return rep

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.nombre = nombre
        else:
            return "Error"

    def set_edad(self, edad):
        if isinstance(edad, int):
            self.edad = edad
        else:
            return "Error"

    def set_nacionalidad(self, nacionalidad):
        if isinstance(nacionalidad, str):
            self.nacionalidad = nacionalidad
        else:
            return "Error"

    def set_temporada(self, temporada):
        if isinstance(temporada, int):
            self.temporada = temporada
        else:
            return "Error"

    def set_cant_compet(self, cant_compet):
        if isinstance(cant_compet, int):
            self.cant_compet = cant_compet
        else:
            return "Error"

    def set_cant_vict(self, cant_vict):
        if isinstance(cant_vict, int):
            self.victorias = cant_vict
        else:
            return "Error"

    def set_cant_destacadas(self, destacadas):
        if isinstance(destacadas, int):
            self.cant_destacadas = destacadas
        else:
            return "Error"

    def set_cant_fallidas(self, fallidas):
        if isinstance(fallidas, int):
            self.cant_fallidas = fallidas
        else:
            return "Error"
