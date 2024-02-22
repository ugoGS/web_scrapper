import threading
import time

# Función que imprime números del 1 al 5
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)  # Espera 1 segundo entre cada número

# Función que imprime números del 1 al 5 y el hilo de ejecucion
def print_numbers_threads():
    # Obtener el nombre del hilo actual
    thread_name = threading.current_thread().name
    print(f'Hilo {thread_name} iniciado')
    
    for i in range(1, 6):
        print(f'{thread_name}: {i}')
        time.sleep(1)  # Espera 1 segundo entre cada número

    print(f'Hilo {thread_name} terminado', end='\n')



# Creamos dos hilos que ejecutan la función print_numbers
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Creamos dos hilos que ejecutan la función print_numbers_threads
thread3 = threading.Thread(target=print_numbers_threads)
thread4 = threading.Thread(target=print_numbers_threads)

# Iniciamos los hilos 1 y 2
thread1.start()
thread2.start()

# Esperamos a que ambos hilos terminen antes de continuar
thread1.join()
thread2.join()

# Iniciamos los hilos 3 y 4
thread3.start()
thread4.start()

# Esperamos a que ambos hilos terminen antes de continuar
thread3.join()
thread4.join()

print("Fin de los hilos")