
class reg:
    __temp = 0
    __hum = 0
    __presion = 0
    def __init__(self,t=1,h=1,p=1):
        self.__temp = t
        self.__hum = h
        self.__presion = p
    def __str__(self):
        return "{}      {}      {}".format(self.__temp, self.__hum, self.__presion)
    def get_temp(self):
        return self.__temp
    def get_h(self):
        return self.__hum
    def get_p(self):
        return self.__presion