class Alarme:
    def __init__(self, estado:bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado

    def set__estado(self, valor: bool) -> None:
        self.__estado = valor
