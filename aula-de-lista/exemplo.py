import os
os.system('cls')

nomes = []
nota = []

n = int(input('Qual a quantidade de alunos ? '))
for i in range(n):
    nome = input("Qual o nome do aluno? ")
    n1 = float(input(f'Qual a 1° nota do {nome} : '))
    n2 = float(input(f'Qual a 2° nota do {nome}: '))
    media = (n1+n2)/2
    nomes.append(nome)
    nota.append(media)

    
print(10*'-')
for i, e in enumerate(nomes):
    print(f'[{i}]- {e}')
print(10*'-')

print(10*'-')
i = (input("Qual o nome do aluno?  "))
i = nomes.index(nome)
resultado = 'Aprovado' if nota[i] > 6 else 'Reprovado'
print(f'O aluno {nomes[i]} foi {resultado} ')
print(f'Média: {nota[i]:.2f}')
