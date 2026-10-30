#Reto (Soporte tecnico)
Encendido = False
Pantalla = False
Internet = False

#1
if Encendido and not Pantalla and not Internet:
    print("Revisar conexion a fuente de energia o bateria.")
#2
elif Pantalla and not Encendido and not Internet:
    print("Revisar conexion de monitor, cable HDMI o tarjeta de video.")

#3
elif Internet and not Encendido and not Pantalla:
    print("Reinicio de modem, uso de conexion Ethernet o contactar a proveedor de internet.")

#4
elif Encendido and Pantalla and not Internet:
    print("Posible danio en la placa madre, recomendado enviar al servicio tecnico.")

#5
else:
    print("Equipo funcionando correctamente.")