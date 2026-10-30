#Mini proyecto - Asistente medico inteligente
fiebre = False
tos = False
fatiga = False

if fiebre and tos and not fatiga:
    print("Infeccion respiratoria")
elif fiebre and fatiga and not tos:
    print("Posible influenza")
elif fiebre and tos and fatiga:
    print("Alta probabilidad de influenza")
else:
    print("No se encontraron coincidencias")
