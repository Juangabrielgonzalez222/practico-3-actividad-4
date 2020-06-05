from Clase_empleado import Empleado
class Externo(Empleado):
    __tarea=""
    __fechaInicio=None
    __fechaFinalizacion=None
    __montoViatico=0
    __costoObra=0
    __costoSeguro=0
    def __init__(self,dni,nombre,direccion,telefono,fechaInicio,fechaFinalizacion,tarea,montoviatico,costoObra,costoSeguro):
        from datetime import datetime
        if (type(fechaInicio)==datetime and type(fechaFinalizacion)==datetime): 
            self.__fechaInicio=fechaInicio
            self.__fechaFinalizacion=fechaFinalizacion
            self.__montoViatico=montoviatico
            self.__tarea=tarea
            self.__costoObra=costoObra
            self.__costoSeguro=costoSeguro
            super().__init__(dni, nombre, direccion, telefono)
        else:
            print("El tipo de dato de la hora no es correcto")
    def calcularSueldo(self):
        sueldo=self.__costoObra-self.__montoViatico-self.__costoSeguro
        return sueldo
    def getTarea(self):
        return self.__tarea
    def getFechaFinal(self):
        return self.__fechaFinalizacion
    def getCostoObra(self):
        return self.__costoObra