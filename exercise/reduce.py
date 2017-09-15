def mul(x,y):
    return x * y

def prod(l):
    return str(reduce(mul,l))

print('3 * 5 * 7 * 9 = ' + prod([3,5,7,9]))
