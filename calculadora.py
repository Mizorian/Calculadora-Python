# -------------------------------
# Calculadora interactiva en Python
# -------------------------------

# Paso 1: Definir la función principal
def calculadora():
    print("¡Bienvenido a la calculadora interactiva!")
    while True:
        print("\nOperaciones disponibles:")
        print("1 - Suma (+)")
        print("2 - Resta (-)")
        print("3 - Multiplicación (*)")
        print("4 - División (/)")
        print("5 - Salir")

        # Paso 2: Pedir al usuario la operación
        opcion = input("Elige una operación (1-5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break  # Salir del bucle y del programa

        # Paso 3: Pedir los números
        num1 = float(input("Escribe el primer número: "))
        num2 = float(input("Escribe el segundo número: "))

        # Paso 4: Realizar la operación
        if opcion == "1":
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcion == "2":
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcion == "3":
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif opcion == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
            else:
                print("Error: No se puede dividir entre 0")
        else:
            print("Opción no válida, intenta de nuevo")

# Paso 5: Ejecutar la calculadora
calculadora()
