#  SOFTEX-RECIFE
# Aluno: Fábio de Tássio

# Atividade 05 do Módulo 04 (Executar função de códigos)

# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando 
# infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
#
# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a
# mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa
# executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar. 

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 


# Início 

def calculadora(num01, num02, operacao):    # função calculadora
    if operacao == 1:
        calc = num01 + num02
        return (calc)
    elif operacao == 2:
        calc = num01 - num02
        return (calc)
    elif operacao == 3:
        calc = num01 * num02
        return (calc)
    elif operacao == 4:
        calc = num01 / num02
        return (calc)

while True:
    print('\n')
    operacao = int(input('Digite 1 - Soma | 2 - Subtração | 3 - Multiplicação | 4 - Divisão | 0 - SAIR \n'))
    if operacao == 1 or operacao == 2 or operacao == 3 or operacao == 4:
        num1 = int(input('Digite o primeiro número:\n'))
        num2 = int(input('Digite o segundo número:\n'))
        resultado = calculadora(num1, num2, operacao)
        print('Resultado:',resultado)
    elif operacao == 0:
        break
    else:
        print('Essa opção não existe!!!\n')
print("- Calculadora encerrada! -")    
