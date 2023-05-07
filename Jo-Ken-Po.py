import random

#Escolhas possíveis
opcoes = ["pedra", "papel", "tesoura"]

#Jogadores
jogada_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
jogada_computador = random.choice(opcoes)

print("Você jogou " + jogada_jogador)
print("Computador jogou " + jogada_computador)

#Resultados possíveis
if jogada_jogador not in opcoes:
    print("Jogada inválida.")
    print("Desenvolvido por Raul Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023")
elif jogada_jogador == jogada_computador:
    print("Empate!")
    print("Desenvolvido por Raul Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023")
elif jogada_jogador == "pedra":
    if jogada_computador == "papel":
        print("Você perdeu!")
        print("Desenvolvido por Raul Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023")
    else:
        print("Você venceu!")
        print("Desenvolvido por Raul Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023")
elif jogada_jogador == "papel":
    if jogada_computador == "tesoura":
        print("Você perdeu!")
        print("Desenvolvido por Raul Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023")
    else:
        print("Você venceu!")
        print("Desenvolvido por Raul Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023")
elif jogada_jogador == "tesoura":
    if jogada_computador == "pedra":
        print("Você perdeu!")
        print("Desenvolvido por Raul Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023")
    else:
        print("Você venceu!")
        print("Desenvolvido por Raul Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023")

        # '''Em relação a Matemática Discreta, podemos visualizar em um simples jogo de Jo-Ken-Po. 
        # Relações Binárias a partir do possíveis resultados:
        # Conjuto = (Pedra, Papel e Tesoura)
        # (Pedra, Papel); (Pedra, Tesoura); (Pedra, Pedra)
        # (Papel, Papel); (Papel, Tesoura); (Papel, Pedra)
        # (Tesoura, Papel); (Tesoura, Tesoura); (Tesoura, Pedra)
