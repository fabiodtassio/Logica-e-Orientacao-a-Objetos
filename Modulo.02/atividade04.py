# SOFTEX-RECIFE
# Aluno: Fábio de Tássio

# Atividade 04 do Módulo 04 (Executar função de códigos)

# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da
# operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

# Início

def calculadora(num1, num2, oper):
    if oper == 1:
        calc = num1 + num2
        return(calc)
    elif oper == 2:
        calc = num1 - num2
        return(calc)
    elif oper == 3:
        calc = num1 * num2
        return(calc)
    elif oper == 4:
        calc = num1 / num2
        return(calc)
    else: 
        calc = 0
        return(calc)

num1 = 3
num2 = 7
oper = int(input('Digite 1 - soma, 2 - subtração, 3 - multiplicação, 4 - divisão:'))
resultado = calculadora(num1,num2, oper)
print(resultado)