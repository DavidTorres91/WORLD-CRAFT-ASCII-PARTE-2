#En este modulo agregar funciones
import random

filas = []
columnas = []
anchos = []
altos = []
paredes = []
blokes=[]

def titulo():
    print("""

         _   _      _     _  _        _ ___         
 \    / / \ |_) |  | \   /  |_)  /\  |_  |      
  \/\/  \_/ | \ |_ |_/   \_ | \ /--\ |   |    

      __  _ ___ ___      _       _ ___ _   _  
 /\  (_  /   |   |  o   |_) /\  |_) | |_    )
/--\ __) \_ _|_ _|_ o   |  /--\ | \ | |_   /_ 
  """)


def definir_muro(muro):
  """ 
	Función encarga de capturar la cantidad de muros que solicita el usuario

	Parameters
	-----------------
	muro : int
		Cantidad de muros solicitada por el jugaror

	Returns
	------------------
	Retorna el mapa
  """
  for i in range(0, muro):
      fila = int(random.randrange(31))
      filas.append(fila)
      columna = int(random.randrange(31))
      columnas.append(columna)
      ancho = int(random.randrange(abs(30-columna)+1)) 
      anchos.append(ancho)
      alto = int(random.randrange(abs(30-fila)+1))
      altos.append(alto)
  return (filas, columnas, anchos, altos)

def list_pared(muro):
  """ 
	Función generar las lista de paredes que se puntaran, son las entradas basicas que el constructor recibe.

	Parameters
	-----------------
	muro : int
		Cantidad de muros solicitada por el jugaror

	Returns: list
	------------------
    Retorna las paredes lista generadas de manera aleatoria con valores (fila,columna,ancho,alto)
	"""
  for i in range(0, muro):
    pared_x = []
    f = filas[i]
    pared_x.append(f)
    c = columnas[i]
    pared_x.append(c)
    a = anchos[i]
    pared_x.append(a)
    l = altos[i]
    pared_x.append(l)
    paredes.append(pared_x)
  return paredes


def muros(fila, columna, ancho, alto):
  """ 
	Función encarga de construir los muros a pintar, esta funcion es la mas importante dado que determina las casillas exactas que contiene cada pared a pintar

	Parameters
	-----------------
  fila:int
    La fila de la casilla donde iniciara el cuadro.

  columna:int
    La columna de la casilla donde iniciara el cuadro.

  ancho:int
    El desplazamiento en x del cuadro.
  
  alto:int
    El desplazamiento en y del cuadro.
	Returns:list
    coodenadas con cada una de las posiciones a dibujar en el mapa.
	------------------

	"""
  coordenadas = []
  for i in range(0, alto):
      for j in range(0, ancho):
          coordenadas.append(str(fila + i) + ":" + str(columna + j))
  return coordenadas

def pasa_muro(muro,paredes):
  """ 
	Función de transicion, encargada de generear la extraccion de cada una de las pociciones recibidas para pasar muro a muro al constructor

	Parameters
	-----------------
  muro:int
    cantidad de muros que extraera

  paredes:list
    lista de los muros a extraer

	Returns
	------------------
	blokes : list
		Retorna lista de elementos ordenadas para el constructor
	"""
  for i in range (0,muro):
    casilla=muros(paredes[i][0],paredes[i][1],paredes[i][2],paredes[i][3])
    blokes.append(casilla)
  return blokes

def pintar_mundo(colunms, fils):
  """ 
	Función de que dibuja las casillas renglon a renglon, sin importar si sobre escribe una casilla ya marcada

	Parameters
	-----------------
  colunms:int
    Cual es la columna donde dibujara.

  fils:int
    Cual es la columna donde dibujara.

	Returns
	------------------
	casillas : list
		Retorna linea con las marcas indicadas.
	"""
  casillas = []
  for i in range(0, colunms):
      mundo = ("- " * fils)
      casillas.append(mundo)
  return casillas


def reemplaza_linea(fila,columna,sitio):
  """ 
	Función que reemplaza la linea dibujada por pintar:mundo()

	Parameters
	-----------------
  filas:int
    Cual es la filas donde dibujara.

  columna:int
    Cual es la columna donde dibujara.
  
  sitio:int
    Cual es la sitio(mapa) donde dibujara.

	Returns
	------------------
	sitio : list
		Retorna el mapa con los muros marcados
	"""
  nfila = sitio[fila].split()
  nfila.pop(columna)
  nfila.insert(columna,'X')
  nfila.append("")
  sitio[fila]=" ".join(nfila)

  return sitio
    


