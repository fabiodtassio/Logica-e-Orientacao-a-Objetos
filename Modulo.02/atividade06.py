#  SOFTEX-RECIFE
# Aluno: Fábio de Tássio

# Atividade 05 do Módulo 04 (Contornar problemas previstos no sistema)

# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. 
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará,
# no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará 
# perguntando até que um valor correto seja preenchido.

# Início

def func_AnoNasc(AnoNasc):
    if AnoNasc >= 1922 and AnoNasc <= 2021:
        Idade = 2022 - AnoNasc
    elif AnoNasc < 1922 or AnoNasc > 2021:
        raise Exception('Ano inválido!!!')
    return Idade

Nome = input('Digite seu nome completo: \n')
while True:
    try:
        AnoNasc = int(input('Digite o ano de nascimento que seja entre 1922 e 2021:\n'))
        Idade = func_AnoNasc(AnoNasc)
        print(Nome, 'sua idade é', Idade, 'ano(s) em 2022!')
        break
    
    except ValueError:
        print('ERRO!!!')
        print('\n')

    except Exception as err:
        print(err)  
        print('\n')   