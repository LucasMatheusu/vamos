class Carro:
    def __init__(self, modelo, velocidade, marca):
        self.modelo = modelo
        self.velocidade = velocidade
        self.marca = marca

    def cor(self):
        print('azul')

    def ano_do_carro(self):
        print('2020')


carro1 = Carro('civic', '200Km', 'Honda ')
print(carro1.modelo, carro1.velocidade, carro1.marca)
carro1.cor()
carro1.ano_do_carro()
