print('Bienvenido a la calculadora')
print('Para salir ingresa: salir')
print('Las operaciones disponibles son: suma, resta, multiplicacion, division')
resulado = ''
while True:
    if not resulado:
        resulado = input('Ingresa primer numero: ')
        if resulado.lower() == 'salir':
            break
        resulado = int(resulado)
    operacion = input('Ingresa tipo de operacion:')
    if operacion.lower() == 'salir':
        break
    numeroDos = input('Ingresa segundo numero: ')
    if numeroDos.lower() == 'salir':
        break
    numeroDos = int(numeroDos)
    if operacion == 'suma':
        resulado += numeroDos
    elif operacion == 'resta':
        resulado -= numeroDos
    elif operacion == 'multiplicacion':
        resulado *= numeroDos
    elif operacion == 'division':
        resulado /= numeroDos
    else:
        print('Operacion no valida')
        break
    print('El resultado es: ', resulado)