nomes = []

for i in range(5):
    nome = input('Qual o seu nome? ')
    nomes.append(nome)

print(nomes)
print(len(nomes))

nome = input('Digite o nome do usúario: ')
nomes.remove(nome)
print(nomes)
print(len(nomes))