dia = int(input("\nDigite dia: "))
mes = int(input("\nDigite mes: "))
ano = int(input("\nDigite ano: "))
if (ano >=1):
    vd = True
    if(mes < 1 or mes > 12 or dia >30):
        vd = False
    elif((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30):
        vd = False
    elif(mes == 2):
        if(ano % 4==0 and ano % 100 != 0 and ano % 400==0):
            if(dia > 29):
                vd = False
        elif(dia > 28):
            vd = False 
else:
    vd = False
if (vd == False):
    print("Data invalida ")
else:
    print("Data valida ")           
            

