# Heladería MsP - Registro de pedidos

# Inicializar contadores para cada sabor
# Una heladería quiere registrar 5 pedidos. Por cada cliente, el programa debe pedir el sabor elegido:

# Colores ANSI
#ROJO = "\033[91m"
#VERDE = "\033[92m"
#AMARILLO = "\033[93m"
#AZUL = "\033[94m"
#MAGENTA = "\033[95m"
#CIAN = "\033[96m"
#BLANCO = "\033[97m"
#CHOCOLATE = "\033[38;5;94m"
#VAINILLA = "\033[93m"
#FRESA = "\033[95m"
#RESET = "\033[0m"

#contador_chocolate = 0
#contador_vainilla = 0
#contador_fresa = 0

#print(VERDE +"------------Bienvenido a la Heladería MsP---------- | Por favor, ingrese el sabor de helado que desea pedir:" + VERDE)
#print(CHOCOLATE + "1. Chocolate" + RESET)
#print(VAINILLA + "2. Vainilla" + RESET)
#print(FRESA + "3. Fresa" + RESET    )
#print(AZUL + "4. Salir" + RESET)

#for i in range(5):
#    sabor = float(input("Ingrese el número correspondiente al sabor elegido: "))
    
#    if sabor == 1:
#        contador_chocolate += 1
#    elif sabor == 2:
#        contador_vainilla += 1
#    elif sabor == 3:
#        contador_fresa += 1
#        print("Gracias por elegirnos")
#    elif sabor == 4:
#        print(CIAN+"Gracias por visitar la Heladería MsP. ¡Hasta luego!"+RESET)
#        break
#    else:
#        print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")

#    print(VERDE +"El cliente a ordenado los siguientes sabores: " + RESET + {2: CHOCOLATE + "Chocolate" + RESET, 3: VAINILLA + "Vainilla" + RESET, 4: FRESA + "Fresa" + RESET}.get(sabor, "Opción no válida"))

# Programa Gisnasio 

def validar_entrada(edad):
    "Función para validar que la edad ingresada sea un número entero positivo"
    if edad < 13:
        print("Lo siento, no puedes ingresar al gimnasio. Debes tener al menos 13 años.")
        return False
    elif edad >=20:
        print("ERES CLASE SENIOR, puedes ingresar al gimnasio.")
        return False
    else:
        print("¡Bienvenido al gimnasio! Puedes ingresar.")
        return True
    
edad = int(input("Ingrese su edad: "))

validar_entrada(edad)

   