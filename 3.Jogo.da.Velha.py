#Desenvolvido por Raul José Batista Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023



#Criação do Tabuleiro
tabuleiro = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

#Jogador 1
jogador = "X"
jogando = True

def exibir_tabuleiro():
    for linha in tabuleiro:
        print(" ".join(linha))

#Jogadas
def jogada():
    global jogador
    linha = int(input("Escolha a linha (0, 1 ou 2): "))
    coluna = int(input("Escolha a coluna (0, 1 ou 2): "))
    if tabuleiro[linha][coluna] == "-":
        tabuleiro[linha][coluna] = jogador
        if vencedor():
            print(f"Parabéns, o jogador {jogador} venceu!")
            print("Desenvolvido por Raul José Batista Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023")

            global jogando
            jogando = False
        jogador = "X" if jogador == "O" else "O"
    else:
        print("Essa posição já está ocupada, tente novamente.")

#Vence quem
def vencedor():
    # Verifica linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] != "-":
            return True
    # Verifica colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != "-":
            return True
    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != "-":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != "-":
        return True
    return False

while jogando:
    exibir_tabuleiro()
    jogada()

exibir_tabuleiro()

# Em relação a Matemática Discreta, podemos visualizar em um simples jogo da Velha. 
# Na função 'vencedor()' usa relações verdadeiras e falsas da matemática discreta para verificar se algum jogador venceu o jogo. Ela verifica todas as possíveis linhas, colunas e diagonais do tabuleiro. São chamadas de operações lógicas discretas.
