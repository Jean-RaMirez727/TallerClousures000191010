# ==============================================================================================================
# EJERCISIO 10
# Interruptor Múltiple (Máquina de Estados Ligera): 
# Crea crear_conmutador(lista_estados) que alterne cíclicamente entre una lista de estados internos privados 
# en cada llamada.
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