#Trabajo Práctico Integrador Programación I

#importamos librerías
import random
import time
import sys
sys.setrecursionlimit(20000)  

# Listas base para generación aleatoria
nombres_masculinos = ["Nahuel", "Juan", "Carlos", "Pedro", "Diego"]
nombres_femeninos = ["Florencia", "María", "Lucía", "Sofía", "Camila"]
sexos = ["masculino", "femenino"]
colores_piel = ["blanco", "negro", "marrón"]

# Generar lista de sospechosos aleatorios
def generar_sospechosos(n):
    sospechosos = []
    for _ in range(n):
        sexo = random.choice(sexos)
        nombre = random.choice(nombres_femeninos if sexo == "femenino" else nombres_masculinos)
        sospechoso = {
            "nombre": nombre,
            "sexo": sexo,
            "edad": random.randint(0, 80),
            "color_piel": random.choice(colores_piel)
        }
        sospechosos.append(sospechoso)
    return sospechosos

# QuickSort para ordenar por edad
def quicksort(lista, clave):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[clave] <= pivote[clave]]
        mayores = [x for x in lista[1:] if x[clave] > pivote[clave]]
        return quicksort(menores, clave) + [pivote] + quicksort(mayores, clave)

# Inserción para ordenar por edad (para comparación)    
def insertion_sort(lista, clave):
    
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        # Comparar hacia atrás
        while j >= 0 and lista[j][clave] > actual[clave]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual

    return lista

# Búsqueda binaria para encontrar sospechosos dentro del rango etario ingresado
def buscar_por_rango_etario(lista_ordenada, edad_min, edad_max):
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    inicio = -1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_ordenada[medio]["edad"] < edad_min:
            izquierda = medio + 1
        else:
            inicio = medio
            derecha = medio - 1

    if inicio == -1:
        return []

    resultado = []
    i = inicio
    while i < len(lista_ordenada) and lista_ordenada[i]["edad"] <= edad_max:
        resultado.append(lista_ordenada[i])
        i += 1

    return resultado

# Búsqueda lineal combinada por sexo y color de piel
def filtrar_por_sexo_y_color(lista, sexo_buscado, color_buscado):
    return [
        s for s in lista
        if s["sexo"] == sexo_buscado and s["color_piel"] == color_buscado
    ]

# ***PROGRAMA PRINCIPAL*** #

######### PASOS PREVIOS #########

# Generar lista sospechosos
sospechosos = generar_sospechosos(100)

#Ordenar por edad
inicio = time.time()

#FUNCION INSERCION Y QUICKSORT (activar y desactivar con # según desee)

#sospechosos_ordenados = insertion_sort(sospechosos, "edad")
sospechosos_ordenados = quicksort(sospechosos, "edad")

#tiempo para pruebas
fin = time.time()
print(f"Tiempo de ordenamiento: {fin - inicio:.2f} segundos")


######### INPUTS #########

# INGRESO DE DATOS DETECTIVE #
print("\nIngrese los criterios físicos del sospechoso según los testigos:")

# Pedimos rango etario sospechoso
edad_min = int(input("Edad mínima: "))
edad_max = int(input("Edad máxima: "))

while edad_min >= edad_max:
    print("Edad mínima debe ser menor que edad máxima. Intente nuevamente.")
    edad_min = int(input("Edad mínima: "))
    edad_max = int(input("Edad máxima: "))

# Pedimos sexo sospechoso
sexo_objetivo = input("Sexo (masculino/femenino): ").strip().lower()
while sexo_objetivo not in sexos:
    print("Sexo inválido. Debe ser 'masculino' o 'femenino'.")
    sexo_objetivo = input("Sexo (masculino/femenino): ").strip().lower()

# pedimos color de piel sospechoso
color_objetivo = input("Color de piel (blanco/negro/marrón): ").strip().lower()
while color_objetivo not in colores_piel:
    print("Color inválido. Debe ser 'blanco', 'negro' o 'marrón'.")
    color_objetivo = input("Color de piel (blanco/negro/marrón): ").strip().lower()


######### RESULTADOS #########

# Filtrar por rango etario (búsqueda binaria)
filtrados_por_edad = buscar_por_rango_etario(sospechosos_ordenados, edad_min, edad_max)

# Filtrar por sexo y color de piel
resultado_final = filtrar_por_sexo_y_color(filtrados_por_edad, sexo_objetivo, color_objetivo)

# Mostrar resultados
print(f"\nSospechosos que coinciden con los criterios ingresados:")
if resultado_final:
    for s in resultado_final:
        print(s)
else:
    print("No se encontraron coincidencias.")