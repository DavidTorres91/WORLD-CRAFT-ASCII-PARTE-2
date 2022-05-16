# nota: 4.5

#WORLD CRAFT ASCII: PARTE 2
import utilidades
import os

centinela=None
while centinela==None:
  utilidades.titulo()

  muro = int(input("Que cantidad de muros desea? "))

  print(f"Los muros a pirntar son:\n",utilidades.definir_muro(muro))
  print("= "*34)
  for i in range(0,muro):
    print(f"La pared {i+1} es:\n ",utilidades.list_pared(muro)[i])
  
  print("= "*34)
  
  lista_casillas=utilidades.pasa_muro(muro,utilidades.list_pared(muro))
  
  mundo1=(utilidades.pintar_mundo(32,32))
  
  
  for i in range(0,len(lista_casillas)):
    for j in range (0,len(lista_casillas[i])):
      x=int(lista_casillas[i][j].split(':')[0])
      y=int(lista_casillas[i][j].split(':')[1])
      utilidades.reemplaza_linea(x,y,mundo1)
    
  print(mundo1)
  newreg=int(input("Desea agregar un nuevo registro?(Si=1,No=0) \n"))
  if newreg==1:
    centinela=None
    os.system ("clear") 
  else:
    centinela=False

   