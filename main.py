from Clase_coleccion import Coleccion
from Clase_menu import Menu
if __name__=='__main__':
    print("Bienvenido al programa:")
    dimension=int(input("Ingrese la cantidad de empleados a cargar desde los archivos:, en este caso 10:"))
    coleccion=Coleccion(dimension)
    menu=Menu()
    coleccion.cargarEmpleados()
    op=None
    print("Bienvenido al programa:")
    while(op!=6):
        print("Ingrese 1 para registrar horas a un empleado ")
        print("Ingrese 2 para mostrar el costo total de una tarea ")
        print("Ingrese 3 para conocer empleados con sueldo inferior a 25000$ ")
        print("Ingrese 4 para mostrar informacion y sueldo de todos los empleados")
        print("Ingrese 5 para realizar un test")
        print("Ingrese 6 para salir")
        op=int(input("Ingrese opcion:"))
        menu.opcion(op,coleccion)