registros={}
b=0
def interface():
    print("escolha uma das opçoes")
    print("1-cadastrar cliente ")
    print("2-alterar o registro")
    print("3-viualizar todos os registros")
    print("4-deletar cliente ")
    print("5-sair")
    a = int(input(""))
    return a
    


def cadastroDeCliente():
    nome= input("qual o nome do cliente")
    idade= int(input("qual a idade do cliente"))
    telefone=input("qual o telefone do cliente?")
    if idade < 18:
        print("cliente não foi cadastrasdo pq ele é de menor")
    else:
        
        registros [nome]={"idade":idade,"telefone":telefone}
        print("NOVO REGISTRO ADICIONADO COM SUCESSO!") 
    return nome,idade,telefone,registros
    
    
def alteracao():
    
    quem = input("quem voce deseja alterar?")
    print("insira o novo registro")
    nome_novo= input("insira o novo nome do cliente")
    idade= int(input("insira a idade do cliente"))
    telefone=input("insira o telefone do cliente?")
    if idade >18:
        del registros [quem] 
        registros [nome_novo]={"idade":idade,"telefone":telefone}
        print("ALTERAÇÃO FEITA COM SUCESSO")
    else:
        del registros [quem] 
        print("cliente foi excluido pois ele é d menor")
        
        

def deletar():
    quem = input("quem voce deseja deletar")
    del registros [quem]
    print("DELETADO COM SUCESSO")
  




while b != 5:
    b =interface()
    if b == 1:
        print("")
        cadastroDeCliente()
        print("")


        

    elif b== 2:
        print("")
        alteracao()
        print("")




    elif b== 3:
        print(registros)
        print("")
        print("")

    elif b == 4:
        print("")
        deletar()
        print("")
    
print("ADEUS")

