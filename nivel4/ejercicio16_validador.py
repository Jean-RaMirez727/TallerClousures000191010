# ==============================================================================================================
# EJERCISIO 16
# Validador Compuesto de Reglas de Negocio: 
# Crea crear_validador_múltiple(*lambdas_criterios) que retorne un closure que evalúe si un objeto cumple 
# todas las reglas pasadas como argumento.
# ==============================================================================================================

def crear_validador_multiple(*lambdas_criterios):

    def validar(objeto):

        return all(
            criterio(objeto)
            for criterio in lambdas_criterios
        )

    return validar


# Una persona debe:
# 1. Ser mayor o igual a 18.
# 2. Estar activa.
# 3. Tener un nombre de al menos 3 caracteres.
validador = crear_validador_multiple(

    lambda persona: persona["edad"] >= 18,

    lambda persona: persona["activo"] is True,

    lambda persona: len(persona["nombre"]) >= 3
)


persona_1 = {
    "nombre": "Winter",
    "edad": 23,
    "activo": True
}

persona_2 = {
    "nombre": "Jo",
    "edad": 17,
    "activo": True
}

print("========== EJERCICIO 16 ==========")
print("Persona 1:", validador(persona_1))
print("Persona 2:", validador(persona_2))