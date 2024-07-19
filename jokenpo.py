import random

hierarquia = {
    '1': 'papel',
    '2': 'tesoura',
    '3': 'pedra'
}

while True:
    jogador = input('Pedra [1], Papel [2], Tesoura [3]: ')
    pc = random.choice(['tesoura', 'papel', 'pedra'])

    if hierarquia[jogador] == pc:
        print(f'O pc jogou {pc} e você perdeu!')

    elif ['pedra','papel','tesoura'][int(jogador)-1] == pc:
        print(f'O pc também jogou {pc} e deu empate!')
 
    else:
        print(f'O pc jogou {pc} e você ganhou!')