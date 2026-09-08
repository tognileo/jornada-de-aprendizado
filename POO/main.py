class Carro:
    def __init__(self,cor , modelo, ano):
        self .cor =cor
        self .modelo = modelo
        self .ano = ano
        self . velocidade = 0

    def acelerar (self, incremento):
        self .velocidade += incremento
    def frear(self, decremento):
        self .velocidade -= decremento
        

carro1 = Carro ("azul","x1","2022")
print(carro1.cor)
carro1.acelerar(4500)
carro1.frear(40)
print(carro1.velocidade) 



























































































