def main():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname': 'Franco', 'lastname': 'Manca'}

    super_list = [
        {'firstname': 'Franco', 'lastname': 'Manca'},
        {'firstname': 'Ivan', 'lastname': 'Manca'},
        {'firstname': 'Maxi', 'lastname': 'Almeira'},
        {'firstname': 'Federico', 'lastname': 'Rivera'},
        {'firstname': 'Veronica', 'lastname': 'Luna'},
    ]
    
    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_num': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.4]
    }
    
    for key, value in super_dict.items():
        print(key, ' ', value)
    
    print('*'*64)
    
    for dic in super_list:
        for key, value in dic.items():
            print(key, ' ', value)
        
        print('-'*10)
    
if __name__ == '__main__':
    main()