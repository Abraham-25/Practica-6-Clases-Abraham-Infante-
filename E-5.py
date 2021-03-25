#Cargar una lista de 10 enteros, 
# luego mostrarlos por pantalla a cada elemento separados por una coma. 
# Usando funciones.

var=[]
def l():
  for i in range (10):
    a=int(input(f"Ingrese su numero {i+1}:"))
    var.append(a,)
l()
vista=var
print(f"Su 10 digitos son:\n {var}")
