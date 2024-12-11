#VARIABLES. TIPOS BASICOS
"""
int, float, bool(True,False), str
Las cadenas no son más que texto encerrado entre comillas simples (‘cadena’) o dobles 
Podemos usar \n y \t
Funciones
len(cadena) Nos devuelve la longitud de una cadena
int(cadena) Convierte a int
str(numero) Convierte a string

string
nombre='juan'
print(nombre[0])   #se imprime una j 
print(nombre[-1]  #se imprime una n. Última letra
x = 'a' in 'aeiou' #operador in. Lo usaremos con listas

Comentarios
# y """ """

Asignación de variables
No se indica el tipo. Python lo averigua o infiere
x= 6 # python sabe que es int

Operadores
Los mismos que otros lenguajes. Para las condiciones (and,or,not)

Conversión de tipos
- a entero (tipo de datos “int”): int('26') , int(35.9) , round(45.9) 
- con decimales (tipo de datos “float”): float('25.7') 
- a cadena (tipo de datos “string”): str(43)

Solicitar por teclado
input devuelve siempre un string
 edad = int( input('¿Cuántos años tienes? ') ) 

Salida por pantalla
print('texto a imprimir', variables, ...) 
Por ejemplo: 
 print('Hola', variable) 
 print(a, b, c, sep='|', end=' ') # end="" permite que la salida sea en horizontal
 print('resultado','\t',3*5,'\n') 



"""
# Importamos liberías random (num aleatorio) y time (para parar unos segundos)
import random
import time

# Con input pedimos por pantalla. Siempre devuelve un string
numero = int(input("dame numero: "))
print("El numero  es ",numero)
number = random.randint(1, 20)
print("hola, espera 3 segundos")
time.sleep(3)


#SENTENCIA IF
"""
Sintaxis
if condicion:
    sentencia
elif condicion:
    sentencia
else:
    sentencia
Se recomienda usar parentesis en las condiciones
"""
#Sentencia if elif else. Indicar siempre : al final de la sentencia. Tabulación
if numero <= 5:
    print("numero menor igual que 5")
elif numero <= 10:
    print("numero menor igual que 10")
else:
    print("numero mayor a 10")
    

#BUCLES
"""
while condicion:
    sentencia

for i in range(inicial,final,incremento):
    sentencia
Valor por defecto de inicial es 0
Valor por defecto de incremento es 1
Ejemplo: 
range(1,10,2) De uno a 10 de dos en dos.
range(1,10). De 1 a 9.
range(10). De 0 a 9

Recorrer strings
for c in “hola”:
	print(c,end=””)
	
cadena = “prueba”
for i in range(len(cadena)):
	print(cadena[i],end=”-”)
	
cadena = “prueba”
i = 0
while i < len(cadena):
    print(cadena[i],end=””)
    i = i+1
"""
# Bucle for. Función range(n) va desde 0 a n-1
print("for")
for i in range(10):
    print(i)
print("while")
cont = 0
while cont < 10:
    print(cont)
    cont = cont + 1

#LISTAS
"""
Las listas en Python son uno de los tipos o estructuras de datos más versátiles del lenguaje, 
ya que permiten almacenar un conjunto arbitrario de datos. 
Es decir, podemos guardar en ellas prácticamente lo que sea. 
Si vienes de otros lenguajes de programación, se podría decir que son similares a los arrays.
lista = [1, 2, 3, 4]

Características
Son ordenadas, mantienen el orden en el que han sido definidas
Pueden ser formadas por tipos arbitrarios
Pueden ser indexadas con [i].
Se pueden anidar, es decir, meter una dentro de la otra.
Son mutables, ya que sus elementos pueden ser modificados.
Son dinámicas, ya que se pueden añadir o eliminar elementos.

Acceso
a = [10, "Python", 3.97]
print(a[0]) #10
print(a[1]) #Python
print(a[2]) #3.97
Se puede también acceder al último elemento usando el índice [-1].
a = [90, "Python", 3.87]
print(a[-1]) #3.87
De la misma manera, al igual que [-1] es el último elemento, podemos acceder a [-2] que será el penúltimo.
print(a[-2]) #Python

Slices
Se extraen elementos de una secuencia, tal como una lista o una cadena de caracteres.
 las posiciones de inicio y de fin no necesariamente tienen que ser números positivos. 
 Si se usan números negativos, Python asume que se están referenciando las posiciones numeradas 
 desde la última hasta la primera, empezando con -1

cadena="Hola Mundo!"
>>> cadena[-1]
'!'
>>> cadena[-2]
'o'

Slices avanzados
Tercer parámetro disponible para describir un slice en Python, el cual también se separa usando el caracter ':'. 
Este tercer parámetro, que tiene como valor por defecto 1, indica cómo se deben recorrer las posiciones desde 
el inicio hasta el fin. Así, cuando su valor es 1 con cada paso se va a sumar 1 a la posición actual, 
mientras que cuando el valor es -2 con cada paso se resta 2 a la posición actual.

>>> valores
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> valores[0:5]
[0, 1, 2, 3, 4]
>>> valores[5:]
[5, 6, 7, 8, 9, 10]
>>> valores[2:-1:2]
[2, 4, 6, 8]
>>> valores[-1::-2]
[10, 8, 6, 4, 2, 0]
>>> valores[-1:0:-2]
[10, 8, 6, 4, 2]

Funciones de listas
x.append(elem) añade al final
x.insert(i,e) añade en pos i
x.remove(elem) elimina elem
x.sort() ordena
x.reverse() inversa
x.clear() vacía lista
x.copy() copia por referencia
"""
# Listas ejemplo recorrido
print("lista de 1 a 5")
lista = [1,2,3,4,5]
for l in lista:
    print(l)



