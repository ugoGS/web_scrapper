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

 
if __name__ == '__main__':
    persona1 = PersonalData("Juanito","Alimaña",29,170,"Colombian")

    persona1.name = input("Ingrese su nombre: ")
    persona1.surname = input("Ingrese su apellido: ")
    persona1.age = int(input("Ingrese la edad: "))
    persona1.height = int(input("Ingrese su estatura: "))
    persona1.nationality = input("Ingrese su nacionalidad: ")

    print("Nombre: "+persona1.name)
    print("Apellido:"+persona1.surname)
    print("Edad "+str(persona1.age))
    print("Altura: "+str((persona1.height)/100)+" mts")
    print("Nacionalidad: "+persona1.nationality)