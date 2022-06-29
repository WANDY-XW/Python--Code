# Filltrando Datos 

# DATA is a constante variable, with funcion is saved a Diccionary



DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'OEA',
        'position': 'Technical Coach',
        'language': 'Python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',   },
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
        'organization': 'ONU',
        'position': 'Associate',
        'language': 'JavaScript',
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
        'language': 'GO',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': 'C',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'GO',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'JavaScript',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'Python',
    },
]

def FilterData():
    AllDevs = [Devs['name'] for Devs in DATA if Devs['language'] == 'Python' ]
    OnlyDevs = list(filter(lambda Devs: Devs['age']  >=  17, DATA))
    Aduls = list(map(lambda Devs: Devs['age'] > 32, DATA ))
    Aduls = list(map(lambda Devs: Devs | {  'Old': Devs['age']   >  32  }, DATA ))

    for Devs in Aduls:
        print(Devs)
if __name__ == "__main__":
    FilterData()