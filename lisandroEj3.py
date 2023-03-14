print. (---------------)
print("Ejercicio 3: Puntaje final")
print("----------------")

#Entradas
print ("Ingrese numero de respuestas correctas")
RC = int (input())
print ("Ingrese numero de respuestas incorrectas")
RI = int (input())
print ("Ingrese numero de respuetas en blanco")
RB = int (input())

#Proceso

PCR = RC*3
PRI = RI*-1
PRB= RB*0
PF = PCR + PRI + PRB
#salida
print ("El puntaje total es:",PF)