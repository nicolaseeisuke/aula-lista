import os
os.system('cls')

nomes = []
nota = []
while True:
    nome = input("Qual o nome do aluno? ")
    n1 = float(input(f'Qual a 1° nota do {nome}: '))
    n2 = float(input(f'Qual a 2° nota do {nome}: '))
    media = (n1+n2)/2
    nomes.append(nome)
    nota.append(media)

    resp = input("deseja continuar ?").upper()
    if resp == 'N':break
print(10*'-')
for i, e in enumerate(nomes):
    print(f'[{i}]- {e}')
print(10*'-')

print(10*'-')
i = int(input("Qual o aluno deseja consultar ? "))
#resultado = 'Aprovado' if nota[i] > 6 else 'Reprovado
if nota[i] > 6:
    print(f'O aluno {nomes[i]} foi aprovado ')
else:
    print(f'O aluno {nomes[i]} foi reprovado')
print(f'Média: {nota[i]:.2f}')
