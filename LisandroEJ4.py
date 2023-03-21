print("Ejercicio Nª4, TOTAL DE PARTIDOS GANADOS")
print("-.--------------------------------------------")

#Entrada de datos
print ("Ingrese los números de partidos ganados")
PG = int(input())
print ("Ingrese ls números de partidos empatados")
PE = int (input())
print ("Ingrese los números de partidos perdidos")
PP = int(input())

#Proceso

PPG = PG*3
PPE = PG*1
PPP = PG*0

PF = PPG+PPE+PPP

#Salida


print ("\nSALIDA: ")
print("------------------------------------")
print ("El puntaje final es:",PF)