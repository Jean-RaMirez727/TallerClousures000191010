# ==============================================================================================================
# EJERCISIO 2
# Multiplicador Paramétrico con Mapeo: 
# Crea crear_operador(factor, operacion_lambda) que devuelva un closure capaz de aplicar la operación 
# recibida utilizando el factor encapsulado.
# ==============================================================================================================

def crear_operador(factor, operacion_lambda):

    def operar(numero):
        return operacion_lambda(numero, factor)

    return operar


# Utilizamos 7 como factor personalizado.
multiplicar_por_7 = crear_operador(
    7,
    lambda numero, factor: numero * factor
)

# Otra operación usando el mismo patrón.
sumar_19 = crear_operador(
    19,
    lambda numero, factor: numero + factor
)

print("\n========== EJERCICIO 2 ==========")
print("618 x 7 =", multiplicar_por_7(618))
print("23 + 19 =", sumar_19(23))