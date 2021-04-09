import math

def main():
    # my_dict = {}
    # 
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print('Reto 1')
    print(my_dict)
    print('*'*30)
    
    numbers_dict={i:math.sqrt(i) for i in range(1,1001)}
    print('Reto 2')
    first_ten = dict(list(numbers_dict.items())[:10])
    print(first_ten)
    print('*'*30)

if __name__ == '__main__':
    main()