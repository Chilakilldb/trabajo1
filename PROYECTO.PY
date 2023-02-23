class Persona:

    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def MayorEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False
 
    def VerifiCacion(self):
        if self.MayorEdad():
            return "Es mayor de edad"
        else:
            return "Es menor de edad"

    def PresenTar(self):
        print(f' me llamo {usuario.nombre}, tengo {usuario.edad} años, y mi identificacion es {usuario.DNI}')



usuario = Persona("Maria",18,"Rgnajdbsk")
usuario.PresenTar()

#print(Persona.MayorEdad())
print("es mayor de edad ?", usuario.MayorEdad())

print(usuario.nombre, usuario.VerifiCacion())




