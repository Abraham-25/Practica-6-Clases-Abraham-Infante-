#Crear una clase Contacto. 
# Esta clase deberá tener los atributos "nombre, apellidos, telefono y direccion". 
# También deberá tener una función "SetContacto"  con los parámetros que permita cambiar el valor de los atributos.
#  También tendrá una función "Saludar", que escribirá en pantalla "Hola, soy " seguido de sus datos.
#  Crear también una clase llamada ProbarContacto. 
# Esta clase deberá contener sólo la función principal, que creará dos objetos de tipo Contacto, 
# les asignará los datos del contacto y les pedirá que saluden.



dto1=[]
dto2=[]
class contacto:
  nombre="Abraham"
  dto1.append(nombre)
  apellido="Infante"
  dto1.append(apellido)
  telefono= 5556667777
  dto1.append(telefono)
  direccion="Lugar #69"
  dto1.append(direccion)
  def SetContacto(self):
    op=int(input("Que deseas op?\n 1-Nombre\n 2-Apellido\n 3-telefono\n 4-dirrecion\n Opcion:"))
    if op == 1:
      dto1.remove(self.nombre)
      newn=input("Nuevo Nombre: ")
      dto1.append(newn) 
      dto2.append(newn) 
      print(f"Se ha modificado con exito {self.nombre} por {newn}")
    if op == 2: 
      dto1.remove(self.apellido)
      newa=input("Nuevo Apellido:")
      dto1.append(newa)
      dto2.append(newa)
      print(f"Se ha modifiado {self.apellido} por {newa}")
    if op ==3:
      dto1.remove(self.telefono)
      nwep=input("Nuevo Numero:")
      dto1.append(nwep)
      dto2.append(nwep)
      print(f"Se ha modifiado {self.telefono} por {nwep}.")
    if op ==4:
      dto1.remove(self.direccion)
      newd=input("Nuevo Direccion:")
      dto1.append(newd)
      dto2.append(newd)
      print(f"Se ha modifiado {self.direccion} por {newd}.")
    elif op < 1 and op >4:
        print("No se ha modifiado nada.")
  def saludar (self):
    print(f"Hola ,como estas?{dto1}")
class Pcontactos ():
  def principal(self):
    print(f"Datos: {dto1}")
    print(f"Se han Modificado los datos: {dto2}")
    

personas1=contacto()
personas1.SetContacto()
personas1.saludar()  
personas2=Pcontactos()
Pcontactos.principal()