class Circo:
    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()

    def apresentar_palhaço(self):
        print('palhaço apresentando seu show')


class malabarista:

    def apresentar_show(self):
        print('malabarista apresentar seu show')


class palhaço:

    def apresentar_show(self):
        print('palhaço apresentar seu show')

class Domador:
    def apresentar_show(self):
        print('domador apresentar seu show')

class conferente:
    def apresentar_show(self):
        print('o conferente esta verificando os ingressos')




Circo = Circo()
malabarista = malabarista()
palhaço = palhaço()
Domador = Domador()
conferente = conferente()
Circo.apresentar(malabarista)
Circo.apresentar(palhaço)
Circo.apresentar(Domador)
Circo.apresentar(conferente)
