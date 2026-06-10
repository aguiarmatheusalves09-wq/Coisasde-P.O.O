class Conta():
    def __init__(self, saldo: float):
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor

class Poupanca(Conta):
    def __init__(self, saldo, taxaRendimento: float):
        super().__init__(saldo)
        self.__taxaRendimento = taxaRendimento
    
    def render(self, tempo):
        self.taxaRendimento = (self.saldo * (0.5 * tempo))
        self.__saldo += self.taxaRendimento

class ContaEspecial(Conta):
    def __init__(self, saldo, limite):
        super().__init__(saldo)
        self.__limite = limite
    
    def sacar(self, valor):
        self.__saldo -= valor
        if self.__saldo <= 0:
            resto = self.__saldo - valor
            self.__limite -= resto
            if self.__limite <= 0:
                print("Compra Invalida")
