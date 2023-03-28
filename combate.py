from random import randint

vidaUno = 100
vidaDos = 90

while vidaUno > 0 and vidaDos > 0:
    #primer peleador:
    print('ataque primer peleador')
    #genera numero entre 1 y dos:
    ataqueUno = randint(1, 2)
    if ataqueUno == 1:
        print('ataque')
        vidaDos -= 10
    else:
        print('ataque')
        vidaDos -= 10
    
    #segundo peleador:
    print('ataque segundo peleador')
    ataqueDos = None
    while ataqueDos != 'a' and ataqueDos != 'b' and ataqueDos != 'c':
        ataqueDos = input('ataque a realizar: a)golpe, b)patada, c)tirada: ')

    if ataqueDos == 'a'or 'b' or 'c':
        vidaUno -= 10

    print(f'vida p1: {vidaUno} y p2: {vidaDos}')

if vidaUno > vidaDos:
    print('el peleador uno ha ganado')
else:
    print('el peleador dos ha ganado')