class Alvo:
    def __init__(self,dano,ataque):
        self.__vidaInimigo=dano
        self.ataque=ataque
        

    def dano(self,dano):
        while self.__vidaInimigo > 25:
            self.__vidaInimigo -= dano
            print(f"O inimigo recebeu {dano} de dano!")
            print(f"O inimigo possui {self.__vidaInimigo} de vida!")
        print("O inimigo está incapacitado. Capture-o!!!")
