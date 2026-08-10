
total = 0
preco = None

while preco != 0:
    preco =float(input("qual o valor do produto"))
    print("")
    total += preco 

print("o valor total da compra é de: R$",total)