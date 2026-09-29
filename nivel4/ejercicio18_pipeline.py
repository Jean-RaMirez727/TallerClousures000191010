# ==============================================================================================================
# EJERCISIO 18
# Motor de Pipeline Secuencial (Currying / Middleware): 
# Crea crear_pipeline(*funciones_transformacion) que permita pasar un dato inicial y hacerlo fluir en orden a 
# través de todas las lambdas/funciones del pipeline.
# ==============================================================================================================

def crear_pipeline(*funciones_transformacion):

    def ejecutar(dato):

        resultado = dato

        for funcion in funciones_transformacion:

            resultado = funcion(resultado)

        return resultado

    return ejecutar


pipeline = crear_pipeline(

    lambda x: x + 19,

    lambda x: x * 7,

    lambda x: x - 23,

    lambda x: x // 2
)

print("\n========== EJERCICIO 18 ==========")
print("Resultado del pipeline:", pipeline(7))