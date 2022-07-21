def run():
    dicc = {
        'k1': 1,
        'k2': 2,
    }

    #print(dicc)
    for key, val in dicc.items():
        print('Llave: ' + key + ' Valor: ' + str(val))
    print('Diccionario:')
    print(dicc)

if __name__ == '__main__':
    run()
