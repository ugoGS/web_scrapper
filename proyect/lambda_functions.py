nombres = ["Juan", "María", "Carlos", "Ana", "Wazabee"]
nombres_ordenados_a_z = sorted(nombres)
nombres_ordenados_longitud = sorted(nombres, key=lambda x: len(x))
nombres_ordenados_longitud_alreves = sorted(nombres, key=lambda x: len(x), reverse=True)

def run():

    print(nombres_ordenados_longitud)
    print(nombres_ordenados_a_z)
    print(nombres_ordenados_longitud_alreves)

if __name__ == '__main__':
    run() 