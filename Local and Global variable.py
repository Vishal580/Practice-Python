x=200    #BTMC Global->Accessable everywhere
def f1():
    #x=10  #Local variable->Accessable inside the function
    print(x)

def f2():
    #x=20   #Local variable
    print(x)
    f1()
f2()
