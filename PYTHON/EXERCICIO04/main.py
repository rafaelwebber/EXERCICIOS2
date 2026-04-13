'''Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.'''

'''Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.'''

from Carro import Carro
from Moto import Moto


carro1 = Carro('Toyota', 'Corola', 4)
carro2 = Carro('VW', 'Gol', 2)
carro2.definir_ligado(True) 
carro3 = Carro('VW', 'Nivius',  4)

moto1 = Moto('Honda', 'CG', 'Casual')
moto2 = Moto('Honda', 'Bros', 'Casual')
moto3 = Moto('Honda', 'CB', 'Esportiva')

print(carro1)
print(carro2)
print(carro3)

print(moto1)
print(moto2)
print(moto3)