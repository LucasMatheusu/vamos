class Vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas = vendas

    def metas(self, metas):
        if self.vendas > metas:
            print(self.nome, 'bateu a meta')
        else:
            print(self.nome, 'não bateu a meta')


vendedor1 = Vendedor('lucas')
vendedor1.vendeu(1200)
vendedor1.metas(2311)
print(vendedor1.vendas)
