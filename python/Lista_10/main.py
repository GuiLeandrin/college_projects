from moldura import Moldura
from moldura_reforcada import MolduraBaseReforcada

print("Moldura simples:")
m = Moldura(10, 4)
m.mostrar()

print("\nMoldura reforçada:")
r = MolduraBaseReforcada(10, 4)
r.mostrar()
