lista=[]
a=0
def interface():
    global a
    print("escolha uma das opçoes")
    print("1-adicionar itens ")
    print("2-alterar itens")
    print("3-viualizar todos os itens")
    print("4-deletar itens ")
    print("5-sair")
    a = int(input(""))
    
    


def adicionar_itens():
    global add_iten,lista,add_iten
    add_iten=input("digite o item que deseja adicionar")
    lista.append (add_iten)
    print(lista)
    
    
    
def alterar_iten():
    global qual
    qual = input("Qual item deseja alterar? ")
    lista.remove(qual)
    novo = input("Digite o novo item: ")
    lista.append(novo)
    
   
def remover ():
    global lista, remover
    remover=input("qual item voce deseja remover?")
    lista.remove (remover)
    
    
    

while a != 5:
    interface()
    if a == 1:
        adicionar_itens()
        
    elif a == 2 :
        alterar_iten()


    elif a == 3:
        print(lista)
        
    elif a== 4:
        remover ()
       


    else:
        print("thau")