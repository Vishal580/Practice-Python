position=-1
def linear_search(my_list,k):
    if i in range(len(my_list)):
        if my_list[i]==k:
            globals()['position']=i
            return True
        return False


a=[1,2,3,4,5,6]
key=5

if linear_search(a,key):
    print(f'{key} found at position {position+1} in list {a}')
else:
    print(f'{key} was not found in list{a}')
