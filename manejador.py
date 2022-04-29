from calendar import c
from registro import reg
import csv

class man:
    __lista = []
    def __init__(self):
        for i in range(30):
            self.__lista.append([])
            for j in range(24):
                self.__lista[i].append(None)
    def cargarDatos(self):
        archivo = open("reg.csv")
        reader = csv.reader(archivo,delimiter=';')
        for comp in reader:
                nuevo = reg(float(comp[2].replace(",",".")), float(comp[3].replace(",",".")), float(comp[4].replace(",",".")))
                self.__lista[int(comp[0])-1][int(comp[1])-1] = nuevo
        archivo.close()
    def __str__(self):
        return "%s"%(self.__lista)
    def mayor_menor(self):
        mayor_t = 0.0
        menor_t = 9999.9
        mayor_h = 0.0
        menor_h = 9999.9
        mayor_p = 0.0
        menor_p = 9999.9
        for i in range(30):
            for j in range(24):
                if self.__lista[i][j].get_temp() > mayor_t:
                    mayor_t = self.__lista[i][j].get_temp()
                    dia_ma_t = i + 1
                    hora_ma_t = j + 1
                if self.__lista[i][j].get_temp() < menor_t:
                    menor_t = self.__lista[i][j].get_temp()
                    dia_me_t = i + 1
                    hora_me_t = j + 1
                if self.__lista[i][j].get_h() > mayor_h:
                    mayor_h = self.__lista[i][j].get_h()
                    dia_ma_h = i + 1
                    hora_ma_h = j + 1
                if self.__lista[i][j].get_h() < menor_h:
                    menor_h = self.__lista[i][j].get_h()
                    dia_me_h = i + 1
                    hora_me_h = j + 1
                if self.__lista[i][j].get_p() > mayor_p:
                    mayor_p = self.__lista[i][j].get_p()
                    dia_ma_p = i + 1
                    hora_ma_p = j + 1
                if self.__lista[i][j].get_p() < menor_p:
                    menor_p = self.__lista[i][j].get_p()
                    dia_me_p = i + 1
                    hora_me_p = j + 1
        print("Dia y hora de la mayor temperatura {}: {}   {}".format(mayor_t,dia_ma_t,hora_ma_t))
        print("Dia y hora de la menor temperatura {}: {}   {}".format(menor_t,dia_me_t,hora_me_t))
        print("Dia y hora de la mayor humedad {}: {}   {}".format(mayor_h,dia_ma_h,hora_ma_h))
        print("Dia y hora de la menor humedad {}: {}   {}".format(menor_h,dia_me_h,hora_me_h))
        print("Dia y hora de la mayor presion {}: {}   {}".format(mayor_p,dia_ma_p,hora_ma_p))
        print("Dia y hora de la menor presion {}: {}   {}".format(menor_p,dia_me_p,hora_me_p))
    def promedio(self):
        for i in range(24):
            z = 0.0
            for j in range(30):
                z += self.__lista[j][i].get_temp()
                v = (z/30)
            print("El promedio de la temperatura para la hora {} es {}".format(i,v))
    def imprimir(self):
        d = int(input("ingrese dia a listar"))
        print("'HORA'       'TEMPERATURA'       'HUMEDAD'       ''PRESION")
        for i in range(24):
            t = str(self.__lista[d-1][i].get_temp())
            h = str(self.__lista[d-1][i].get_h())
            p = str(self.__lista[d-1][i].get_p())
            print("{}           {}          {}          {}".format(i, t.ljust(12), h.ljust(8), p))