from Clase_empleado import Empleado
class Planta(Empleado):
    __sueldobasico=0
    __antiguedad=0
    def __init__(self,dni,nombre,direccion,telefono,sueldo,antiguedad):
        self.__sueldobasico=sueldo
        self.__antiguedad=antiguedad
        super().__init__(dni, nombre, direccion, telefono)
    def calcularSueldo(self):
        sueldo=self.__sueldobasico+((100/self.__sueldobasico)*self.__antiguedad)
        return sueldo
