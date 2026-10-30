#Actividad 4
print("#4 Hola Inteligencia Artificial")

#Actividad 5
fiebre = True
tos = False
if fiebre and tos:
    print("#5 Posible infeccion respiratoria")
else:
    print("#5 No existe evidencia suficiente")
    
#Actividad 6 - Agregar Reglas
Fiebre = True
Tos = True
Fatiga = True
if Fiebre and Tos and Fatiga:
    print("#6 Alta probabilidad de influenza")
elif Fiebre and Tos:
    print("#6 Posible infeccion respiratoria")
else:
    print("#6 Sin diagnostico")

#Actividad 7 - Logica Basica (25,28,30,31,35)
temperatura = 25
if temperatura > 30:
    print("#7 Temperatura alta")
else:
    print("#7 Temperatura Normal")

#Actividad 8 - Logica Difusa Simplificada
temperatura = 14
grado_calor = temperatura/40
print("#8 Grado de Calor:", round(grado_calor,2))
