
class Persona:
    def __init__(self,nombre, edad):
        self.__nombre = nombre
        self.edad = edad
    
    def get_nombre(self):
        return self.__nombre

    def set_edad(self, Edad):
        self.__edad = Edad
        
    
    def MayorEdad1(self):
        if (self.edad >= "18" ):
            return True
        else:
            return False
    
    def ComparAcion1(self):
        if self.MayorEdad():
            return "es mayor edad"
        else:
            return  "es menor de edad"

    def MayorEdad2(self):
        if (edad2 >= "18" ):
            return True
        else:
            return False
    
    def ComparAcion2(self):
        if self.MayorEdad():
            return "es mayor edad"
        else:
            return  "es menor de edad"

    def ComPara(self):
        if (edad1 > edad2):
            return True
        else:
            return False
    
    

print("escribe tu nombre ")
nombre1 = input()
print("escribe tu edad")
edad1=input()
mostrar = Persona(nombre1, edad1)

print("escribe tu nombre ")
nombre2 = input()
print("escribe tu edad")
edad2=input()
mostrar1 = Persona(nombre2, edad2)




print(mostrar.get_nombre())
mostrar.set_edad("23")
print(mostrar.edad)
print(mostrar.MayorEdad1())

print("-------------------------------")

print(mostrar1.get_nombre())
mostrar1.set_edad("23")
print(mostrar1.edad)
print(mostrar1.MayorEdad2())

print("-------------------------------")

print(mostrar.get_nombre() ,"es mayor que", mostrar1.get_nombre(), "?")
print(mostrar1.ComPara())


