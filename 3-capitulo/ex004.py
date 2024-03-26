print('******************************')
print('*    Jogo da adivinhação     *')
print('******************************')

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while total_de_tentativas >= rodada:
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
    
    rodada += 1
print('Fim do jogo')
