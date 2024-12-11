# Escriba un programa en Python para aceptar dos números de un usuario e imprimir el promedio de ellos.
import math
print("-------------------")
num1 = int(input("dame el primer numero"))
num2 = int(input("dame el segundo numero"))
print ("El promedio es ", (num1 + num2) / 2)


# Escriba un programa para generar lo siguiente mostrando por pantalla el mensaje. ¡Hola, lector!.
print("-------------------")
print("¡Hola, lector!")

# Imprime la siguiente línea. Puede probarlo usando comillas simples o dobles: la altura de Andres es 1,70m.
print("-------------------")
print("la altura de Andres es 1,70m.")


# Escriba un programa en Python para calcular el área de un círculo. Su programa debe aceptar el radio de un usuario. 
# Puede suponer que el usuario solo proporciona entradas válidas.
print("-------------------")
radio = float(input("dame el radio del círculo"))
pi = 3.14
area = pi * radio ** 2
print("El área del círculo es ", area)

# Escriba un programa que solicite al usuario que ingrese el ancho y el largo de una habitación. 
# Una vez que se hayan leído estos valores, su programa debe calcular y mostrar el área de la habitación. 
# El largo y el ancho se ingresarán como números de coma flotante.
print("-------------------")
ancho = float(input("dame el ancho de la habitación"))
largo = float(input("dame el largo de la habitación"))
area2 = ancho * largo
print("El área de la habitación es ", area2)

# En muchas ciudades, se agrega un pequeño depósito de dinero a los envases de bebidas para animar a las personas a reciclarlos. 
# Menos de un litro 0.10 y más de un litro 0.25.
# Escriba un programa que lea el número de contenedores de cada tamaño del usuario. 
# Formatee la salida para que incluya el signo de euro y dos dígitos a la derecha del punto decimal.
print("-------------------")
envasepeq = int(input("dame el número de envases pequeños"))
envasegr = int(input("dame el número de envases grandes"))
total = envasepeq * 0.10 + envasegr * 0.25
print("El total es ", total, "€")




# Escriba un programa que lea un entero positivo, n, del usuario.. 
# La suma de los primeros n enteros positivos se puede calcular usando la fórmula: sum = n*(n+1)/2.
print("-------------------")
n = int(input("dame un número entero positivo"))
sumaOtra = n * (n + 1) / 2
print("La suma de los primeros n enteros positivos es ", sumaOtra)


# Escriba un programa que lea un número entero del usuario.
# Luego su programa debe mostrar un mensaje que indique si el número es par o impar.
print("-------------------")
numerin = int(input("dame un número entero"))
if numerin % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")


""" Cree un programa que lea dos enteros, a y b, del usuario. Su programa debe calcular y mostrar: 
 • La suma de a y b 
 • La diferencia cuando se resta de a 
 • El producto de a y b 
 • El cociente cuando se divide entre b 
 • El resto cuando se divide entre b 
 • El resultado de log10a 
 • El resultado de a elevado a b
"""
print("-------------------")
a = int(input("dame el primer número entero"))
b = int(input("dame el segundo número entero"))
suma4 = a + b
resta2 = a - b
producto2 = a * b
division2 = a / b
resto = a % b
logaritmo = math.log10(a)
potencia = a ** b
print("La suma de a y b es ", suma4)
print("La diferencia cuando se resta de a es ", resta2)
print("El producto de a y b es ", producto2)
print("El cociente cuando se divide entre b es ", division2)
print("El resto cuando se divide entre b es ", resto)
print("El resultado de log10a es ", logaritmo)
print("El resultado de a elevado a b es ", potencia)

