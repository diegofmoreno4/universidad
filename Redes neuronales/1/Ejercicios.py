#Capitulo 2

#Ejercicio 1
#Escribe un programa que use input para pedirle al usuario
#su nombre y luego darle la bienvenida.
prompt = "introduzca su nombre: "
entrada = input (prompt)
print("Hola: " + entrada)

#Ejercicio 2
#Escribe un programa para pedirle al usuario el número de
#horas y la tarifa por hora para calcular el salario bruto.
prompt = "introduzca Horas: "
horas = int(input (prompt))
prompt = "introduzca Tarifa: "
tarifa = int(input (prompt))
salario = horas * tarifa
print("salario: ")
print(salario)

#Ejercicio 3
#Asume que ejecutamos las siguientes sentencias de asignación:
ancho = 17
alto = 12.0
#Para cada una de las expresiones siguientes, escribe el valor de 
#la expresión y el tipo (del valor de la expresión).
#1. ancho/2 = 8.5 float
#2. ancho/2.0 = 8.5 float
#3. alto/3 = 4 float
#4. 1 + 2 * 5 = 11 int

#Ejercicio 4
#Escribe un programa que le pida al usuario una temperatura en
#grados Celsius, la convierta a grados Fahrenheit e imprima
#por pantalla la temperatura convertida.
prompt = "introduzca grados en Celcius: "
celcius = float(input (prompt))
fahrenheit = celcius * (9/5) + 32
print("El grado en fahrenheit es: ")
print(fahrenheit)

#Capitulo 3

#Ejercicio 1
#Reescribe el programa del cálculo del salario para darle 
#al empleado 1.5 veces la tarifa horaria para todas las
#horas trabajadas que excedan de 40.
#Introduzca las Horas: 45
#Introduzca la Tarifa por hora: 10
#Salario: 475.0
prompt = "introduzca Horas: "
horas = int(input (prompt))
prompt = "introduzca Tarifa: "
tarifa = int(input (prompt))
if int (horas) > 40:
    extra =  (horas - 40) * 1.5 * (tarifa)
    horas= 40
    salario = horas * tarifa + extra
else:
    salario = horas * tarifa   
print("salario: ")
print(salario)

#Ejercicio 2
#Reescribe el programa del salario usando try y except, 
#de modo que el programa sea capaz de gestionar entradas 
#no numéricas con elegancia, mostrando un mensaje y saliendo
#del programa. A continuación se muestran dos ejecuciones del programa:
try:
    prompt = "introduzca Horas: "
    horas = int(input (prompt))
    prompt = "introduzca Tarifa: "
    tarifa = int(input (prompt))

    if int (horas) > 40:
        extra =  (horas - 40) * 1.5 * (tarifa)
        horas= 40
        salario = horas * tarifa + extra
    else:
        salario = horas * tarifa               
    print("salario: ")
    print(salario)
except:    
    print('Por favor, introduzca un número') 

#Ejercicio 3
#Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
#puntuación está fuera de ese rango, muestra un mensaje de error. 
#Si la puntuación está entre 0.0 y 1.0, muestra la calificación
#usando la tabla siguiente:
#Puntuación Calificación
#>= 0.9 Sobresaliente
#>= 0.8 Notable
#>= 0.7 Bien
#>= 0.6 Suficiente
#< 0.6 Insuficiente
try:
    prompt = "introduzca Calificación: "
    cal = float(input (prompt))
    if cal > 1.0:
        print('Puntuación incorrecta')
    elif cal >= 0.9:
        print("Sobresaliente")
    elif cal >= 0.7:
        print("Bien")
    elif cal >= 0.8:
        print("Notable")
    elif cal >= 0.6:
        print("Suficiente")   
    elif cal < 0.6:
        print("Insuficiente") 
except:    
    print('Puntuación incorrecta')       

#Capitulo 4

#Ejercicio 1
#¿Cuál es la utilidad de la palabra clave “def” en Python?
#a) Es una jerga que significa “este código es realmente estupendo”
#b) Indica el comienzo de una función
#c) Indica que la siguiente sección de código indentado debe ser almacenada
#para usarla más tarde => Respuesta correcta
#d) b y c son correctas ambas
#e) Ninguna de las anteriores

#Ejercicio 2
#Qué mostrará en pantalla el siguiente programa Python?
#def fred():
#   print("Zap")
#def jane():
#   print("ABC")
#jane()
#fred()
#jane()

#a) Zap ABC jane fred jane
#b) Zap ABC Zap
#c) ABC Zap jane
#d) ABC Zap ABC => Respuesta correcta
#e) Zap Zap Zap

#Ejercicio 3
#Reescribe el programa de cálculo del salario, con tarifa-y media para las
#horas extras, y crea una función llamada calculo_salario que reciba dos 
#parámetros (horas y tarifa).   
def calculo_salario():
    try:
        prompt = "introduzca Horas: "
        horas = int(input (prompt))
        prompt = "introduzca Tarifa: "
        tarifa = int(input (prompt))

        if int (horas) > 40:
            extra =  (horas - 40) * 1.5 * (tarifa)
            horas= 40
            salario = horas * tarifa + extra
        else:
            salario = horas * tarifa               
        print("salario: ")
        print(salario)
    except:    
        print('Por favor, introduzca un número') 
calculo_salario()    

#Ejercicio 4
#Reescribe el programa de calificaciones del capítulo anterior usando una 
#función llamada calcula_calificacion, que reciba una puntuación como 
#parámetro y devuelva una calificación como cadena.

def calcula_calificacion():
    try:
        prompt = "introduzca Calificación: "
        cal = float(input (prompt))
        if cal > 1.0:
            print('Puntuación incorrecta')
        elif cal >= 0.9:
            print("Sobresaliente")
        elif cal >= 0.7:
            print("Bien")
        elif cal >= 0.8:
            print("Notable")
        elif cal >= 0.6:
            print("Suficiente")   
        elif cal < 0.6:
            print("Insuficiente") 
    except:    
        print('Puntuación incorrecta')
calcula_calificacion()