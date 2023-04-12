print ("------------------COMPLEMENTARIO N°7 --------------------------")

Pi = 3.1416

print ("ingrese los lados del triangulo")
b = float (input("lado b:"))
c = float (input("lado c:"))
print ("ingrese el angulo en grados sexagisemilaes")
alfa = float (input())

a= (b**2+c**2-2*b*c*math.cos(alfa*Pi/180))**0.50

print ("El lado A es:",a)