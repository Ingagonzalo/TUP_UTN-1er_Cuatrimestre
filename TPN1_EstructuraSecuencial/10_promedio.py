#Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

numero1 = float(input("Ingresa su primer valor: "))
numero2 = float(input("Ingresa su segundo valor: "))
numero3 = float(input("Ingresa su tercer valor: "))

promedio = (numero1 + numero2 + numero3)/3

print(f"El valor promedio de los valores {numero1}, {numero2}, {numero3} es de {promedio}")