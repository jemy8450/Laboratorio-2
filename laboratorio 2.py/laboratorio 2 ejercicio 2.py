#Hola ingeniero bienvenido 
print("Hola ingeniero bienvenido")

# Solicitar tres números enteros desde teclado
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

# Determinar el número más grande
if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3
print("El número", max_num, "es el número más grande de los tres")

# Determinar el número de enmedio
if num1 >= num2 and num1 >= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num2
else:
    max_num = num3
print("El número", max_num, "es el número de enmedio de los tres")

# Determinar el número más pequeño
if num1 <= num2 and num1 <= num3:
    max_num = num1
elif num2 >= num1 and num2 >= num3:
    max_num = num3
else:
    max_num = num3
print("El numero",max_num, "es el número mas pequeño de los tres")

print("fin")

