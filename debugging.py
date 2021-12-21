def divisor(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            raise ValueError("Valor negativo. Solo insertar positivos")
        if num == 0:
            raise ValueError("El valor ingresado es 0. Debe ser un valor mayor a 1")
        print(divisor(num))
        print('Finished')
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    run()