import random

def generar():
    may = ['A', 'P', 'M']
    min =['a', 'e', 'i']
    simb = ['/', '$']
    num = ['1', '9', '0']

    caracteres = may + min + simb + num

    contrasenia = []

    for i in range(12):
        caracter_random = random.choice(caracteres)
        contrasenia.append(caracter_random)

    contrasenia = "".join(contrasenia)

    return contrasenia

def run():
    contrasenia = generar()
    print('Contraseña generada: ' + contrasenia)

if __name__ == '__main__':
    run()