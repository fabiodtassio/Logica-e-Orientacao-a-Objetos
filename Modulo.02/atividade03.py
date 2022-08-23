# SOFTEX-RECIFE
# Aluno: Fábio de Tássio

# Atividade 03 do módulo 02

# Faça um código que execute a contagem regressiva de uma bomba, informando o número de segundos para explodir.
# Ele deverá mostrar a mensagem “iniciando contagem regressiva”, os segundos passados e, no final, a mensagem “BUM!”.
# Nã0 é necessário, mas, caso deseje tornar o sistema mais realista para que o tempo realmente passe em segundos, 
# você pode usar a função time.sleep() que existe na Python. No entanto, é preciso adicionar uma biblioteca antes de executá-la. 

# Início

import time                                  # Biblioteca usada p/ utilizar a função time.

print('"Iniciando contagem regressiva"')
time.sleep(2)                                # Função usada para adicionar atraso na execução de um programa.
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)

print('BUMMMMM!')    
print('Momento exato da explosão:')
print(time.ctime())                          # Função usada para adicionar data e hora.
