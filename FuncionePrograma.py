# Definición de variables para notas
NOTA_MINIMA = 0
NOTA_MAXIMA = 100

nota_de_entrada = float(input("Ingrese la nota del estudiante (entre 0 y 100): "))  

def validar_nota(nota):
    "Funcion para validar que la nota ingresada este dentro del rango establecido para aprobar o reprobar"
    return NOTA_MINIMA <= nota <= NOTA_MAXIMA

def obtener_nota_final(nota_de_entrada):
    "Funcion para determinar si el estudiante aprueba o reprueba basado en la nota ingresada"
    if nota_de_entrada >= 60:
        return "Aprobado"
    else:
        return "Reprobado"
    
def calcular_resultado(nota_de_entrada):
    "Funcion principal que utiliza las funciones anteriores para validar la nota y obtener el resultado final"
    if validar_nota(nota_de_entrada):
        resultado = obtener_nota_final(nota_de_entrada)
        print(f"El estudiante ha {resultado}.")
    else:
        print("La nota ingresada no es válida. Por favor ingrese una nota entre 0 y 100.")


validar_nota(nota_de_entrada)
obtener_nota_final(nota_de_entrada)
calcular_resultado(nota_de_entrada)
