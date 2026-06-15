from encodings.punycode import T
from itertools import count


class Onibus():
    def __init__(self, placa, nome_motorista, assentos):
        self.__placa = placa
        self.__nome_motorista = nome_motorista
        self.__assentos = [False] * assentos
    
    def __len__(self):
        return len(self.__assentos)
    
    def __getitem__(self, indice):
        if 0 < indice <= len(self.__assentos):
            self.__assentos = [not indice for indice in self.__assentos]
        else:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
    
    def __setitem__(self, indice, valor):
        if 0 < indice <= len(self.__assentos):
            self.__assentos = [not indice for valor in self.__assentos]
        else:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
    
    def __str__(self):
        return f"Ônibus (Placa: {self.__placa} - Motorista: {self.__nome_motorista} /n Assentos totais: {len(self.__assentos)} /n Assentos ocupados: {self.__assentos.count(True)} /n Assentos livres: {self.__assentos.count(False)})"

onibus = Onibus("ABC-1234", "João Silva", 10)
onibus.__str__()