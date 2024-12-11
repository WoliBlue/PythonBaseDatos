# CONTROL DE FLUJO
#
# Escribir un programa que pida por pantalla un número entre 1 y 1000. Si el número es mayor de 400 debe indicarlo. Mostrar al final el número introducido
num=int(input("dame el primer numero"))
if num>400:
    print("El número (", num, ") es mayor que 400")
else:
    print("El número (", num, ") es menor que 400")
# 2_1. Comprobar si una cadena de texto termina en vocal. Deberá indicarlo mediante un mensaje. Mostrar al final la cadena de texto.
cadena=input("dame una cadena de texto")
if cadena[-1] in "aeiou":
    print("La cadena de texto termina en vocal")
else:
    print("La cadena de texto no termina en vocal")


# Solicitar dos números y sumarlos. Evaluar el resultado mostrando los mensajes:
# Indicar si la suma es par y mayor que 1000
# Igual que anterior pero menor 
# Indicar si la suma es impar y mayor que 1000
num1=int(input("dame el primer numero"))
num2=int(input("dame el segundo numero"))
suma=num1+num2
if suma%2==0 and suma>100:
    print("La suma es par y mayor que 100")
elif suma%2==0 and suma<100:
    print("La suma es par y menor que 100")
elif suma%2!=0 and suma>100:
    print("La suma es impar y mayor que 100")
else:
    print("La suma es impar y menor que 100")



# Programa que calcule la edad de perro sabiendo la edad humana. Se tendrá que controlar lo siguiente:
# Si la edad es menor que 0 o mayor que 120 mostrar un mensaje Edad incorrecta
# En caso contrario calculamos la edad del perro
# Si la edad del perro es menor a 2 años mostrar un mensaje Perro no tiene edad adulta
# En caso contrario mostrar la edad humana y la edad de perro

edadhumano=int(input("dame la edad humana"))
if edadhumano<0 or edadhumano>120:
    print("la has cagado")
else:
    edadperro=21+(edadhumano-2)*4
    if edadperro<2:
        print("El perro no tiene edad adulta")
    else:
        print("La edad humana es ", edadhumano, " y la edad del perro es ", edadperro)
   

# La duración de un mes varía de 28 a 31 días. En este ejercicio crearás
# un programa que lee el nombre de un mes del usuario como una cadena. 
# El programa debe mostrar el mes y el número de días en ese mes. Mostrar "28 o 29 días" para febrero y los años bisiestos.

mes = input("dame el nombre de un mes")
if mes==["febrero","bisiesto"]:
    print("28 o 29 días")
elif mes in ["abril","junio","septiembre","noviembre"]:
    print("30 días")
else:
    print("31 días")
# Pedir por pantalla una nota (entre 1 y 7). Luego se debe comprobar que el número efectivamente esté en ese rango, si no lo está imprima un mensaje de error. Si lo está, que imprima:
# suspenso si la nota es inferior a 5
# regular si está entre  5 y 6(menor),  
# y por último, bien si está entre 6 y 7.
# Propuesta: Ampliar para los valores de 7 a 10 (Notable y Sobresaliente)
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

nota = int(input("dame una nota"))
if nota<1 or nota>7:
    print("Error")
elif nota<5:
    print("Suspenso")
elif nota<6 and nota>=5:
    print("Regularcin")
elif nota < 7 and nota >= 6:
    print ("Bien")
elif nota < 10 :
    print("Sobresaliente")
else: print ("Notable o Sobresaliente")