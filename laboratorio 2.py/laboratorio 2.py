#Hola ingeniero bienvenido 
print("Hola ingeniero bienvenido")

#Numero de infracciones

n = int(input("Ingrese el número de infracciones reportadas en el mes: ")) 

infracciones_mañana = int(n * 0.20)
infracciones_tarde = int(n * 0.35)
infracciones_noche = int(n * 0.45)
infracciones_noche = n - infracciones_mañana - infracciones_tarde 

print("El número de infracciones reportadas en la mañana es:", infracciones_mañana)
print("El número de infracciones reportadas en la tarde es:", infracciones_tarde)
print("El número de infracciones reportadas en la noche es:", infracciones_noche)




























