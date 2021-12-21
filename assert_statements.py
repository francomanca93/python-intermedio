def divisor(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input("Enter a number: ")
    assert num.isnumeric() and int(num) > 0, 'The value must be a positive number'
    print(divisor(int(num)))
    print('Finished')


if __name__ == '__main__':
    run()