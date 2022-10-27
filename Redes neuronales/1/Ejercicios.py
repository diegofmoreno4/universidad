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

#Capitulo 5

#Ejercicio 1
#Escribe un programa que lea repetidamente números hasta
#que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
#muestra por pantalla el total, la cantidad de números y la media de
#esos números. Si el usuario introduce cualquier otra cosa que no sea un
#número, detecta su fallo usando try y except, muestra un mensaje de
#error y pasa al número siguiente.
total = 0
cont = 0
while True:
    prompt = "introduzca un número: "
    num = input (prompt)
    try: 
        if num != "fin":
            total = total + int(num)
            cont = cont + 1 
            media = total/cont
        else:
            print("el total es: total: ",total)   
            print("La cantidad de número es: ",cont) 
            print("La media  es: ",media)
            break 
    except: 
        print('dato erroneo')

#Ejercicio 2
#Escribe otro programa que pida una lista de números como
#la anterior y al final muestre por pantalla el máximo y mínimo de los
#números, en vez de la media.
total = 0
cont = 0
mayor = None
menor = None
while True:
    prompt = "introduzca un número: "
    num = input (prompt)
    try: 
        if num == "fin":
            break 
        else:
            num= int(num) 
            total = total + num
            cont = cont + 1 
            if  mayor is None or num > mayor:
                mayor = num
            if  menor is None or num < menor:
                menor = num
            
    except: 
        print('dato erroneo')
print("el total es: total: ",total)   
print("La cantidad de número es: ",cont) 
print("El número mayor es: ",mayor)
print("El número menor es: ",menor)  

#Resuelva el siguiente ejercicio en el Lenguaje Python:
#Se desea comprar un vehículo financiado: La forma de pago es una cuota 
#inicial del 20% y el 80% restante en 40 cuotas mensuales; a cada cuota 
#mensual se le carga el 2% sobre el saldo de la deuda. Escriba un programa 
#que reciba como entrada el costo del vehículo, y devuelva el valor de la 
#cuota inicial y de cada una de las cuotas mensuales
prompt = "introduzca el costo del vehiculo: "
costo = input (prompt)
inicial= costo * 0.20
saldo = costo - inicial
recargo = saldo * 0.02
cuota_mes = saldo/40 + recargo
print("el 20% de la cuota inicial es : ",inicial)   
print("el valor de las 40 cuotas aplicando el 2% del recargo es: ",cuota)