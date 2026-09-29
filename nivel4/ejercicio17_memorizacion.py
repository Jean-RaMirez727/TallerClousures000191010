# ==============================================================================================================
# EJERCISIO 17
# Caché con Expiración o Tamaño Máximo (Memorización Profesional): 
# Crea la HOF memorizar_avanzado(fn_costosa, max_items) que retorne un closure controlando el estado privado 
# de una memoria caché con límite de capacidad.
# ==============================================================================================================

def memorizar_avanzado(fn_costosa, max_items):

    cache = {}

    def ejecutar(*args):

        if args in cache:

            print("Resultado recuperado desde caché.")

            return cache[args]

        print("Calculando resultado...")

        resultado = fn_costosa(*args)

        # Si llegamos al límite, eliminamos
        # el elemento más antiguo.
        if len(cache) >= max_items:

            primer_elemento = next(iter(cache))

            del cache[primer_elemento]

        cache[args] = resultado

        return resultado

    return ejecutar


def calcular(numero):

    return numero * numero


memoizada = memorizar_avanzado(
    calcular,
    3
)

print("\n========== EJERCICIO 17 ==========")

print(memoizada(7))
print(memoizada(19))
print(memoizada(618))

# Este ya está almacenado.
print(memoizada(19))

# Al agregar otro elemento se supera la capacidad.
print(memoizada(23))

# 7 fue eliminado por ser el más antiguo.
print(memoizada(7))