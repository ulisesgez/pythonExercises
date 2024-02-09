from random import randint

vidaUno = 100
vidaDos = 100

while vidaUno > 0 and vidaDos > 0:
    #primer peleador:
    print('ataque primer peleador')
    #randint genera numero entre 1 y 10:
    ataqueUno = randint(1, 10)
    vidaDos -= ataqueUno
    
    #segundo peleador:
    print('ataque segundo peleador')
    seleccion = None
    while seleccion != 'a' and seleccion != 'b' and seleccion != 'c':
        seleccion = input('ataque a realizar: a)golpe, b)patada, c)tirada: ')

    if seleccion == 'a'or 'b' or 'c':
        ataqueDos = randint(1, 10)
        print('ataque segundo peleador')
        vidaUno -= ataqueDos

    print(f'vida p1: {vidaUno} y p2: {vidaDos}')

if vidaUno > vidaDos:
    print('el peleador uno ha ganado')
else:
    print('el peleador dos ha ganado')