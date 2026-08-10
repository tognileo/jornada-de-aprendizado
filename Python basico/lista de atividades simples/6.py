lista=[]
maior= None
for i in range (6):
    aluno = float(input("qual a nota do aluno"))
    if aluno >10:
        print("a nota maxima é 10")
    else:
        lista.append (aluno)

menor = 10
maior =0
for i in lista:
    if i >maior:
        maior = i


for i in lista:
    if i < menor:
        menor = i 


print("a nota menor é",menor)
print("a note maior é" ,maior)
conta = 0

for i in  lista:
    conta +=i
resultado = conta /6
print ("a media da turma é ",resultado)

