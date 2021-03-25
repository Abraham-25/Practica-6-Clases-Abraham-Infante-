#Crear una clase Persona que tenga como atributos el "cedula, nombre, apellido y la edad 
#(definir las propiedades para poder acceder a dichos atributos)". 
# Definir como responsabilidad una cuncion para mostrar ó imprimir. 
# Crear una segunda clase Profesor que herede de la clase Persona. 
# Añadir un atributo sueldo ( y su propiedad) y en la función para imprimir su sueldo. 
# Definir un objeto de la clase Persona y llamar a sus funciones y propiedades. 
# También crear un objeto de la clase Profesor y llamar a sus funciones y propiedades.

obj = []
saldo=2000
personas = []
def acciones ():
  print(f"Datos: {personas}")
  print(f"sueldo: {obj}")
class Persona:
  def Datos (self):
    self.nombre = input('Nombre:')
    personas.append(self.nombre)
    self.apellido = input('Apellido:')
    personas.append(self.apellido)
    self.edad = int(input("Edad:"))
    personas.append(self.edad)
    self.cedula = int(input('Cedula:'))
    personas.append (self.cedula)

class Profesor(Persona):
  def informe (self): 
    sueldo = float(input("Ponga su Sueldo: "))
    obj.append(saldo-sueldo)

pr1 = Profesor()
pr1.informe()
p1 = Persona()
p1.Datos()
acciones()