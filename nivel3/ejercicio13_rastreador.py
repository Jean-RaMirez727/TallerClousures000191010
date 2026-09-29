# ==============================================================================================================
# EJERCISIO 13
# Ejecutor Repetitivo con Estado Accesible: 
# Crea ejecutar_y_rastrear(fn_tarea, n) que retorne un closure con el historial de resultados de haber 
# ejecutado fn_tarea $N$ veces.
# ==============================================================================================================

def ejecutar_y_rastrear(fn_tarea, n):

    historial = []

    for _ in range(n):

        resultado = fn_tarea()

        historial.append(resultado)

    def obtener_historial():

        return historial

    return obtener_historial


# Creamos una tarea cuyo estado también está encapsulado.
def crear_tarea_numerica():

    numero = 0

    def tarea():

        nonlocal numero

        numero += 7

        return numero

    return tarea


tarea = crear_tarea_numerica()

rastreador = ejecutar_y_rastrear(
    tarea,
    5
)

print("\n========== EJERCICIO 13 ==========")
print("Historial de resultados:")
print(rastreador())