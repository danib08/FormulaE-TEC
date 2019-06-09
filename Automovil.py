"""
Archivo Automovil
Python 3.7.3

Clase Automovil
Atributos:
    marca (string)
    modelo (string)
    pais (string)
    foto (string)
    temporada (int)
    cant_baterias (int)
    cant_pilas (int)
    tension (int, float)
    estado (string)
    consumo (int, float)
    luz (boolean)
    nivel_bateria (int, float)
    peso (int, float)
    eficiencia (int, float)
    x (int) Marcador para el archivo de texto

Metodos:
    set_marca(marca):
        E: marca
        S: cambia self.marca a marca
        R: str

    set_modelo(modelo):
        E: modelo
        S: cambia self.modelo a modelo
        R: str

    set_pais(pais):
        E: pais
        S: cambia self.pais a pais
        R: str

    set_temporada(temporada):
        E: temporada
        S: cambia self.temporada a temporada
        R: int

    set_cant_baterias(baterias):
        E: baterias
        S: cambia self.cant_baterias a baterias
        R: int

    set_cant_pilas(pilas):
        E: pilas
        S: cambia self.cant_pilas a pilas
        R: int

    set_tension(tension):
        E: tension
        S: cambia self.tension a tension
        R: int, float

    set_estado(estado):
        E: estado
        S: cambia self.estado a estado
        R: str

    set_consumo(consumo):
        E: consumo
        S: cambia self.consumo a consumo
        R: int, float

    set_nivel_bateria(nivel):
        E: nivel
        S: cambia self.nivel_bateria a nivel
        R: int, float

    set_peso(peso):
        E: peso
        S: cambia self.peso a peso
        R: int, float

    set_eficiencia(eficiencia):
        E: eficiencia
        S: cambia self.eficiencia a eficiencia
        R: int, float
"""

class Automovil:
    def __init__(self, marca, modelo, pais, foto, temporada, cant_baterias, cant_pilas, tension, estado, consumo,
                 luz, nivel_bateria, peso, eficiencia, x):
        self.marca = marca
        self.modelo = modelo
        self.pais = pais
        self.foto = foto
        self.temporada = temporada
        self.cant_baterias = cant_baterias
        self.cant_pilas = cant_pilas
        self.tension = tension
        self.estado = estado
        self.consumo = consumo
        self.luz = luz
        self.nivel_bateria = nivel_bateria
        self.peso = peso
        self.eficiencia = eficiencia
        self.x = x

    def set_marca(self, marca):
        if isinstance(marca, str):
            self.marca = marca
        else:
            return "Error"

    def set_modelo(self, modelo):
        if isinstance(modelo, str):
            self.modelo = modelo
        else:
            return "Error"

    def set_pais(self, pais):
        if isinstance(pais, str):
            self.pais = pais
        else:
            return "Error"

    def set_temporada(self, temporada):
        if isinstance(temporada, int):
            self.temporada = temporada
        else:
            return "Error"

    def set_cant_baterias(self, baterias):
        if isinstance(baterias, int):
            self.cant_baterias= baterias
        else:
            return "Error"

    def set_cant_pilas(self, pilas):
        if isinstance(pilas, int):
            self.cant_pilas = pilas
        else:
            return "Error"

    def set_tension(self, tension):
        if isinstance(tension, (int, float)):
            self.tension = tension
        else:
            return "Error"

    def set_estado(self, estado):
        if isinstance(estado, str):
            self.estado = estado
        else:
            return "Error"

    def set_consumo(self, consumo):
        if isinstance(consumo, (int, float)):
            self.consumo = consumo
        else:
            return "Error"

    def set_nivel_bateria(self, nivel):
        if isinstance(nivel, (int, float)):
            self.nivel_bateria = nivel
        else:
            return "Error"

    def set_peso(self, peso):
        if isinstance(peso, (int, float)):
            self.peso = peso
        else:
            return "Error"

    def set_eficiencia(self, eficiencia):
        if isinstance(eficiencia, (int, float)):
            self.eficiencia =  eficiencia
        else:
            return "Error"
