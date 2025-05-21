cont = (' zero','um', 'dois', 'tres', 'quetro', 'cinco', 'seis', 'sete', 'oito')
while True:
    num = int(input('digite um numero de 0 a 20'))
    if 0 <= num <= 20:
        break
    print('erro, tente novamente', end='')
print(f'Voce digitou o numero {cont[num]}')
