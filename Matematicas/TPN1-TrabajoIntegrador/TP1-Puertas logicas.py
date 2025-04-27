# Simulador de puertas lógicas con selección y resultado booleano

print("🧠 Simulador de Puertas Lógicas")

# Menú de opciones
print("\nSelecciona una compuerta lógica:")
print("1. AND")
print("2. OR")
print("3. NOT")
print("4. NAND")
print("5. NOR")
print("6. XOR")

opcion = input("Ingresa el número de la compuerta que deseas simular: ")

if opcion in ["1", "2", "4", "5", "6"]:
    # Pedimos dos valores binarios para las compuertas binarias
    a = int(input("Primer valor binario (0 o 1): "))
    b = int(input("Segundo valor binario (0 o 1): "))
    if (a not in [0, 1]) or (b not in [0, 1]):
        print("Error: Debes ingresar solo 0 o 1.")
    else:
        if opcion == "1":
            resultado_num = a & b
            nombre_compuerta = "AND"
        elif opcion == "2":
            resultado_num = a | b
            nombre_compuerta = "OR"
        elif opcion == "4":
            resultado_num = 1 - (a & b)
            nombre_compuerta = "NAND"
        elif opcion == "5":
            resultado_num = 1 - (a | b)
            nombre_compuerta = "NOR"
        elif opcion == "6":
            resultado_num = a ^ b
            nombre_compuerta = "XOR"
        resultado_bool = bool(resultado_num)
        print(f"\nEl resultado de la compuerta {nombre_compuerta} es: {resultado_num} ({resultado_bool})")

elif opcion == "3":
    # Pedimos un valor binario para la compuerta NOT
    a = int(input("Ingresa un valor binario (0 o 1): "))
    if a not in [0, 1]:
        print("Error: Debes ingresar solo 0 o 1.")
    else:
        resultado_num = 1 - a
        resultado_bool = bool(resultado_num)
        print(f"\nEl resultado de la compuerta NOT es: {resultado_num} ({resultado_bool})")

else:
    print("Opción inválida. Por favor, selecciona un número del menú.")