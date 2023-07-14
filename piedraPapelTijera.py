import random

print(f'1: Piedra\n2: Papel\n3: Tijera')
player = int(input('Ingrese su elección: '))
computer = random.randint(1, 3)

def game(player, computer):
    if player == computer:
        print('Empate, ambos eligieron lo mismo')
    elif player == 1 and computer == 2:
        print('Perdiste, la computadora eligió papel')
    elif player == 1 and computer == 3:
        print('Ganaste, la computadora eligió tijera')
    elif player == 2 and computer == 1:
        print('Ganaste, la computadora eligió piedra')
    elif player == 2 and computer == 3:
        print('Perdiste, la computadora eligió tijera')
    elif player == 3 and computer == 1:
        print('Perdiste, la computadora eligió piedra')
    elif player == 3 and computer == 2:
        print('Ganaste, la computadora eligió papel')
    else:
        print('Opción inválida')

game(player, computer)