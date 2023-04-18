import random

#Número aleatório de 0 a 10
numero_aleatorio = random.randint(0, 10)

#Número de Vidas(tentativas)
tentativas_maximas = 3
tentativas = 0

# Loop do jogo
while tentativas < tentativas_maximas:
    #Palpite do Usuário
    palpite = int(input("Adivinhe um número de 0 a 10: "))

    #Verificar o Palpite
    if palpite == numero_aleatorio:
        print("Parabéns! Você acertou o número!")
        break
    else:
        print("Que pena! Você errou o número.")
        tentativas += 1

        #Dica
        if tentativas < tentativas_maximas:
            if palpite < numero_aleatorio:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")

#Caso o usurário perca
if tentativas == tentativas_maximas:
    print("Você não conseguiu adivinhar o número. O número correto era {}.".format(numero_aleatorio))