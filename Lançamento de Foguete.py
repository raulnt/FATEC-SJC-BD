#Contagem Regressiva
import time

print("O foguete será lançado em: ")
time.sleep(2)

#Número inicial da contagem
contador = 10

#Loop de contagem do 10 ao 0
while contador >= 0:
    print(contador)
    time.sleep(1) #Intervalo(EM SEGUNDOS) de um número para o outro
    contador -= 1

print("Foguete Lançado!!!")
