class Carro:
    def __init__(self, valor):
        self.valor = valor
        self.modelo = self.definir_modelo()

    def definir_modelo(self):
        if self.valor >= 2000:
            return "civc"
        elif self.valor >= 1500:
            return "ferrari"
        elif self.valor >= 1000:
            return "corsa"
        else:
            return "Modelo Básico"

    def detalhes(self):
        return f"Carro: {self.modelo}, Valor: {self.valor}"

# Exemplo de uso
carro1 = Carro(2000)
print(carro1.detalhes())  # Saída: Carro: Modelo X, Valor: 2000

carro2 = Carro(1200)
print(carro2.detalhes())  # Saída: Carro: Modelo Z, Valor: 1200

