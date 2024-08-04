#N number of arguments
#The arguments are accesse by using **parameters[['key']

def car_name(**cars):
    print(f'The name of car is {cars["c3"]}')

car_name(c2='Betly',c3='Porsche',c1='Jaguar')

#skip position
