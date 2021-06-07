from utils.helper import formata_moeda


class Produto:
    contador = 1
    
    def __init__(self, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self.__preco: float = preco
        Produto.contador += 1

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    def __str__(self) -> str:
        return f'Código: {self.codigo} \nNome: {self.nome} \nPreço: {formata_moeda(self.preco)}'
