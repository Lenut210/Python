print ("EJERCICIO N6  DISTANCIA ETNRE 2 PUNTOS A Y B,  EN 2D")
print ("-------------------------------------------------")

#Entradas

print ("Ingrese coordenadas del Punto A :")
AX = float(input("Ax:"))
AY = float(input("Ay:"))


print ("Ingrese las coordenadas del punto B:")
BX = float(input("Bx:"))
BY = float(input("By:"))

#Proceso

D=((AX-BX)**2+(AY-BY)**2)**0.5

#Salida
print("----------------------------")
print ("Resultado:",D)