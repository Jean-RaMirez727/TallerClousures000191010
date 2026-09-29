# ==============================================================================================================
# EJERCISIO 1
# Generador de Formateadores con Transformación: 
# Crea crear_formateador(prefijo, fn_transformacion) que devuelva un closure. La función devuelta debe procesar 
# un texto aplicando la lambda/función fn_transformacion y concatenar el prefijo.
# ==============================================================================================================

def crear_formateador(prefijo, fn_transformacion):

    def formatear(texto):
        texto_transformado = fn_transformacion(texto)
        return prefijo + texto_transformado

    return formatear


# Transformamos el texto a mayúsculas y agregamos un prefijo.
formateador = crear_formateador(
    "REGISTRO 618: ",
    lambda texto: texto.upper()
)

print("========== EJERCICIO 1 ==========")
print(formateador("agenda de software"))