# ==============================================================================================================
# EJERCISIO 5
# Conversor de Divisas con Margen: 
# Crea crear_conversor(tasa, margen_lambda) que retorne una función para convertir montos calculando 
# dinámicamente la comisión adicional.
# ==============================================================================================================

def crear_conversor(tasa, margen_lambda):

    def convertir(monto):

        convertido = monto * tasa
        margen = margen_lambda(convertido)

        return convertido + margen

    return convertir


# Ejemplo: conversión con una tasa personalizada
# y un margen del 2%.
conversor = crear_conversor(
    0.92,
    lambda monto: monto * 0.02
)

print("\n========== EJERCICIO 5 ==========")
print("Conversión de 618 =", round(conversor(618), 2))
print("Conversión de 19 =", round(conversor(19), 2))