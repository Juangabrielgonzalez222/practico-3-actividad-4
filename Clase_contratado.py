from Clase_empleado import Empleado
class Contratado(Empleado):
    __fechaInicio=None
    __fechaFinalizacion=None
    __horasTrabajadas=0
    valorporhora=0
    def __init__(self,dni,nombre,direccion,telefono,fechaInicio,fechaFinalizacion,horas):
        from datetime import datetime
        if (type(fechaInicio)==datetime and type(fechaFinalizacion)==datetime): 
            self.__fechaInicio=fechaInicio
            self.__fechaFinalizacion=fechaFinalizacion
            self.__horasTrabajadas=horas
        else:
            print("El tipo de dato de la hora no es correcto")
        super().__init__(dni, nombre, direccion, telefono)
    @classmethod
    def establecerValorHora(cls,valor):
        cls.valorporhora=valor
    @classmethod
    def getValor(cls):
        return cls.valorporhora
    def calcularSueldo(self):
        sueldo=self.__horasTrabajadas*self.getValor()
        return sueldo
    def incrementarHoras(self,horas):
        self.__horasTrabajadas+=horas
    def getHoras(self):
        return self.__horasTrabajadas
    