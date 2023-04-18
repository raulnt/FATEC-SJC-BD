palavra = str(input("\n Digite uma palavra: "))
letra = palavra[0]
if (letra =="l" or letra == "L" or letra == "d" or letra == "D"):
    palavra1 = palavra [1]
    palavra2 = palavra [-1]
    palavraaux = letra + palavra1 + palavra2
    print(f'a palavra e {palavra2}')
    print(f'a palavra e {palavraaux}')
else:
    palavra1 = palavra [1:]
    print(f'a palavra e {palavra1}')

