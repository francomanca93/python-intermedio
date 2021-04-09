def main():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    
    # list comprehension donde numeros al cuadrado no sean multiplo de 3.
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print('Reto 1')
    print(squares)
    print('*'*30)
    
    # list comprehension donde los numeros sean multiplos de 4, 6 y 9 en un rango de numeros con hasta 5 digitos
    squares_2 = [i for i in range(1, 9999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0][:10]
    print('Reto 2')
    print(squares_2)
    print('*'*30)

if __name__ == '__main__':
    main()