#Exercicio 1
numero = int(input('Insira um numero: '))
if numero%2 == 0:
    print('par')
else:
    print('impar')

#Exercicio 2
idade = int(input('Insira sua idade: '))
if 0 <= idade <= 12:
    print('Classificação: criança') 
elif 13 <= idade <= 18:
    print('Classificação: adolescente')
else:
    print('Classificação: adulto')        

#Exercicio 3
nome = input('Insira um nome de usuáirio: ')
senha = input('Insira a senha:')
if nome == 'user' and senha == '1234':
    print('corresponde')
else:
    print('diferentes')

#Exercício 4
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")
