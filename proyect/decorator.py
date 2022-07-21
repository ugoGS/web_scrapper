def decorador(func):
    def envoltura():
        print('Append')
        func()
    return envoltura

'''
def saludo():
    print('Hi!')
    
saludo = decorador(saludo)
'''
#Syntactic sugar 

@decorador
def saludo():
    print('Hi!')

if __name__ == '__main__':
    saludo()



