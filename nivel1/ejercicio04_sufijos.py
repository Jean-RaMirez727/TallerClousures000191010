# ==============================================================================================================
# EJERCISIO 4
# Generador de Seriales / Nombres Únicos: 
# Crea crear_generador_sufijos(patron_lambda) que devuelva un closure para transformar nombres de archivos 
# basándose en una lambda de formato.
# ==============================================================================================================

def crear_generador_sufijos(patron_lambda):

    def generar(nombre):
        return patron_lambda(nombre)

    return generar


# Creamos nombres de archivos personalizados.
generador = crear_generador_sufijos(
    lambda nombre: f"{nombre}_618_final.py"
)

print("\n========== EJERCICIO 4 ==========")
print(generador("proyecto"))
print(generador("agenda"))
