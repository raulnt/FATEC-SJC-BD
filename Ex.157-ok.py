data = int(input("Data no formato ddmmaaaa: "))
dia = data // 1000000
mes = data % 1000000 // 10000
ano = data % 10000
if(ano >=1):
    vd = True
    if (mes > 12 or dia < 1 or dia > 31):
        vd = False
    elif((mes == 4 or mes == 6 or mes == 9 or mes == 11) or dia > 30):
        vd = False
    elif(mes == 2):
        if ((ano % 4==0 and ano % 100 != 0) or ano % 400==00):
            if(dia > 29):
                vd = False
            elif(dia > 28):
                vd = False
elif():
    vd = False
if(vd == 0):
    print("\nData invalida")
else:
    print("\nData valida")



