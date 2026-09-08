n1= int(input("digite um numero"))
codigo = 1234
while n1 != codigo:
    if n1 < codigo:
        print("numero que eu quero é maior ")
    else:
        print("numero que eu quero é menor ")
    n1= int(input("digite outro"))
print("voce acertou")