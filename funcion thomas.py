#Esta función activa el movimiento del robot hacia adelante y hacia atrás
def movimiento():
    adelante = 1
    atrás = 2
    contador = 1
    while(contador == 1):
     print("Si desea que el robot vaya para adelante, pulse 1, si desea que vaya para atrás, pulse 2")
     respuesta = int(input())
     if respuesta == 1:
      print("El robot está avanzando correctamente")
      print("Si desea volver a interactuar con el robot pulse 1 sino pulse 0")
      decisión = int(input())
      if decisión == 0:
        print("Se ha cerrado correctamente")
     if respuesta == 2:
      print("El robot está retrocediendo correctamente")
      print("Si desea volver a interactuar con el robot pulse 1 sino pulse 0")
      decisión = int(input())
      if decisión == 0:
       print("Se ha cerrado correctamente")

movimiento()        