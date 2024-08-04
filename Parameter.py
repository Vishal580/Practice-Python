"""If you pass argunment,the default parameter is skipped,else print the default value"""
def fav_sub(fav='Maths'):
    print(f'Our favourate subject is:{fav}')

fav_sub("DBMS")
fav_sub('CN')
fav_sub("ADE")
fav_sub()
