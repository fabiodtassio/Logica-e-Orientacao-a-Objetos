# SOFTEX-RECIFE
# Aluno: Fábio de Tássio

# Atividade 02 do módulo 02 (Dominar as diferentes estruturas condicionais lógicas)

# Desenvolva um código que utilize as seguintes características de um veículo:
# - Quantidade de rodas;
# - Peso bruto em quilogramas;
# - Quantidade de pessoas no veículo.
# Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
# A: Veículos com duas ou três rodas;
# B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
# C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
# D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
# E: Veículos com quatro rodas ou mais e com mais de 6000 kg

# Ínicio
qtd_rodas = int(input('Digite a quantidade de rodas:'))
qtd_pessoas = int(input('Digite a quantidade de pessoas:'))
Peso = int(input('Didite o peso do veículo:'))

if qtd_rodas == 2 or qtd_rodas == 3:
    print('Categoria A')
elif qtd_rodas == 4 and qtd_pessoas <= 8 and Peso <= 3500:
    print('Categoria B')
elif qtd_rodas >= 4 and qtd_pessoas <= 8 and Peso >= 3500 and Peso <= 6000:
    print('Categoria C')
elif qtd_rodas >= 4 and qtd_pessoas > 8 and Peso <= 6000:
    print('Categoria D')  
elif qtd_rodas >= 4 and Peso > 6000:
    print('Categoria E')
else:
    print('O veículo não se enquadra em nenhuma categoria!')    
