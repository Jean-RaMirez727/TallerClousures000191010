# ==============================================================================================================
# EJERCISIO 11
# Pipeline de Mapeo y Filtrado Combinado: 
# Crea la HOF procesar_coleccion(lista, fn_predicado, fn_transformacion) que combine internamente filter y 
# map pasando expresiones lambda.
# ==============================================================================================================

def crear_conmutador(lista_estados):

    indice = 0

    def cambiar():

        nonlocal indice

        estado_actual = lista_estados[indice]

        indice = (indice + 1) % len(lista_estados)

        return estado_actual

    return cambiar


conmutador = crear_conmutador(
    ["INICIO", "PROCESANDO", "FINALIZADO"]
)

print("\n========== EJERCICIO 10 ==========")
print(conmutador())
print(conmutador())
print(conmutador())
print(conmutador())
print(conmutador())