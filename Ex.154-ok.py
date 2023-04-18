placa = (input("Digite a placa: "))
#p = ultimo numero da placa do carro
p = placa[-1]
if (p == "1"):
    print("\nJaneiro")
elif (p == "2"):
    print("\nFevereiro")
elif (p == "3"):
    print("\nMarço")
elif (p == "4"):
    print("\nAbril")
elif (p == "5"):
    print("\nMaio")
elif (p == "6"):
    print("\nJunho")
elif (p == "7"):
    print("\nJulho")
elif (p == "8"):
    print("\nAgosto")
elif (p == "9"):
    print("\nSetembro")
elif (p == "0"):
    print("\nOutubro")
else:
    print("\nOpcao invalida")