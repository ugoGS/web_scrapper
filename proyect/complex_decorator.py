import time

#Función que calcula el tiempo de ejecución de la función envuelta
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f'Function "{func.__name__}" took {elapsed_time:.6f} seconds')
        print('\n')
        return result
    return wrapper

#Función que comprueba si una cadena es palindromo
def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]


@execution_time
def palindromes():  #Función que imprime todos los palindromos del archivo de texto.
    with open("./names.txt", "r", encoding="utf-8") as f: 
        names = [linea.rstrip('\n') for linea in f]

    print(names)
    
    for linea in names:
        if is_palindrome(linea):
            print(linea + " es palindromo")    

@execution_time
def triangle(filas): #Función que imprime un triangulo de asteriscos
    asterisks = []
    for i in range(1, filas + 1):
        asterisks.append('*' * i)
    for i in range(len(asterisks)):
        print(asterisks[i])

@execution_time
def rectangle(filas): #Función que imprime un rectángulo de X y O
    for i in range(1, filas):
        print("X" * ((filas-1) - i) + "O" * i)
@execution_time
def rectangle_comprehesion(filas): #Función que imprime un rectángulo de X y O con compresión de listas
    [print("X" * ((filas-1) - i) + "O" * i) for i in range(1, filas)]

@execution_time
def print_numbers(range_number): # Función que imprime números del 1 al 5 cada segundo
    for i in range(1, range_number + 1):
        print(i)
        time.sleep(1)  # Espera 1 segundo entre cada número


if __name__ == '__main__':
    palindromes()
    triangle(6)
    rectangle(6)
    rectangle_comprehesion(6)
    print_numbers(5)
