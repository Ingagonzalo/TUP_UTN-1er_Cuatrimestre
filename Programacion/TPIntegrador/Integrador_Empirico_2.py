<<<<<<< HEAD
import time

def busqueda_lineal(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1

# Prueba empírica
tamaños = [100_000, 200_000, 500_000, 5_000_000, 10_000_000]
for tamaño in tamaños:
    objetivo = -1  # Fuerza la búsqueda completa
    inicio = time.perf_counter()
    busqueda_lineal(range(tamaño), objetivo)
    fin = time.perf_counter()
=======
import time

def busqueda_lineal(lista, objetivo):
    for i, valor in enumerate(lista):
        if valor == objetivo:
            return i
    return -1

# Prueba empírica
tamaños = [100_000, 200_000, 500_000, 5_000_000, 10_000_000]
for tamaño in tamaños:
    objetivo = -1  # Fuerza la búsqueda completa
    inicio = time.perf_counter()
    busqueda_lineal(range(tamaño), objetivo)
    fin = time.perf_counter()
>>>>>>> 61fab377bc4462eed250fe67f3f018ab75a62ab4
    print(f"Tamaño: {tamaño:,}, Tiempo: {fin - inicio:.9f} segundos")