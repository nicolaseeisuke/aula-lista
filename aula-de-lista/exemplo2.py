import os
os.system('cls')

notas = [6,7,6.5,4.8,8]
nomes = ['Nicolas','Marley','Matheus','João','Thiago']

soma = 0
cont = 0
for n in notas:
   soma += n
media = soma / len(notas)

print(f'total de notas é {soma} e a média é {media:.2f}')

for i in range(len(notas)):
   if notas[i] > media:
      cont += 1
print(f'{nomes[i]}')