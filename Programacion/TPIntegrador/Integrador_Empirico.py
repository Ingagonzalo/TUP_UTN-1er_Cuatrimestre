import time

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Prueba empírica
tamaños = [100000, 200000, 500000,5000000,10000000] #Lista de entrada
for tamaño in tamaños:
    lista = list(range(tamaño))
    objetivo = -1  # Usamos esto para que la funcion busqueda_lineal, recorra todos los tamaños

    inicio = time.time() #Medimos el inicio de la funcion
    busqueda_lineal(lista, objetivo)
    fin = time.time() #Medimos el final de la funcion

    print(f"Tamaño: {tamaño}, Tiempo: {fin - inicio:.15f} segundos")
    

