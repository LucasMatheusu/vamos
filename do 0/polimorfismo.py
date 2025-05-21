class PessoaA:
    def se_apresentar(self):
        print("ola eu sou a pessoa A")


class PessoaB(PessoaA):

    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print("estou aleterando esse metado")


class PessoaC(PessoaB):
    def __init__(self):
        super().__init__()


pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()

pessoa3 = PessoaC()
pessoa3.se_apresentar()
