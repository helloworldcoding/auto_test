#!/usr/bin/python3

import itertools

def full_arrangement(**kwargs):
    print(kwargs)
    print(kwargs.values())
    result = [[]]
    for val in kwargs.values():
        result = [x+[y] for x in result for y in val]
    print(result)
    #mapRes = [[]]
    mapRes = [{}]
    for k,v in kwargs.items():
       # mapRes = [_x+[{k:_y}] for _x in mapRes for _y in v]
        mapRes = [_x  if _x and (_x.update({k:_y}) is None)  else {k:_y}  for _x in mapRes for _y in v]
    print(mapRes,len(mapRes))
    #for x in itertools.product(kwargs):
    #    print(x)

def _test_full_arrangement():
    full_arrangement(name=["zhangsan"],age=[12,23,2],status=[1,2,3,5])
    
   
if __name__ == '__main__':
    _test_full_arrangement()

