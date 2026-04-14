from abc import ABC, abstractclassmethod

class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome  = nome 
        self._preco = preco

    @classmethod
    @abstractclassmethod
   #todo mundo que herde ItemCardapio precia ter esse metodo implementado
    def aplicar_desconto(self):
        pass