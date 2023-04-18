#Função de Soma
def add(x, y):
    return x + y

#Função de Subtração
def subtract(x, y):
    return x - y

#Função da Multiplicação
def multiply(x, y):
    return x * y

#Função da Divisão
def divide(x, y):
    return x / y

#Opções da Calculadora
print("Selecione a operação")
print("1.Somar")
print("2.Subtrair")
print("3.Multiplicar")
print("4.Dividir")

#Seleção do Usuário
choice = input("Digite sua escolha (1/2/3/4): ")

#Número inserido pelo Usuário
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

#Execução da operação
if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=",subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=",multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Opção inválida!")