class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basico', 'plus']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('plano invalido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('plano invalido')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'ver filme {filme}')
        elif self.plano == 'plus':
            print(f"ver filme {filme}")
        elif self.plano == 'basico' and plano_filme == 'plus':
            print('faça uma melhoria para o plano plus')
        else:
            print('plano invalido')


cliente = Cliente("Lucas", "luca@gmail.com", "basico")
print(cliente.plano)
cliente.ver_filme("lagoa preta", 'plus')

# no botao uprag
cliente.mudar_plano('plus')
print(cliente.plano)
cliente.ver_filme("lagoa preta", 'plus')
