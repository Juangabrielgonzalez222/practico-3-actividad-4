class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.salir
                         }
    def opcion(self,op, coleccion):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if(op<1 or op>6):    
            func()
        else:
            func(coleccion)
    def salir(self,coleccion):
        print('Usted salio del programa')
    def opcion1(self,coleccion):
        dni=input("Ingrese DNI del empleado:")  
        horas=int(input("Ingrese horas a añadir al empleado:"))
        coleccion.incrementarHoras(horas,dni)
    def opcion2(self,coleccion):
        coleccion.mostrarTareas()
        tarea=input("Ingrese el nombre de la tarea:")
        coleccion.mostrarMontoTarea(tarea)
    def opcion3(self,coleccion):
        coleccion.ayuda()
    def opcion4(self,coleccion):
        coleccion.sueldos()
    def opcion5(self,coleccion):
        coleccion.test()