
filmes = []

for i in range (5):
    a = input("qual o nome do filme?")
    filmes.append (a)
count=0
print("foram cadastrados 5 filmes")
for i in filmes:
    count+=1
    print(count,"°",i)
