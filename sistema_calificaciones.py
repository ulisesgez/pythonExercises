calificacion = int(input('Introduce una calificacion entre 0 y 10: '))
#Equivalente:
#if  calificacion >= 9 and calificacion <= 10:
if 9 <= calificacion <= 10:
    print('A')
elif 8 <= calificacion <= 9:
    print('B')
elif 7 <= calificacion <= 8:
    print('C')
elif 6 <= calificacion <= 7:
    print('D')
elif 0 <= calificacion < 6:
    print('F')
else:
    print('Incorrecto')
