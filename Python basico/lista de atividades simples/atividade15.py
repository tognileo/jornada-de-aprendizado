
def calculadora ():
    global a
    a = float(input("qual a velocidade que tava o carro"))


    if a <= 40:
        print("lento")

    elif a >=41 and a <=80:
        print("normal")

    elif a >=81 and a <= 120:
        print("rapido")

    else:
        print("muito rapido")


calculadora ()



















    