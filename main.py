import random

opcao = int(input(''' 
        Escolha sua opção:
        [ 1 ] Frente
        [ 2 ] Esquerda
        [ 3 ] Direita
        [ 4 ] Voltar
    '''))

while  True:
    if opcao == 1:
        num = random.randint(1, 10)
        print(num)
        if num == 5:
            print("Voce chegou no final!!!")
        else:
            comb = "g10"
            opcao = input("Voce não chegou no fim! Escolha entre as opções abaixo para prosseguir: ")

    if opcao == 2:
