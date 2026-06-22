from operator import truediv
import random
class Personagens():
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida
    
    def tomar_dano(self, valor:int):
        return self.__vida - valor
    
    def __str__(self):
        return f" Nome: {self.__nome} \nVida: {self.__vida}"

class Mago(Personagens):
    def __init__(self, nome, vida, mana):
        super().__init__(nome, vida)
        self.__mana = mana
    
    def __str__(self):
        return f"{super().__str__()} \nMana: {self.__mana}"
    
    def __add__(self, valor:float):
        return self.__mana + valor
    
    def __sub__(self, valor:float):
        return self.__mana - valor

    def __mul__(self, valor:float):
        return self.__mana * valor
    
    def __truediv__(self, valor:float):
        return self.__mana / valor

class Barbaro(Personagens):
    def __init__(self, nome, vida, stamina):
        super().__init__(nome, vida)
        self.__stamina = stamina 
        self.__furia = False
    
    def __str__(self):
        return f"{super().__str__()} \nStamina = {self.stamina} \nFuria = {self.furia}"
    
    def __add__(self, valor):
        if self.__furia == True:
            return self.__furia + (valor * 1.5)
        else:
            return self.__furia + valor
    
    def __sub__(self, valor):
        self.__stamina = self.__stamina - valor
        if self.__stamina <= 0 and self.__furia == False:
            self.__furia = True
            self.__stamina = 5
    
    def __mul__(self, valor):
        if self.__furia == True:
            self.__stamina = self.__stamina * valor
            self.vida += 5
        else:
            return self.__stamina * valor
    
    def __truediv__(self, valor):
        return self.__stamina / valor

personagem = input("Escolha o personagem que quer criar \n1) - Mago \n2) - Barbaro")
if personagem == "1":
    while True:
        nome = input("Escola o nome: ")
        mago = Mago(nome, 12, 10)
        print(mago)
        acao = input("1 - Poção simples \n2 - Poção especial \n3 - ataque baasico \n4 - ataque especial \nEscolha umas da opções acima: ")
        if acao == "1":
            mago + 5
        elif acao == "2":
            mago * 1.5
        elif acao == "3":
            mago - 2
        elif acao == "4":
            mago / 2
        elif acao == "5":
            print("Valeu por jogar :)")
            break
        mago.tomar_dano(random.randint(1, 10))
elif personagem == "2":
    while True:
        nome = input("Escolha um nome")
        barbaro = Barbaro(nome, 20, 12)
        print(Barbaro)
        acao = input("1 - Poção simples \n2 - Poção especial \n3 - ataque baasico \n4 - ataque especial \nEscolha umas da opções acima: ")
        if acao == "1":
            barbaro + 5
        elif acao == "2":
            barbaro * 1.5
        elif acao == "3":
            barbaro - 2
        elif acao == "4":
            barbaro / 2
        elif acao == "5":
            print("Valeu por jogar :)")
            break
        barbaro.tomar_dano(random.randint(1, 10))