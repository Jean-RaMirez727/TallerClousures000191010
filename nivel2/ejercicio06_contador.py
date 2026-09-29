# ==============================================================================================================
# EJERCISIO 6
# Contador Ponderado: 
# Crea crear_contador_paso(fn_paso) que incremente su estado interno utilizando una lambda 
# fn_paso(cuenta_actual) en lugar de un incremento fijo.
# ==============================================================================================================

def crear_contador_paso(fn_paso):

    cuenta = 0

    def contar():

        nonlocal cuenta

        cuenta = fn_paso(cuenta)

        return cuenta

    return contar


# Cada llamada aumenta la cuenta en 7.
contador = crear_contador_paso(
    lambda actual: actual + 7
)

print("========== EJERCICIO 6 ==========")
print(contador())
print(contador())
print(contador())
print(contador())