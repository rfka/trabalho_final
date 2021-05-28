vida = 100
chance=False
from alvo import Alvo
import random

opcao = int(input(''' 
        Escolha sua opção:
        [ 1 ] Frente
        [ 2 ] Esquerda
        [ 3 ] Direita
        [ 4 ] Encerrar missão
    '''))

while  True:
    if opcao == 1:
        num = random.randint(1, 10)
        print(num)
        if num == 5:
            print("Voce chegou no final!!!")
            chance=True
        else:
            comb = "g10"
            opcao = input("Voce não chegou no fim! Escolha entre as opções abaixo para prosseguir: ")

    if opcao == 2:
        print("O caminho escolhido não possui saída. ")
        comb = "g40" #10 0 g40 entraria num IF e miminuiria 40; g20 entraria num IF e diminuiria 20
    
    if opcao == 3:
        print("Voce entrou em um campo de asteroides!!!")
        comb = "g30"
        vida = "v" #random de 10 a 50
        municao = "m" #random de 10 a 50

    if opcao == 4:
        print("Comandante, voce FRACASSOU!!!")
        break
while chance==True:
    print("""Qual ação você prefere: 
    [1]Ataque sorrateiro
    [2]Ataque direto
    [3]Desistir
    """)
    if opcao==1:
        vida="v"
        ataque=random.randint(1,20)
        Alvo.dano(ataque)
        
    if opcao==2:
        vida=""
        ataque=random.randint(40,80)
        if 75<ataque<80: 
            print("A nave inimiga explodiu, você perdeu seu alvo.")
        else:
            Alvo.dano(ataque)
    if opcao==3:
        print("Você desistiu,e não capturou seu alvo. Fim do jogo!")
        break
    
