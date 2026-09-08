pagar =  float(input("qual a conta do restaurante?"))
gorjeta = float(input("qual o percentual da gorjeta?(em porcentagem)"))



def calcular_gorjeta ():
    global total
    a = gorjeta /100
    conta = pagar * a
    total = conta + pagar 
    





calcular_gorjeta ()
print("total a pagar: R$",total)




