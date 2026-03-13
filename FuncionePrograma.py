# Definición de variables para notas

# Colores ANSI
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CIAN = "\033[96m"
BLANCO = "\033[97m"

RESET = "\033[0m"

NOTA_MINIMA = 0
NOTA_MAXIMA = 100

print(VERDE+"------------------------------Bienvenido al programa de evaluación de estudiantes-----------------------------"+RESET)
print(AZUL+"==============================================================================================================="+RESET)
print(AZUL+"==============================================================================================================="+RESET)
print(AZUL+"==============================================================================================================="+RESET)
print(AZUL+"==============================================================================================================="+RESET)

nota_de_desarrollo = float(input("Ingrese la nota de desarrollo del estudiante: "))  # Este porcentaje es equivalente al 60% de la formación del estudiante
nota_de_ingles = float(input("Ingrese la nota de inglés del estudiante: "))  # Este porcentaje es equivalente al 20% de la formación del estudiante
nota_de_habilidades_emocionales = float(input("Ingrese la nota de habilidades emocionales del estudiante: "))  # Este porcentaje es equivalente al 20% de la formación del estudiante
if nota_de_desarrollo > 60:
    print(AMARILLO+"La nota de desarrollo no puede ser mayor a 60. Por favor ingrese una nota válida."+RESET)
if nota_de_ingles > 20:
    print(AMARILLO+"La nota de inglés no puede ser mayor a 20. Por favor ingrese una nota válida."+RESET)
if nota_de_habilidades_emocionales > 20:
    print(AMARILLO+"La nota de habilidades emocionales no puede ser mayor a 20. Por favor ingrese una nota válida."+RESET)  

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
        if resultado == "Aprobado":
            print(VERDE+f"El coder {nombre_coder} ha {resultado}."+RESET)
        else:
            print(ROJO+f"El coder {nombre_coder} ha {resultado}."+RESET)
    else:
        print(AMARILLO+"La no" \
        "ta ingresada no es válida. Por favor ingrese una nota entre 0 y 100."+RESET)

def calcular_promedio_de_la_formacion(nota_de_desarrollo, nota_de_ingles, nota_de_habilidades_emocionales):
    "Funcion para calcular el promedio de la formación del estudiante basado en las notas ingresadas"
    promedio = (nota_de_desarrollo * 0.60) + (nota_de_ingles * 0.20) + (nota_de_habilidades_emocionales * 0.20 / 3)
    return promedio        

nombre_coder = input("Ingrese el nombre del coder: ")

validar_nota(nota_de_desarrollo+nota_de_ingles+nota_de_habilidades_emocionales)
obtener_nota_final(nota_de_desarrollo+nota_de_ingles+nota_de_habilidades_emocionales)
calcular_resultado(nota_de_desarrollo+nota_de_ingles+nota_de_habilidades_emocionales)
promedio = calcular_promedio_de_la_formacion(nota_de_desarrollo, nota_de_ingles, nota_de_habilidades_emocionales)