# Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidad de faltas que ele teve. Conclua se o aluno está aprovado ou reprovado de acordo com as especificações:

# - Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
# - Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado;
# - Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado.

# No sistema, todos os valores devem estar armazenados em variáveis.
# Programa para verificar se o aluno foi aprovado ou reprovado

#Início
Nome = input('Digite seu nome: ')
Nota01 = float(input('Digite a primeira nota: '))
Nota02 = float(input('Digite a segunda nota: '))
Faltas = int(input('Digite quantas faltas você tem: '))

Media = (Nota01 + Nota02) / 2  
if Faltas > 3:
    print('Faltas:', Faltas)
    print(Nome,', infelizmente você foi reprovado(a) por exceder a quantidade de faltas permitidas (3 faltas)!')
elif Media < 7:
    print('Média:', Media)
    print(Nome,', infelizmente você foi reprovado(a) por não alcançar a pontuação mínima na média (7.0 pontos)!') 
else: 
    print(Nome, ', você foi aprovado(a)!') 
    print('Sua média foi:', Media)
    print('Parabéns!!!')