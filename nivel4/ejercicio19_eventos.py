# ==============================================================================================================
# EJERCISIO 19
# Sistema Pub/Sub (Event Listener con HOFs y Closures): 
# Crea crear_sistema_eventos() que devuelva un closure gestor capaz de registrar suscriptores (lambdas) y 
# emitir eventos notificando a cada uno.
# ==============================================================================================================

def crear_sistema_eventos():

    suscriptores = {}

    def gestionar(
        accion,
        evento=None,
        callback=None
    ):

        # Registrar un nuevo suscriptor.
        if accion == "registrar":

            if evento not in suscriptores:

                suscriptores[evento] = []

            suscriptores[evento].append(callback)

            return "Suscriptor registrado."

        # Emitir el evento.
        elif accion == "emitir":

            if evento not in suscriptores:

                return "No existen suscriptores."

            for suscriptor in suscriptores[evento]:

                suscriptor()

            return "Evento emitido."

        return "Acción no válida."

    return gestionar


sistema_eventos = crear_sistema_eventos()


sistema_eventos(
    "registrar",
    "inicio",
    lambda: print("Listener 1: Sistema iniciado.")
)

sistema_eventos(
    "registrar",
    "inicio",
    lambda: print("Listener 2: Preparando aplicación.")
)

sistema_eventos(
    "registrar",
    "final",
    lambda: print("Listener 3: Sistema finalizado.")
)


print("\n========== EJERCICIO 19 ==========")
print("Emitiendo evento INICIO:")

sistema_eventos(
    "emitir",
    "inicio"
)

print("\nEmitiendo evento FINAL:")

sistema_eventos(
    "emitir",
    "final"
)