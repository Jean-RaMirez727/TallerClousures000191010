# ==============================================================================================================
# EJERCISIO 14
# Compositor de Cadenas de Operaciones: 
# Crea la HOF componer_dos(f, g) que devuelva un closure que aplique $f(g(x))$, permitiendo encadenar 
# transformaciones complejas en línea.
# ==============================================================================================================

def componer_dos(f, g):

    def composicion(x):

        return f(g(x))

    return composicion


# Primero sumamos 19.
sumar_19 = lambda x: x + 19

# Después multiplicamos por 7.
multiplicar_7 = lambda x: x * 7

operacion_combinada = componer_dos(
    multiplicar_7,
    sumar_19
)

print("\n========== EJERCICIO 14 ==========")
print("Resultado:", operacion_combinada(7))