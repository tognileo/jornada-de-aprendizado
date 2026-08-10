
print("altura em metros")
peso = float(input("qual seu peso"))
altura = float(input("qual seua altura"))
def imc():
    global peso, altura,conta
    conta = peso/(altura*altura) 
    print(conta)


imc ()

def funcao ():
    global peso, altura,conta
    if conta <= 18.5:
        print("abaixo do peso")
        
    elif conta >=18.5 and conta <= 24.8:
        print("peso normal")
    else:
        print("sobrepeso")



funcao ()