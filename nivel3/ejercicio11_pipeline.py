# ==============================================================================================================
# EJERCISIO 11
# Pipeline de Mapeo y Filtrado Combinado: 
# Crea la HOF procesar_coleccion(lista, fn_predicado, fn_transformacion) que combine internamente filter y 
# map pasando expresiones lambda.
# ==============================================================================================================

def procesar_coleccion(lista, fn_predicado, fn_transformacion):

    elementos_filtrados = filter(fn_predicado, lista)

    elementos_transformados = map(
        fn_transformacion,
        elementos_filtrados
    )

    return list(elementos_transformados)


numeros = [7, 19, 23, 42, 50, 61, 618]

resultado = procesar_coleccion(
    numeros,
    lambda numero: numero % 2 == 1,
    lambda numero: numero * 2
)

print("========== EJERCICIO 11 ==========")
print("Impares duplicados:", resultado)