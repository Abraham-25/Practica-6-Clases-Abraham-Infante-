#Definir una función superposicion() 
# que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
# Escribir la función usando el bucle for anidado.

l1=[]
l2=[]
def superposicion():
  for i in range (1,4):
    n=input(f"Ponga su Nombre Numero {i} para su lista 1:")
    l1.append(n)
    for i in range (1):
      n1=input(f"Ponga su Nombre Numero {i} para su lista 2:")
      l2.append(n1)
      
definir=superposicion()
print(l1,l2)