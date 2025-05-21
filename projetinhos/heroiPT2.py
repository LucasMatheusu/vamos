class Hero:
    def __init__(self, nome):
        self.nome = nome
        self.poder = 0
        self.nivel = 0

    def Subir_nivel(self):
        self.nivel += 3
        print(f'{self.nome} subiu de nivel ')

    def Subir_Poder(self):
        self.poder += 4
        print(f'seu poder era 0 agora seu poder subiur para {self.poder}')


class personagem(Hero):
    def __init__(self, nome):
        super().__init__(nome)

    def Habilidade(self):
        print(f'agora {self.nome} a sua habilidade e de fogo')

    def evoluçao(self):
        print(f'seu poder era de fogo agora e fogo + vento')

class Curandeiro(Hero):
     def __init__(self, nome,):
         super().__init__(nome)




kil = personagem('kil')
kil.Subir_nivel()
kil.Habilidade()
kil.Subir_Poder()
kil.evoluçao()
