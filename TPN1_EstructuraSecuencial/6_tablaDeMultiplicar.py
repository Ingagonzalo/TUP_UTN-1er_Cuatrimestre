#Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

tabla = int(input("Ingrese su tabla: "))

for i in range (1,11):
    
    resultado = i*tabla
    print(f"{tabla} * {i} = {resultado}")
    
print("Fin")