lista = []

def adicionar():
    a = input("qual o nome do produto que voce deseja adicionar na lista?")
    lista.append (a)
    print (lista)
    print ("")
    menu()

def remover():
    a = input("qual iten voce deseja remover na lista?")
    lista.remove (a)
    print (lista)
    print ("")
    menu()

def menu():
    print("faça uma escolha (1,2)")
    print("1- adicionar itens na lista")
    print("2- remover itens na lista")
    escolha = input("ou digite qualque coisa para vizualizar a lista")
    if escolha == "1":
        adicionar()

    elif escolha == "2":
        remover()

    else:
        print(lista)
        menu()

menu()











































