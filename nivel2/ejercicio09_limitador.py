# ==============================================================================================================
# EJERCISIO 9
# Limitador de Tasa Inteligente (Rate Limiter con Reset): 
# Crea crear_limitador_avanzado(max_intentos, fn_alerta) que cuente ejecuciones privadas y ejecute fn_alerta 
# cuando el límite sea superado.
# ==============================================================================================================

def crear_limitador_avanzado(max_intentos, fn_alerta):

    intentos = 0

    def ejecutar(accion="ejecutar"):

        nonlocal intentos

        if accion == "reset":
            intentos = 0
            return "Contador reiniciado."

        intentos += 1

        if intentos > max_intentos:

            fn_alerta(intentos)

            return False

        return True

    return ejecutar


limitador = crear_limitador_avanzado(
    3,
    lambda intentos:
        print(f"ALERTA: se superó el límite con {intentos} intentos.")
)

print("\n========== EJERCICIO 9 ==========")

print("Intento 1:", limitador())
print("Intento 2:", limitador())
print("Intento 3:", limitador())
print("Intento 4:", limitador())

print(limitador("reset"))

print("Después del reset:")
print("Intento 1:", limitador())
print("Intento 2:", limitador())