class Pessoa():
    def __init__(self, nome, altura:float):
        self.__nome = nome
        self.__altura = altura
    
    def __str__(self):
        return f"Seu nome é {self.__nome} e sua altura: {self.__altura}"
    
    def __gt__(self, other):
        return self.__altura > other.__altura
    
    def __lt__(self, other):
        return self.__altura < other.__altura

lst = []
resposta = int(input("Quantas pessoas serão cadastradas? "))
for i in range(resposta):
    nome = input("Insira o nome: ")
    altura = float(input("Insira a altura: "))
    respostas = Pessoa(nome, altura)
    lst.append(respostas)

print(max(lst))
print(min(lst))

for pessoa in sorted(lst):
    print(pessoa)