from limpiador_model import Board

#Jesus Sebastian Jaime Oviedo A01412442

import matplotlib
import numpy as np
import matplotlib.pyplot as plt

import time
import datetime

def basic_example_space():
    # Tamaño del espacio
    m = 10
    n = 10

    # Número de agentes
    num_agentes = 3

    # Porcentaje de celdas normalmente sucias
    p_sucias = 0.6

    # Tiempo máximo de ejecución del algoritmo. MINUTOS
    tiempo_max = 2

    # Nivel de carga máximo de los agentes. Puede ser en porcentaje o en unidades de carga.
    carga_max = 100

    #PROGRAMA
    model = Board(m, n, num_agentes, p_sucias)
    start_time = time.time()
    num_mov = 0
    while((time.time() - start_time) < tiempo_max and not model.allClean()):
        model.step()
    num_mov = model.count_moves(m, n, num_agentes)
    # Reporte
    print('Tiempo: ', str(datetime.timedelta(seconds=(time.time() - start_time))))
    print('Porcentaje de celdas sucias: ', str(model.numDirty()/(m*n)*100)+"%")
    print('Movimientos totales: ', str(num_mov))
    print('Movimientos por agente: ', str(num_mov/num_agentes))


basic_example_space()
#matrix = np.random.randint(maxVal, size=(rows, columns))
