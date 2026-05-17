# Exercício 4
# Leia duas notas e informe se o aluno foi aprovado (>=7) ou reprovado.

# escreva seu código abaixo



n1 = float(input('Digite sua Nota: '))
n2 = float(input('Digite sua Nota: '))

def calcularmedia (n1, n2):
    soma = n1 + n2
    media = soma /2 
    if media >= 7:
        print('Aprovado')
    elif media == 6 :
        print('Recuperação')
    else:
        print('Reprovado')

calcularmedia(n1, n2)
