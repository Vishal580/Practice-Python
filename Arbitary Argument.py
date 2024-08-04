#There can be n numbers of arguments.
#They are accessed using the index.
#The parameters is passed by an asterisk(*).

def car_name(*c):
    print(f'The name of car is {c[3]}')

car_name('Betly','Porsche','Jaguar','Ferrari')
