peso = float(input("Digite o peso: "))
idade = int(input("Digite a idade: "))
gotas = 500 / 20 #mg em gotas

if (peso <5.):
    print("\n Não pode tomar o remédio porque não tem peso. Consulte um médico.")
elif (idade >= 12, peso >=60.):
    print("\nTomar ", 1000 / gotas, " gotas")
elif (idade < 12, peso <60.):
    print("\nTomar ", 875 /gotas, " gotas")
elif (peso <= 9.):
    print("\nTomar ", 125 / gotas, " gotas")
elif (peso <=16.):
    print("\nTomar ", 250 / gotas, " gotas")
elif (peso <=24.):
    print("\nTomar ", 375 / gotas, " gotas")
elif (peso <=30.):
    print("\nTomar ", 500 / gotas, " gotas")
else:
    print("\nTomar ", 750 / gotas, " gotas")
