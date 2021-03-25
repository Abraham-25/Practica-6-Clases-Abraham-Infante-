#Crear tres clases ClaseA, ClaseB, ClaseC que ClaseB herede de ClaseA y ClaseC herede de ClaseB. 
# Definir un constructor a cada clase que muestre un mensaje. 
# Luego definir un objeto de la clase ClaseC.

class ClaseA():
  def c1(self):
    print("Soy el revolucionario")
class ClaseB(ClaseA):
  def c2(self):
    print("Sere el hombre mas rico del mundo")
class ClaseC(ClaseB):
  def c3(self):
    print("Traere las paz al mundo")
  
llamando=ClaseA()
ClaseA.c1()
llamando3=ClaseB()
ClaseB.c2()
llamando2=ClaseC()
ClaseC.c3()