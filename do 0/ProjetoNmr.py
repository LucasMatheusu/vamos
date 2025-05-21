import random
nmr = random.randint(1, 30)
print('Bem-vindo')
print('Tente acertar o numero!')
tenta = None
#verificar chutes
while tenta != nmr:
    try:
        tenta = int(input('digite aqui um numero de 1 a 30!'))
        if tenta == nmr:
            print('Parabens, voce acertou')
            break
        elif tenta < nmr:
            print('seu numero e maior')
        elif tenta > nmr:
            print('seu numero e menor')
    except ValueError:
        # Caso o usuário digite algo que não seja um número
        print('Por favor, digite u numero valido')
else:
    print('seu numeor e menor!')