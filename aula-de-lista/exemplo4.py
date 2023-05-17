import os
os.system('cls')

num = []
soma = 0
maior = 0
while True:
    n = int(input("Digite um número inteiro (0 sair)"))
    if n == 0: break 
    num.append(n)
    soma += n

for n in num:
    if n  > maior:
        maior = n
media = soma/len(num)
print(f'A média é {media:.2f}')
print(f'O maior n° digitado é {maior}')
print(num)