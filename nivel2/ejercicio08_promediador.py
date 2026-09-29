# ==============================================================================================================
# EJERCISIO 8
# Promediador con Eliminación de Valores Extremos: 
# Crea crear_promediador_filtrado(filtro_ruido_lambda) que acumule datos privadamente pero aplique la lambda 
# para descartar valores atípicos antes de recalcular el promedio.
# ==============================================================================================================

def crear_promediador_filtrado(filtro_ruido_lambda):

    valores = []

    def agregar(valor):

        if filtro_ruido_lambda(valor):
            valores.append(valor)
        else:
            print(f"Valor {valor} descartado por ser ruido.")

        if not valores:
            return 0

        return sum(valores) / len(valores)

    return agregar


# Consideramos válidos valores entre 10 y 100.
# Valores como 7 y 618 serán considerados extremos/ruido.
promediador = crear_promediador_filtrado(
    lambda valor: 10 <= valor <= 100
)

print("\n========== EJERCICIO 8 ==========")
print("Promedio:", promediador(19))
print("Promedio:", promediador(23))
print("Promedio:", promediador(7))
print("Promedio:", promediador(50))
print("Promedio:", promediador(618))
print("Promedio:", promediador(80))