#Desenvolvido por Raul José Batista Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023

import random

# O Computador ira gerar dois números em um intevalo de 1 a 8:
num1 = random.randint(1, 8)
num2 = random.randint(1, 8)

# Hora da Soma, pergunte ao usuário o valor da SOMA:
soma = int(input("Qual o valor da soma de {} e {} : ".format(num1, num2)))

# Verificando o resultado
if soma == num1 + num2:
    print("PARABÉNS, você acertou!")
    print("Desenvolvido por Raul José Batista Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023")
else:
    print("QUE PENA, você errou.Tente novamente!")
    print("Desenvolvido por Raul José Batista Neto // FATEC SJC // Banco de Dados // 1° Semestre no ano de 2023")

# Em relação a Matemática Discreta, podemos visualizar em um simples jogo de Qual a SOMA. 
# Relações Binárias distintas em ralação aos números gerados a serem somados:
# Conjunto = (1, 2, 3, 4, 5, 6, 7, 8)
# (1,1); (1,2); (1,3); (1,4); (1,5); (1,6); (1,7); (1,8);
# (2,1); (2,2); (2,3); (2,4); (2,5); (2,6); (2,7); (2,8);
# (3,1); (3,2); (3,3); (3,4); (3,5); (3,6); (3,7); (3,8);
# (4,1); (4,2); (4,3); (4,4); (4,5); (4,6); (4,7); (4,8);
# (5,1); (5,2); (5,3); (5,4); (5,5); (5,6); (5,7); (5,8);
# (6,1); (6,2); (6,3); (6,4); (6,5); (6,6); (6,7); (6,8);
# (7,1); (7,2); (7,3); (7,4); (7,5); (7,6); (7,7); (7,8);
# (8,1); (8,2); (8,3); (8,4); (8,5); (8,6); (8,7); (8,8);