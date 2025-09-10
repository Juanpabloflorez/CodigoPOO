class perro:
    def __init__(self, alimentado,paseado,acariciado):
        self.alimentado=alimentado
        self.paseado=paseado
        self.acariciado=acariciado

elperro=perro(False,False,False)

def alimentar():
        print("Has alimentado al perro")
        elperro.alimentado=True
def pasear():
        print("Has paseado al perro")
        elperro.paseado=True
def acariciar():
        print("Has acariciado al perro")
        elperro.acariciado=True

while not (elperro.alimentado and elperro.paseado and elperro.acariciado):
      opcion=int(input("Haz al perro feliz, presiona 1 para alimentarlo, 2 para pasearlo y 3 para acariciarlo, realice las 3: "))
      if(opcion==1):
        alimentar()
      elif(opcion==2):
            pasear()
      elif(opcion==3):
            acariciar()
      elif():
           opcion=int(input("opcion no valida, ingrese 1, 2 o 3")) 

if(elperro.alimentado and elperro.paseado and elperro.acariciado):
      print("Enhorabuena, el perro es feliz")