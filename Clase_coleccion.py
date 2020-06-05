import numpy as np
from Clase_empleado import Empleado
from Clase_planta import Planta
from Clase_contratado import Contratado
from Clase_externo import Externo
from datetime import datetime
import csv
class Coleccion():
    __arregloEmpleados=None
    __actual=0
    __dimension=0
    __incremento=0
    def __init__(self,dimension,incremento=4):
        self.__arregloEmpleados=np.empty(dimension,dtype=Empleado)
        self.__dimension=dimension
        self.__incremento=incremento
        self.__cantidad=0
    def añadirAlArreglo(self,empleado):
        if(type(empleado)==Planta or type(empleado)==Contratado or type(empleado)==Externo ):
            self.__arregloEmpleados[self.__cantidad]=empleado
            self.__cantidad+=1
        else:
            print("No se añadio al empleado, el parametro era del tipo incorrecto.")
    def cargarEmpleados(self):
        archivo=open("planta.csv")
        archivo1=open("contratados.csv")
        archivo2=open("externos.csv")
        error=None
        bandera=True
        reader=csv.reader(archivo1,delimiter=";")
        for fila in reader:
            if(len(fila)==7):
                    fecha=fila[4].split("/")
                    fechaInicio=datetime(int(fecha[2]),int(fecha[1]),int(fecha[0]))
                    fecha=fila[5].split("/")
                    fechaFin=datetime(int(fecha[2]),int(fecha[1]),int(fecha[0]))
                    self.añadirAlArreglo(Contratado(fila[0],fila[1],fila[2],fila[3],fechaInicio,fechaFin,int(fila[6])))  
            elif(len(fila)==1):
                    Contratado.establecerValorHora(int(fila[0]))
                    bandera=False
            else:
                error=-1
        archivo1.close()
        if(bandera):
            print("No se encomtro en la primera linea del archivo el valor por hora de los contratados,no se les asigno un valor.")
            valor=int(input("Ingrese el valor por hora trabajada de contratados:"))
            Contratado.establecerValorHora(valor)
        if(error==-1):
            print("Hay un error en el archivo ,en una/s fila/S de contratados.csv, las cuales no se añadieron.")
        self.recorrerCSV(archivo)
        self.recorrerCSV(archivo2)
    def recorrerCSV(self,archivo):
         error=None
         reader=csv.reader(archivo,delimiter=";")
         for fila in reader:
            if(len(fila)==6):
                self.añadirAlArreglo(Planta(fila[0],fila[1],fila[2],fila[3],int(fila[4]),int(fila[5])))
            elif(len(fila)==10):
                fecha=fila[4].split("/")
                fechaInicio=datetime(int(fecha[2]),int(fecha[1]),int(fecha[0]))
                fecha=fila[5].split("/")
                fechaFin=datetime(int(fecha[2]),int(fecha[1]),int(fecha[0]))
                self.añadirAlArreglo(Externo(fila[0],fila[1],fila[2],fila[3],fechaInicio,fechaFin,fila[6],int(fila[7]),int(fila[8]),int(fila[9])))
            else:
                error=-1
         archivo.close()
         if(error==-1):
             if(archivo.name== "planta.csv"):
                 print("Hay un error en el archivo ,en una/s fila/S de planta.csv,las cuales no se añadieron.")
             else:
                 print("Hay un error en el archivo ,en una/s fila/S de externo.csv,las cuales no se añadieron.")
    def buscarPorDNI(self,dni):
        i=0
        while(i<len(self.__arregloEmpleados) and self.__arregloEmpleados[i].getDNI()!=dni):
            i+=1
        if(not(i<len(self.__arregloEmpleados))):
            i=-1
        return i
    def incrementarHoras(self,horas,dni):
        pos=self.buscarPorDNI(dni)
        if(pos!=-1):
            if(type(self.__arregloEmpleados[pos])==Contratado):
                self.__arregloEmpleados[pos].incrementarHoras(horas)
                print("Horas acumuladas con el incremento: ",self.__arregloEmpleados[pos].getHoras())
            else:
                print("El empleado no pertenece a los contratados")
                pos=-1
        else:
            print("No se encontro el DNI entre los empleados")
            return pos
    def mostrarMontoTarea(self,tarea):
        acum=0
        print("Datos empleados y costo de obra:")
        for emp in self.__arregloEmpleados:
            if type(emp)==Externo:
                fechaActual=datetime.now()
                if(emp.getTarea()==tarea):  
                    if(fechaActual<emp.getFechaFinal()):
                        acum+=emp.getCostoObra()
                        print(" Nombre:",emp.getNombre()," DNI:",emp.getDNI()," Costo:",emp.getCostoObra())
        if(acum==0):
            print("No se encontraton empleados activos en la tarea ingresada ")
        else:
            print("El monto de tareas total es:",acum)
    def ayuda(self):
        print("Empleados que les corresponde la ayuda:")
        for emp in self.__arregloEmpleados:
            if emp.calcularSueldo()<25000:
                print("Nombre:",emp.getNombre()," Dirección:",emp.getDireccion()," DNI:",emp.getDNI())
    def sueldos(self):
        print("Nombre,Teléfono,Sueldo de empleados:")
        for emp in self.__arregloEmpleados:
            print(emp)
    def mostrarTareas(self):
        tareas=[]
        for emp in self.__arregloEmpleados:
            if(type(emp)==Externo):
                tarea=emp.getTarea()
                if(not(tarea in tareas)):
                    tareas.append(tarea)
        print("Tareas:")
        for tarea in tareas:
            print(tarea)
    def test(self):
        coleccion2=Coleccion(3)
        coleccion2.añadirAlArreglo(Externo("41234324","Mariela Celeste","Gral. Mariano Acha 209N","2646731231",datetime(2020,4,10),datetime(2021,1,15),"Carpintería",10000,50000,10000))
        coleccion2.añadirAlArreglo(Contratado("41234456","Miguel Castro","Mendoza 234 S","2644567532",datetime(2020,3,20),datetime(2020,6,1),30))
        coleccion2.añadirAlArreglo(Planta("34567890","Jose Hernandez","Las heras 233N","264360232",15000,5))
        print("Incremento 30hs a DNI:41234456 ")
        coleccion2.incrementarHoras(30,"41234456")
        print("Monto tarea de Carpintería: ")
        coleccion2.mostrarMontoTarea("Carpintería")
        coleccion2.ayuda()
        coleccion2.sueldos()
        