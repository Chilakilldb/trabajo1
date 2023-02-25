print("bienvenido a hambburgesa grasosa, enseguida desplegaremos el menu para que escoja su hamburguesa preferida")
class Menu:
    def __init__(self, nombre, precio, ingredientes, acompañamiento ):
        self.nombre = nombre 
        self.__precio= precio 
        self.ingredientes = ingredientes
        self.__acompañamiento = acompañamiento
   
    def presentar(self):
        print(f'la hamburguesa {self.nombre} cuesta {self.__precio} tiene {self.ingredientes} y cuenta con {self.__acompañamiento}')
    
    def getprecio(self):
        print(self.__precio)

    def getacompañamiento(self):
        print(self.__acompañamiento)
"""""
class humilde:
    def describir(self):
        print("Una hamburguesa sin ")
"""""    


hamsencilla= Menu("sencilla", 45, "[pan, lechuga, jitomate, ketchup y cebolla]", "[papas y refresco]")
hamsencilla.presentar()

hamdoble= Menu("doble carne", 55, "[pan, lechuga, jitomate, ketchup, doble carne y cebolla]", "[papas y refresco]")
hamdoble.presentar()

hamtocino=Menu("la tocino", 55, "[pan, lechuga, jitomate, ketchup, tocino y cebolla]", "[papas y refresco]")
hamtocino.presentar()

print("tambien contamos con distintos paquetes")
