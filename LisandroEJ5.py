print ("EJERCICIO N5  NUMERO DE MICRO DISCOS")
print ("-------------------------------------------------")

#Entradas

print ("Ingrese GB:")
GB = float(input())

#Proceso

MG = GB*1024
MD = MG/1.44

#Salida

print("\nSALIDA: ")
print (MD)

print("Numero de Discos necesarios: ", math.ceil(MD))