#FUNCIONES
"""
sintaxis
def <nombre-funcion> (<parámetros>):
     bloque código
     return <objeto>

def suma(a, b):
    return a + b
res = suma(3,2)

PARAMETROS
Python nos permite llamar a la función indicando en cualquier orden los parámetros de la misma, 
pero debemos especificar en la llamada el nombre del parámetro y el valor a enviarle. 
Este tipo de paso de parámetros en mi opinión no es recomendable

def calcular_sueldo(nombre,costohora,cantidadhoras):
    sueldo=costohora*cantidadhoras
    print(nombre,"trabajo",cantidadhoras,"y cobra un sueldo de",sueldo)
# bloque principal
calcular_sueldo("juan",10,120)
calcular_sueldo(costohora=12,cantidadhoras=40,nombre="ana")

Función que devuelva la suma de entre 2 y n parámetros.
def sumar(v1,v2,*lista):
    suma=v1+v2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma

Los parámetros y las variables declaradas dentro de una función son de ámbito local, 
mientras que las definidas fuera de ella son de ámbito ámbito global.

>>> lenguaje = ‘C++’
>>> def saludo():
...     lenguaje = 'Python'
...     print('¡Bienvenido a', lenguaje + '!')
...     return

>>> saludo()
¡Bienvenido a Python!
>>> print(lenguaje)
C++

Cuando pasamos un objeto mutable (modificable) como listas o diccionarios cualquier cambio 
que se haga dentro de la función mediante el parámetro asociado afectará al objeto original.

>>> primer_curso = [Entornos', FOL]
>>> def añade_modulo(curso, modulo):
...     curso.append(modulo)
...     return
...
>>> añade_modulo(primer_curso, 'Sistemas')
>>> print(primer_curso)
['Entornos', 'FOL', 'Sistemas']

"""
# Funciones ejemplo
def suma_f(a,b):
    return a + b

# Procedimiento
def suma_p(a,b):
    print (a + b)
res = suma_f(3,4)
print("Función suma ",res)
print("Procedimiento suma: ")
suma_p(6,8)

#EXCEPCIONES
"""
Las excepciones en Python son una herramienta muy potente que la gran mayoría de lenguajes de programación modernos tienen. Se trata de una forma de controlar el comportamiento de un programa cuando se produce un error.
a = 3; b = 0
print(a/b)
# ZeroDivisionError: division by zero
Excepción controlada por python

TRY/EXCEPT
Se pueden tratar varias excepciones con un mismo mensaje o de forma independiente
try:
    #c = 5/0       # Si comentas esto entra en TypeError
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except (ZeroDivisionError, TypeError):
    print("Excepcion ZeroDivisionError/TypeError")
“””except ZeroDivisionError:
    print("División  entre cero!")
except TypeError:
    print("Error de tipos!")

ELSE/FINALLY
Else. Dicho bloque se ejecutará si no ha ocurrido ninguna excepción.
Finally. Dicho bloque se ejecuta siempre, haya o no haya habido excepción.

try:
    # Se fuerza excepción
    x = 3/0
except:
    print("Entra en except")
else:
    print("Entra en el else sin excepción”)
finally:
    print("Entra en finally")


"""
#POO
