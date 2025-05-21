class Monstro:
    def __init__(self, nome, origem):
        self.nome = nome
        self.poder = 1
        self.nivel = 1

    def subir_nivel(self):
        self.nivel += 3
        print(f'subiu de nivel {self.nivel}')



class personagem(Monstro):
    def __init__(self, nome, Duasvidas):
        super().__init__(nome)
        self.Duasvidas = Duasvidas


    def usar_espada(self):
        print(F"{self.nome} usou espada")
    def esquivar(self):
        print(F'{self.nome} esquivou e atacou')

    def aumentar_poder(self):
        self.poder += 2
        print(F'seu poder subiu {self.poder}')


look = personagem('look')
look.usar_espada()
look.subir_nivel()
look.esquivar()
look.aumentar_poder()
