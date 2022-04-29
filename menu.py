from cgi import print_form
import csv
from manejador import man


class menu:
    __op = 0
    def __init__(self, p=0):
        self.__op = p
    def opciones(self):
        salir = True
        l = man()
        l.cargarDatos()
        while salir:
            print("Opcion 1: Mostrar para cada variable el día y hora de menor y mayor valor")
            print("Opcion 2: Indicar la temperatura promedio mensual por cada hora")
            print("Opcion 3: Dado un número de día listar los valores de las tres variables para cada hora del día dado")
            print("Opcion 4: salir del programa")
            self.__op = int(input("ingrese opcion 1, 2, 3 o 4"))
            if self.__op == 1:
                l.mayor_menor()
            if self.__op == 2:
                l.promedio()
            if self.__op == 3:
                l.imprimir()
            if self.__op == 4:
                salir = not salir