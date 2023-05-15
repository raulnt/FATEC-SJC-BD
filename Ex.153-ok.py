indice = float(input("\nDigite indice de poluicao: "))
if (indice >= 0.5):
    print("\nSuspender atividades das industrias dos grupos 1, 2 e 3")
elif (indice >=0.4):
    print("\nSuspender atividades das industrias dos grupos 1 e 2 ")
elif (indice >=0.3):
    print("\nSuspender atividades das industrias dos grupos 1 ")
else:
    print("\nIndice de poluicao aceitavel para todos os grupos ")
