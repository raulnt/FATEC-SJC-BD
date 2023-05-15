x = float(input("Digite o valor de X :"))
if x <= 1.0:
    y = 1.0
elif x <= 2.0:
    y = 2.0
elif x <= 3.0:
    y = x **2
else:
    y = x **3

print("\nValor de f(x): ", y)