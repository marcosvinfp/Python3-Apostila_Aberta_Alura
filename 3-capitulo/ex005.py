print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 42
pontuacao = 1000

nivel = int(input('''Escolha o nível de dificuldade: 
            [ 1 ] 20 tentativas
            [ 2 ] 10 tentativas
            [ 3 ] 05 tentativas
-->'''))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print(f'Tentativa {rodada} de {total_de_tentativas}')
    chute = int(input('Digite o seu número: '))
    print(f'Você digitou {chute}')

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print('Você acertou!')
        break
    elif (maior):
        print('Você errou! O seu chute foi maior que o número secreto')
    elif (menor):
        print('Você errou! O seu chute foi menor que o número secreto')
    
    pontuacao -= abs(numero_secreto - chute)
    rodada += 1
    print(f'Pontuação acumulada: {pontuacao}')
print('Fim do jogo')
