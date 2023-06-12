import random

# Define o tamanho do tabuleiro
TAMANHO_TABULEIRO = 5

# Cria uma matriz vazia
tabuleiro = [[0 for x in range(TAMANHO_TABULEIRO)] for y in range(TAMANHO_TABULEIRO)]

# Define a posição do navio aleatoriamente
navio_linha = random.randint(0, TAMANHO_TABULEIRO-1)
navio_coluna = random.randint(0, TAMANHO_TABULEIRO-1)

# Loop principal do jogo
while True:
    # Exibe o tabuleiro
    for linha in tabuleiro:
        print(" ".join(str(coluna) for coluna in linha))
    
    # Pede ao jogador para adivinhar a posição do navio
    palpite_linha = int(input("Digite a LINHA do seu palpite (0-4): "))
    palpite_coluna = int(input("Digite a COLUNA do seu palpite (0-4): "))
    
    # Verifica se o palpite acertou o navio
    if palpite_linha == navio_linha and palpite_coluna == navio_coluna:
        print("Parabéns, você acertou o navio!")
        break
    else:
        print("Você errou o navio.")
        # Marca o palpite no tabuleiro
        tabuleiro[palpite_linha][palpite_coluna] = "X"

