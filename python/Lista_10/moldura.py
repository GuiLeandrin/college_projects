class Moldura:
    def __init__(self, largura=5, altura=3):
        self.setLargura(largura)
        self.setAltura(altura)

    def setLargura(self, largura):
        if largura > 0:
            self.__largura = largura
        else:
            self.__largura = 1

    def setAltura(self, altura):
        if altura > 0:
            self.__altura = altura
        else:
            self.__altura = 1

    def getLargura(self):
        return self.__largura

    def getAltura(self):
        return self.__altura

    def mostrar(self):
        for i in range(self.__altura):
            print("*" * self.__largura)