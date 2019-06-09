"""
Archivo Instancias
Python 3.7.3

Imports:
"""
from Escuderia import *
from Piloto import *
from Automovil import *

# Se crean las 5 escuderias de la interfaz
suning = Escuderia("Suning", "suning_logo.png", "China", ["Razer", "ASROCK", "Suning"],
                   [Piloto("SwordArt", 22, "Taiwanés", 2019, 20, 5, 10, 0, 0), Piloto("Smlz", 21, "Chino", 2019, 18, 2,
                    6, 1, 1)], Automovil("Land Rover", "Range Rover", "Inglaterra", "range_rover.png", 2019, 1, 4, 3,
                    "Disponible", 0.5, False, 75, 4, 0.5, 0), [])

fnatic = Escuderia("Fnatic", "fnatic_logo.png", "Reino Unido", ["OnePlus", "Monster Energy", "DXRacer", "AMD"],
                  [Piloto("Rekkles", 22, "Sueco", 2019, 50, 35, 46, 0, 2), Piloto("Hylissang", 24, "Búlgaro", 2019, 35, 5,
                    18, 3, 3)], Automovil("Dallara", "Spark-Renault SRT 01E1", "Italia", "spark.png", 2019, 2, 2, 5,
                   "Disponible", 2, False, 80, 896, 3, 1), [])

tsm = Escuderia("TSM", "tsm_logo.png", "Estados Unidos", ["Logitech", "Twitch", "HyperX", "Dr Pepper"],
                [Piloto("Bjergsen", 23, "Danés", 2019, 70, 50, 50, 0, 4), Piloto("Smoothie", 22, "Canadiense", 2019, 20, 1,
                 3, 5, 5)], Automovil("Dallara", "Spark SRT05e1", "Italia", "spark2.png", 2019, 2, 1, 4, "Disponible", 1,
                 False, 60, 900, 2, 2), [])

origen = Escuderia("Origen", "origen_logo.png", "Dinamarca", ["RFRSH Entertainment", "Audi"], [Piloto("Nukeduck", 23,
                   "Noruego", 2019, 47, 6, 10, 3, 6), Piloto("Patrik", 19, "Checo", 2019, 10, 1, 3, 0, 7)],
                   Automovil("Dallara", "Spark-Renault SRT 01E2", "Italia", "spark.png", 2019, 2, 2, 5, "Disponible", 2,
                   False, 50, 896, 3, 3), [])

g2 = Escuderia("G2", "g2_logo.png", "Alemania", ["Logitech G", "AOC", "NeedforSeat"], [Piloto("Perkz", 20, "Croata",
               2019, 32, 5, 12, 5, 8), Piloto("Wunder", 20, "Danés", 2019, 34, 8, 15, 0, 9)], Automovil("Dallara",
               "Spark SRT05e2", "Italia", "spark2.png", 2019, 2, 1, 4, "Disponible", 1, False, 90, 900, 2, 4), [])


# Lista con las escuderias de la interfaz
escuderias = [suning, fnatic, tsm, origen, g2]

# Lista vacia que tendra a todos los pilotos de las escuderias
pilotos = []

# Lista vacia que tendra a todos los automoviles de las escuderias
autos = []

# for que itera sobre cada escuderia
for e in escuderias:
    # for que itera sobre cada piloto de cada escuderia y lo agrega a la lista 'pilotos'
    for p in e.pilotos:
        pilotos.append(p)
    # se agrega cada automovil de las escuderias a la lista 'autos'
    autos.append(e.auto_actual)
