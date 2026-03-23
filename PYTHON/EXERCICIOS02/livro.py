'''01- Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. 
Inicie um atributo chamado disponivel como True por padrão.

02- Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. 
Crie duas instâncias da classe Livro e imprima essas instâncias.

03- Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

04- Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis 
publicados nesse ano.

05- Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

06- No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

07- No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

08- Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada 
utilizando o método str.'''

class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor 
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self._disponivel}'

    def __repr__(self): #O método __repr__ define como o objeto é exibido em listas e no console. Sem __repr__, Python usa o padrão <Livro object at 0x...>.
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} | {self._disponivel}'

    def emprestar(self):
        self._disponivel = False
        return self._disponivel
    
    @staticmethod
    def verificar_disponibilidade(ano):
        disponivel = []
        for i in Livro.livros:
            if i._ano_publicacao == ano and i._disponivel == True:
                disponivel.append(i)
        return disponivel


livro1 = Livro('volta dos que não foram', 'Rafa', 1899)
livro2 = Livro(' outro livro', 'Autor', 1899)
print(Livro.verificar_disponibilidade(1899))