# ==============================================================================================================
# EJERCISIO 12
# Reductor / Agrupador Personalizado: 
# Crea la HOF agrupar_por(lista, fn_clave) que reciba una colección de diccionarios y los agrupe en un 
# diccionario clave-valor basándose en el resultado de la lambda fn_clave.
# ==============================================================================================================

def agrupar_por(lista, fn_clave):

    grupos = {}

    for elemento in lista:

        clave = fn_clave(elemento)

        if clave not in grupos:
            grupos[clave] = []

        grupos[clave].append(elemento)

    return grupos


personas = [
    {"nombre": "Ana", "edad": 19},
    {"nombre": "Luis", "edad": 23},
    {"nombre": "Pedro", "edad": 19},
    {"nombre": "Maria", "edad": 23},
    {"nombre": "Carlos", "edad": 22}
]

grupos = agrupar_por(
    personas,
    lambda persona: persona["edad"]
)

print("\n========== EJERCICIO 12 ==========")
print(grupos)
