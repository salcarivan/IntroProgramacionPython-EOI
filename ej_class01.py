class Persona ():
    def __init__(self,Nombres, Apellidos):
     self._Nombres=Nombres
     self._Apellidos=Apellidos

    def caminar(self):
        print ("Caminando")
    
    def identificar (self):
        print ("Nombre: ", self._Nombres, "\nApellidos: ", self._Apellidos)


profesor=Persona ("Billy", "Vanegas")
profesor.identificar()
profesor.caminar()

alumno=Persona ("Pedro", "Sanchez")
alumno.identificar()
alumno.caminar()

alumno1=Persona("Iván", "Salas")
alumno1.identificar()
alumno1.caminar()

admin=Persona("Oscar","León")
admin.identificar()
admin.caminar()
