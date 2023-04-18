import random

#Escolhas
opcoes = ["pedra", "papel", "tesoura"]

#Jogadores
jogada_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
jogada_computador = random.choice(opcoes)

print("Você jogou " + jogada_jogador)
print("Computador jogou " + jogada_computador)

#Resultados
if jogada_jogador not in opcoes:
    print("Jogada inválida.")
elif jogada_jogador == jogada_computador:
    print("Empate!")
elif jogada_jogador == "pedra":
    if jogada_computador == "papel":
        print("Você perdeu!")
    else:
        print("Você venceu!")
elif jogada_jogador == "papel":
    if jogada_computador == "tesoura":
        print("Você perdeu!")
    else:
        print("Você venceu!")
elif jogada_jogador == "tesoura":
    if jogada_computador == "pedra":
        print("Você perdeu!")
    else:
        print("Você venceu!")