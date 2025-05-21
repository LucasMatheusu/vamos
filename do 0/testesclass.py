class Heroi:
    # agora vou definir os atributos
    def __init__(self, nome, origem, poder):
        self.nome = nome
        self.origem = origem
        self.poder = poder

    # outras classes:
    def nivel(self):
        print(f'voce subiu para o  nivel 1 ')

    def batalha(self):
        print('você vai enfrentar um grande guerreiro')

    def dano(self):
        print(f'voce usou seu poder de {self.poder} mas voce perdeu 99% da vida')

    def cura(self):
        print('entao uma curandeira te deu 40% de cura')


malaca = Heroi('casaca', 'grego', 'velocidade')
print(malaca.nome, malaca.origem, malaca.poder)
malaca.nivel()
malaca.batalha()
malaca.dano(), malaca.cura()
