def read():
    numbers = []
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ['Pedro', 'Juan', 'Carlos', 'Maria', 'Ana', 'Sofia', 'Rocío']
    print('Se ejecuta la función write')
    with open('./archivos/names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(name + '\n')
    print('Se terminó la función write')
    
def append():
    names = ['Pepe', 'Charlie']
    print('Se ejecuta la función write en modo append')
    with open('./archivos/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name + '\n')
    print('Se terminó la función write en modo append')


def run():
    append()


if __name__ == '__main__':
    run()