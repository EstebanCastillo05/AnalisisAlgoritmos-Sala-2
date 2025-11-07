import random
import time
from bubble_sort import bubble_sort  

# Tamaños de listas que quieres comparar
ns = [100, 500, 1000, 5000]

# Número de repeticiones para obtener un promedio y que no sea un solo un caso aislado
repeticiones = 3

# Abrimos el archivo de resultados
with open("resultados.txt", "w", encoding="utf-8") as f:

    for n in ns:
        tiempos_bubble = []
        tiempos_sorted = []

        for _ in range(repeticiones):
            datos = [random.randint(0, 10**6) for _ in range(n)]

            # Bubble Sort
            datos_b = list(datos)
            t0 = time.perf_counter()
            _ = bubble_sort(datos_b)
            t1 = time.perf_counter()
            tiempos_bubble.append(t1 - t0)

            # sorted() de Python
            datos_s = list(datos)
            t2 = time.perf_counter()
            _ = sorted(datos_s)
            t3 = time.perf_counter()
            tiempos_sorted.append(t3 - t2)

        # Promedios
        promedio_bubble = sum(tiempos_bubble) / repeticiones
        promedio_sorted = sum(tiempos_sorted) / repeticiones

        # Mostrar en consola y guardar en archivo
        linea = f"n={n} -> BubbleSort={promedio_bubble:.6f}s | sorted()={promedio_sorted:.6f}s"
        print(linea)
        f.write(linea + "\n")
