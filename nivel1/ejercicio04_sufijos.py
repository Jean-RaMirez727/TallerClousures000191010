# ==============================================================================================================
# EJERCISIO 4
# Generador de Seriales / Nombres Únicos: 
# Crea crear_generador_sufijos(patron_lambda) que devuelva un closure para transformar nombres de archivos 
# basándose en una lambda de formato.
# ==============================================================================================================

def crear_descuento_dinamico(regla_condicional_lambda):

    descuento = 0.15

    def calcular(precio):

        if regla_condicional_lambda(precio):
            return precio * (1 - descuento)

        return precio

    return calcular


# Aplicamos descuento a compras de 100 o más.
descuento = crear_descuento_dinamico(
    lambda precio: precio >= 100
)

print("\n========== EJERCICIO 3 ==========")
print("Precio 618:", descuento(618))
print("Precio 79:", descuento(79))