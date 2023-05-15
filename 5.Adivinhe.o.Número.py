#Desenvolvido por Raul José Batista Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023

import random

def numero():
    numero = random.randint(1, 4)
    tentativas = 0

    print("Bem-vindo ao jogo Adivinhe o Número!")
    print("Tente adivinhar o número que estou pensando, entre 1 e 3.")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero:
            print("Tente um número maior!")
        elif palpite > numero:
            print("Tente um número menor!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            print("Desenvolvido por Raul José Batista Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023")
            break

numero()

# Em relação a Matemática Discreta, podemos visualizar em um simples jogo de Advinhe o Número. 
# Os possíveis conjuntos de palpites para acertar o número:
# Acertando em 1 tentativa, os conjuntos possíveis seriam:
# (1); (2); (3);
# Acertando em 2 tentativas, os conjuntos possíveis seriam:
# (1,2); (1,3); 
# (2,1); (2,3);
# (3,1); (3,2);
# Acertando em 3 tentativas, os conjuntos possíveis seriam:
# (1,2,3); (1,3,2);
# (2,3,1); (2,1,3);
# (3,2,1); (3,1,2);
#Desenvolvido por Raul José Batista Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023

