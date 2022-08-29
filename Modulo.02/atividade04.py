# SOFTEX-RECIFE
# Aluno: Fábio de Tássio

# Atividade 04 do Módulo 02 (Executar funções de códigos)

# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da
# operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

# Início

def calculadora(num01, num02, oper):
    if oper == 1:
        calc = num01 + num02
    elif oper == 2:
        calc = num01 - num02
    elif oper == 3:
        calc = num01 * num02
    elif oper == 4:
        calc = num01 / num02
    else: 
        calc = 0
    return(calc)

num01 = 12
num02 = 3
print('\n')
oper = int(input('Digite 1 - soma | 2 - subtração | 3 - multiplicação | 4 - divisão \n'))
resultado = calculadora(num01,num02, oper)
print('Resultado:',resultado)
print('\n')