print("bienvenido a hambburgesa grasosa, enseguida desplegaremos el menu para que escoja su hamburguesa preferida")
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
class Menu:
    def __init__(self, combo, nombre, precio, ingredientes, acompañamiento ):
        self.nombre = nombre 
        self.__precio= precio 
        self.ingredientes = ingredientes
        self.__acompañamiento = acompañamiento
        self.combo = combo
   
    def presentar(self):
        print(f'el combo {self.combo}, es la hamburguesa {self.nombre} cuesta {self.__precio} tiene {self.ingredientes} y cuenta con {self.__acompañamiento}')
    
    def getprecio(self):
        print(self.__precio)

    def getacompañamiento(self):
        print(self.__acompañamiento)

class ordenando:
    def describir(self):
        print("cuantos combos quiere ?")
        numeroorden= input()

        if numeroorden== "1":
            print("Que combo quiere ordenar, favor de escribir el numero del combo?")
            ordencli = input() 
            
            print("la hamburguesa con todo?")
            noquiero=input()

            if ordencli == "1":
                print("su total a pagar es de 45 pesos, su pedido estara listo en un momento")
            else:
                print("su total a pagar es de 55 pesos, su pedido estara listo en un momento")

        else:
            print("cuantos combos 1 quiere ordenar?")
            com1= int(input())

            if com1 > 0:
                print("la o las hamburguesas con todo?, (si o no)")
                noquiero1=input()
                if noquiero1 == "no":
                    print("que ingredientes desea quitar")
                    quitar1=input()

            print("cuantos combos 2 quiere ordenar?")
            com2= int(input())
            if com2 > 0:
                print("la o las  hamburguesas con todo?, (si o no)")
                noquiero2=input()
                if noquiero2 == "no":
                    print("que ingredientes desea quitar")
                    quitar2=input()

            print("cuantos combos 3 quiere ordenar?")
            com3= int(input())
            if com3 > 0:
                print("la o las hamburguesas con todo?")
                noquiero3=input()
                if noquiero3 == "no":
                    print("que ingredientes desea quitar")
                    quitar3=input()
            
            
            res1= 45 * com1
            res2= com2*55
            res3= com3*55
            cuentaf= res1 + res2 + res3

            print("El total a pagar es", cuentaf, "su pedido estara listo en un momento")


"""""
class Lovepapas:
    def describir(self):
        print("Aumenta la cantidad de papas al doble de la racion normal, aumenta 10 pesos de su precio original")

        """""
class despedida:
    def describir(self):
        print("Gracias vuelva pronto")
  

def definircombo(combo):
    combo.describir()



hamsencilla= Menu(1," sencilla", 45, "[pan, lechuga, jitomate, ketchup y cebolla]", "[papas y refresco]")
hamsencilla.presentar()

hamdoble= Menu(2,"doble carne", 55, "[pan, lechuga, jitomate, ketchup, doble carne y cebolla]", "[papas y refresco]")
hamdoble.presentar()

hamtocino=Menu(3," la tocino", 55, "[pan, lechuga, jitomate, ketchup, tocino y cebolla]", "[papas y refresco]")
hamtocino.presentar()
print("--------------------------------------------------------------------------------------------------------------------------------------------------")
print("si quiere ordenar, escriba si, si quiere salir escriba bye")
decicion= input()
print("--------------------------------------------------------------------------------------------------------------------------------------------------")

if decicion == "si":
    clase = ordenando()
    definircombo(clase)
else:
    clase =despedida()
    definircombo(clase)