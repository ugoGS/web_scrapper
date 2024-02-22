class PersonalData:

    def __init__(self, name, surname, age, height, nationality):
        self._name = name
        self._surname = surname
        self._age = age
        self._height = height
        self._nationality = nationality
    
    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def age(self):
        return self._age

    @property
    def height(self):
        return self._height

    @property
    def nationality(self):
        return self._nationality  

def persona1():
    try:
        with open("datos_personas.txt", "r") as file:
            data = file.readline().strip().split(",")  
            persona1 = PersonalData(data[0], data[1], int(data[2]), int(data[3]), data[4])
            print(f'Nombre: {persona1.name}, Apellido: {persona1.surname}, Edad: {persona1.age}, Altura: {persona1.height}cm, Nacionalidad: {persona1.nationality}')
    except FileNotFoundError:
        print("El archivo no fue encontrado.")

def personas():
    try:
        with open("datos_personas.txt", "r") as file:
            for line in file:
                try:
                    data = line.strip().split(",")  
                    if len(data) == 5:  # Verificar si hay exactamente 5 elementos en la línea
                        persona = PersonalData(data[0], data[1], int(data[2]), int(data[3]), data[4])
                        print("Nombre:", persona.name)
                        print("Apellido:", persona.surname)
                        print("Edad:", persona.age)
                        print("Altura:", persona.height, "cm")
                        print("Nacionalidad:", persona.nationality)
                        print("\n")
                    else:
                        print(f"Error: La línea '{line.strip()}' no tiene el formato correcto.")
                except ValueError:
                    print(f"Error: La línea '{line.strip()}' no tiene el formato correcto.")
    except FileNotFoundError:
        print("El archivo no fue encontrado.")

if __name__ == '__main__':
   persona1()
   personas()