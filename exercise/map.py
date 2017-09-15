from functools import reduce

def func1(s):
    l = ''
    for i,value in enumerate(s):
        if(i == 0):
            l = l + value.upper()
        else:
            l = l + value.lower()
    return l

print(map(func1,['Micheal','asdas','aASASDA']))

def mul(x,y):
    return x * y

def prod(l):
    return str(reduce(mul,l))

print('3 * 5 * 7 * 9 = ' + prod([3,5,7,9]))
