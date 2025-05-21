#classe pai, vai ser usado para as outras classes
class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero
# super e usado para puxar as informaçoes da primeira classe- mao na roda amigos
class Aluno(Pessoa):
    def __init__(self, nome, idade, genero, curso, periodo):
        super().__init__(nome, idade, genero)
        self.curso = curso
        self.periodo = periodo
class Professor(Pessoa):
    def __init__(self, nome, idade, genero, salario, serviço):
        super().__init__(nome, idade, genero)
        self.salario = salario
        self.serviço = serviço
    

Lucas = Aluno('lucas', 22, 'Masculino', 'analise de sistemas', '2 semestre')
marlinho = Professor('Marlinho', 34, 'M', '4200', 'Prof-fisica')
print(Lucas.nome, Lucas.idade, Lucas.curso, Lucas.genero, Lucas.periodo)
print(marlinho.nome, marlinho.idade, marlinho.serviço, marlinho.genero, marlinho.salario)
