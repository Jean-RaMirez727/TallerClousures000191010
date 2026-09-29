# ==============================================================================================================
# EJERCISIO 20
# Mini-Query Engine sobre Listas de Objetos: 
# Crea crear_consultor(campo) que devuelva una HOF para generar filtros dinámicos sobre listas de 
# diccionarios/objetos mediante expresiones lambda complejas.
# ==============================================================================================================

def crear_consultor(campo):

    def generar_filtro(operador, valor):

        if operador == "==":

            return lambda lista: [
                elemento
                for elemento in lista
                if elemento.get(campo) == valor
            ]

        elif operador == ">":

            return lambda lista: [
                elemento
                for elemento in lista
                if elemento.get(campo) > valor
            ]

        elif operador == "<":

            return lambda lista: [
                elemento
                for elemento in lista
                if elemento.get(campo) < valor
            ]

        elif operador == ">=":

            return lambda lista: [
                elemento
                for elemento in lista
                if elemento.get(campo) >= valor
            ]

        elif operador == "<=":

            return lambda lista: [
                elemento
                for elemento in lista
                if elemento.get(campo) <= valor
            ]

        else:

            raise ValueError(
                "Operador no válido."
            )

    return generar_filtro


productos = [

    {
        "nombre": "Laptop",
        "precio": 1618,
        "stock": 7
    },

    {
        "nombre": "Mouse",
        "precio": 19,
        "stock": 23
    },

    {
        "nombre": "Teclado",
        "precio": 50,
        "stock": 15
    },

    {
        "nombre": "Monitor",
        "precio": 300,
        "stock": 19
    },

    {
        "nombre": "Disco SSD",
        "precio": 80,
        "stock": 7
    }
]


consultor_precio = crear_consultor("precio")

filtro_caros = consultor_precio(
    ">",
    100
)

filtro_baratos = consultor_precio(
    "<",
    100
)


print("\n========== EJERCICIO 20 ==========")

print("Productos con precio mayor a 100:")
print(filtro_caros(productos))

print("\nProductos con precio menor a 100:")
print(filtro_baratos(productos))