class Nave:
    def __init__(self, vida, comb, municao):
        self.__vida = vida
        self.__comb = comb
        self.__municao = municao


    def combustivel(self, comb):
        if comb == "g10":
            self.__comb -= 10
            print(f"A sua nave comsumiu 10l de combustível! Voce possui {self.__comb}l!")
        elif comb == "g30":
            self.__comb -= 30
            print(f"A sua nave comsumiu 30l de combustível! Voce possui {self.__comb}l!")
        elif comb == "g40":
            self.__com -= 40
            print(f"A sua nave comsumiu 40l de combustível! Voce possui {self.__comb}l!")
        

    #def municao(self):


    def vida(self, vida):
        
