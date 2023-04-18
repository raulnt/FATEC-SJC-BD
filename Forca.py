#Escolha da palavra(no caso um pessoa que escolhe)
palavra = input("Digite a palavra: ")
forca = ['_'] * len(palavra)

erros = 0

#Estrutura das Ações
while True:
    print(' '.join(forca))
    letra = input("Digite uma letra: ")
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                forca[i] = letra
        if '_' not in forca:
            print("Você ganhou!")
            break
    else:
        erros += 1
        print("Você errou pela {}ª vez.".format(erros))
        if erros == 6:
            print("Você perdeu!")
            break