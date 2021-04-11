
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

def main():
    
    # ------- with list comprehension -------
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    
    # RETO
    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    
    old_confirmation = lambda worker_age: worker_age > 70
    old_people = [{**worker, **{'old': old_confirmation(worker['age'])}} for worker in DATA]

    print('with list comprehension')
    for worker in all_platzi_workers:
        print(worker)
    print('*'*30)
    
    # ------- with high order functions -------
    
    adults = list(filter(lambda worker: worker['age'] > 18, DATA)) # me entrega un dict
    adults = list(map(lambda worker: worker['name'], adults)) # me entrega un valor
    
    # combinacion del diccionario DATA con otra key y su valor.
    # https://stackoverflow.com/questions/38987/how-do-i-merge-two-dictionaries-in-a-single-expression-taking-union-of-dictiona
    #  Python mayores a 3.5 pero menores a 3.9
    old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))
    
    # Python mayores a 3.9
    # old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    
    # RETO
    all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))
    
    all_platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers = list(map(lambda worker: worker['name'], all_platzi_workers))
    
    print('with high order functions')
    for worker in all_platzi_workers:
        print(worker)
    print('*'*30)

if __name__ == '__main__':
    main()