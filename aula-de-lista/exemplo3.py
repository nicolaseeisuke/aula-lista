import os
os.system('cls')


nomes = []
for i in range(5):
   nome = input('Qual o nome da pesso ? ')
   nomes.append(nome)
print(nomes)

print(10*'-')
n = int(input("Quem você quer exibir?"))

print(nomes[n])