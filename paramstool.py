#!/usr/bin/python3

import itertools

def full_arrangement(**kwargs):
    print(kwargs)
    print(kwargs.values())
    for x in itertools.product(kwargs):
        print(x)

def _test_full_arrangement():
    full_arrangement(name=["zhangsan"],age=[12,23],status=[1,2,3,5])
    full_arrangement(name=("zhangsan"),age=(12,23),status=(1,2,3,5))
    
def product(*args, **kwds):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)    
    
if __name__ == '__main__':
    _test_full_arrangement()
