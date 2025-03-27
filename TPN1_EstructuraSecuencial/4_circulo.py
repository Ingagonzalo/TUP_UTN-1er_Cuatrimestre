#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = float(input("Ingrese el radio de un circulo: "))

pi = 3.1415926

perimetro = 2 * pi * radio

area = pi * radio ** 2

print(f" El area del circulo es de: {area} y su perimetro es de: {perimetro} ")