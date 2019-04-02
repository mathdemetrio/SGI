from ponto import Ponto


class Window(object):
    def __init__(self, minimo_x, minimo_y, maximo_x, maximo_y):
        self.min = Ponto(minimo_x, minimo_y)
        self.max = Ponto(maximo_x, maximo_y)

    def setCoordenadasMinimo(self, x, y):
        self.min.set_x(x)
        self.min.set_y(y)


    def setCoordenadasMaximo(self, x, y):
        self.max.set_x(x)
        self.max.set_y(y)

    def getXMin(self):
        return self.min.get_x()

    def getXMax(self):
        return self.max.get_x()

    def getYMin(self):
        return self.min.get_y()

    def getYMax(self):
        return self.max.get_y()
