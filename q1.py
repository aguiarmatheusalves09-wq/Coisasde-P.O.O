class Carteira():
    def __init__(self, moeda, saldo):
        self.__saldo = saldo
        self.__moeda = moeda
    
    def __add__(self, valor_yuan):
        if self.__moeda != 'CNY':
            if self.__moeda == 'USD':
                valor_yuan = valor_yuan / 0.14
            elif self.__moeda == 'BRL':
                valor_yuan = valor_yuan / 0.85
        self.__saldo += valor_yuan
        
    def __sub__(self, valor_retirado):
        self.__saldo =- valor_retirado
