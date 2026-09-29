# ==============================================================================================================
# EJERCISIO 7
# Acumulador con Filtro de Aceptación: 
# Crea crear_acumulador_validado(criterio_lambda) que mantenga un total acumulado privado, pero solo sume 
# los valores que superen la prueba de la lambda enviada.
# ==============================================================================================================

def crear_acumulador_validado(criterio_lambda):

    total = 0

    def acumular(valor):

        nonlocal total

        if criterio_lambda(valor):
            total += valor

        return total

    return acumular


# Solo se aceptan valores mayores que 19.
acumulador = crear_acumulador_validado(
    lambda valor: valor > 19
)

print("\n========== EJERCICIO 7 ==========")
print("Agregando 7:", acumulador(7))
print("Agregando 23:", acumulador(23))
print("Agregando 618:", acumulador(618))
print("Agregando 15:", acumulador(15))
print("Agregando 50:", acumulador(50))