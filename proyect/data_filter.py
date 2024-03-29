
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # Comprehensions solutions
    # Impriir lista para ver resultados de cada una

    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    adults =  [worker["name"] for worker in DATA if worker["age"] > 18]

    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    adults_n = list(map(lambda worker: worker | {"string":  str(worker["age"] + 2) + "K"}, old_people))

    for worker in all_python_devs:
        print(worker)

    print('---------------------------')
    
    for worker in adults_n:
        print(worker)
    
    #print(adults_n)

    #Probando cadenas
    string_v = 'KLMiwu98oS'
    print(string_v[0:5:-2])    
  

if __name__ == '__main__':
    run() 

