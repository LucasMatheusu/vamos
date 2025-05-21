class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('acessando o banco de dados')
            print('cadastrar p Ususario {}, idade {}'.format(nome, idade))
        else:
            print('dados ivalidos')