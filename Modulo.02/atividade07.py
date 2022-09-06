# Desenvolva um código que simule uma eleição com três candidatos.
# - candidato_X => 889
# - candidato_Y => 847
# - candidato_Z => 515
# - branco => 0

# O código deve perguntar se deseja finalizar a votação depois do voto. Caso o número do voto não corresponda a nenhum
# candidato ou seja branco, ele deve ser tratado como nulo. Se for inserido um texto ao invés de número, o código deve
# retornar uma mensagem para votar novamente.

# Quando a votação for finalizada, o código deverá mostrar o vencedor, aquele com o maior número de votos e, também, a
# quantidade de votos de cada candidato, os brancos e nulos.

# Início

import enum

class candidatos (enum.Enum):
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    branco = 0

qtd_X = qtd_Y = qtd_Z = qtd_branco = 0


while True:
    try:
        print('\n')
        print('CANDIDATOS DA ELEIÇÃO:')
        print(candidatos.candidato_X.name, '-',candidatos.candidato_X.value)
        print(candidatos.candidato_Y.name,'-',candidatos.candidato_Y.value)
        print(candidatos.candidato_Z.name,'-',candidatos.candidato_Z.value)
        print(candidatos.branco.name,'-',candidatos.branco.value,'\n')
        voto = int(input('Digite o número do seu candidato: \n')) 
        if voto == candidatos.candidato_X.value:
            conf = int(input('Confirme seu voto digitando o número: 1 - SIM | 2 - NÃO \n'))
            if conf == 1:
                qtd_X += 1  
        elif voto == candidatos.candidato_Y.value:
            conf = int(input('Confirme seu voto digitando o número: 1 - SIM | 2 - NÃO \n'))
            if conf == 1:
                qtd_Y += 1   
        elif voto == candidatos.candidato_Z.value:
            conf = int(input('Confirme seu voto digitando o número: 1 - SIM | 2 - NÃO \n'))
            if conf == 1:
                qtd_Z += 1
        elif voto == 0:
            conf = int(input('Confirme seu voto digitando o número: 1 - SIM | 2 - NÃO \n'))
            if conf == 1:
                qtd_branco += 1
        else:
            print('Voto nulo!!!')
            conf = int(input('Confirme seu voto digitando o número: 1 - SIM | 2 - NÃO \n'))
            if conf == 1:
                qtd_branco += 1              
       
        fim = input('Deseja finalizar a votação? (s - SIM) ou (n - NÃO") \n')
        if fim != 's':
            continue
        else:
            print('VOTAÇÃO FINALIZADA!!! \n')
            break
                                       
    except ValueError:
        print('\n')
        print('Você digitou algo diferente de um número!!! \n')

print('CONTAGEM DOS VOTOS:')
print(candidatos.candidato_X.name, '-' ,qtd_X,'votos' )
print(candidatos.candidato_Y.name, '-' ,qtd_Y,'votos')
print(candidatos.candidato_Z.name, '-' ,qtd_Z,'votos')
print(candidatos.branco.name, '-' ,qtd_branco,'votos (somando brancos e nulos)')
if (qtd_X > qtd_Y) and (qtd_X > qtd_Z):
    print(candidatos.candidato_X.name, 'venceu a eleição com a maior quantidade de votos' ,qtd_X, '\n')
elif (qtd_Y > qtd_X) and (qtd_Y > qtd_Z):
    print(candidatos.candidato_Y.name, 'venceu a eleição com a maior quantidade de votos' ,qtd_Y, '\n') 
elif (qtd_Z > qtd_X) and (qtd_Z > qtd_Y):      
    print(candidatos.candidato_Z.name, 'venceu a eleição com a maior quantidade de votos' ,qtd_Z, '\n')      
else:     
    print('Votação empatada,vamos para o segundo turno!!! \n')
    print('\n')
    