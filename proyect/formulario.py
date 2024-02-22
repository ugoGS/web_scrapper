'''
El código define una clase PersonalData que representa información personal de una persona, como nombre, apellido, edad, altura y nacionalidad. 
La clase tiene propiedades (con sus correspondientes setters) para cada uno de estos atributos, lo que permite acceder 
y modificar estos datos de manera controlada.

Después de definir la clase PersonalData, el código incluye dos funciones: persona1 y personas. 
Ambas funciones leen datos de un archivo de texto llamado "datos_personas.txt", que se asume tiene un formato específico de CSV (valores separados por comas), donde cada línea representa los datos de una persona en el siguiente orden: nombre, apellido, edad, altura y nacionalidad.

La función persona1 lee solo la primera línea del archivo y crea una instancia de PersonalData con esos datos. 
Luego imprime los datos de la persona.
La función personas lee todas las líneas del archivo, crea una lista de instancias de PersonalData para cada persona y la imprime.
Finalmente, en el bloque if __name__ == '__main__':, se llama a ambas funciones para demostrar cómo funcionan.
'''

class PersonalData:

    #Constructor
    def __init__(self, name, surname, age, height, nationality):
        self._name = name
        self._surname = surname
        self._age = age
        self._height = height
        self._nationality = nationality
    
    #Decorador y primer setter para la propiedad name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    #Decorador y primer setter para la propiedad surname
    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self,surname):
        self._surname = surname
    
    #Decorador y primer setter para la propiedad age
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,age):
        self._age = age
    
    #Decorador y primer setter para la propiedad height
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,height):
        self._height = height

    #Decorador y primer setter para la propiedad nationality
    @property
    def nationality(self):
        return self._nationality  

    @nationality.setter
    def nationality(self,nationality):
        self._nationality = nationality

def persona1():
     # Leer los datos del archivo de texto
    with open("datos_personas.txt", "r") as file:
        lines = file.readlines()
        # Suponemos que el archivo tiene el siguiente formato: nombre,apellido,edad,altura,nacionalidad
        data = lines[0].strip().split(",")  # Suponemos que solo hay una línea en el archivo

    # Crear una instancia de PersonalData con los datos del archivo
    persona1 = PersonalData(data[0], data[1], int(data[2]), int(data[3]), data[4])

    #print(f'Function "{func.__name__}" took {elapsed_time:.6f} seconds')

    # Imprimir los datos de la persona
    print(f'Nombre: {persona1.name}, Apellido: {persona1.surname}, Edad: {persona1.age}, Altura: {persona1.height}cm, Nacionalidad: {persona1.nationality}')

def personas():
       # Leer los datos del archivo de texto
    with open("datos_personas.txt", "r") as file:
        lines = file.readlines() #readlines devuelve una lista con todas las lineas

    personas = []  # Lista para almacenar las instancias de PersonalData (diferente a solo texto)

    # Procesar cada línea del archivo
    for line in lines:
        #print(line)
        data = line.strip().split(",")  # Suponemos que cada línea está en formato CSV
        # Crear una instancia de PersonalData con los datos de la línea y agregarla a la lista personas
        persona = PersonalData(data[0], data[1], int(data[2]), int(data[3]), data[4])
        personas.append(persona)


    # Imprimir los datos de cada persona
    for persona in personas:
        print("Nombre:", persona.name)
        print("Apellido:", persona.surname)
        print("Edad:", persona.age)
        print("Altura:", persona.height, "cm")
        print("Nacionalidad:", persona.nationality)
        print("\n")

    print(lines) #Lista con cada linea e formato de texto separado por comas
    print(personas) #Lista con las instancias de la clase PersonalData


if __name__ == '__main__':
   persona1()
   personas()
    