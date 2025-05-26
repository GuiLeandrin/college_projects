from moldura import Moldura

class MolduraBaseReforcada(Moldura):
    def __init__(self, largura=5, altura=3):
        super().__init__(largura, altura)

    def mostrar(self):
        for i in range(self.getAltura()):
            print("#" * self.getLargura())
