# ==============================================================================================================
# EJERCISIO 15
# Decorador / HOF de Profiling y Auditoría: 
# Crea la HOF auditar_ejecucion(fn_objetivo, fn_logger) que mida el tiempo y envíe el informe execution al 
# closure/lambda de logging pasado por parámetro.
# ==============================================================================================================

import time


def auditar_ejecucion(fn_objetivo, fn_logger):

    def ejecutar(*args, **kwargs):

        inicio = time.perf_counter()

        resultado = fn_objetivo(*args, **kwargs)

        fin = time.perf_counter()

        tiempo_ejecucion = fin - inicio

        fn_logger(
            resultado,
            tiempo_ejecucion
        )

        return resultado

    return ejecutar


def calcular(numero):

    time.sleep(0.1)

    return numero * numero


logger = lambda resultado, tiempo: print(
    f"Auditoría -> Resultado: {resultado} | "
    f"Tiempo: {tiempo:.6f} segundos"
)

funcion_auditada = auditar_ejecucion(
    calcular,
    logger
)

print("\n========== EJERCICIO 15 ==========")
print("Retorno:", funcion_auditada(23))