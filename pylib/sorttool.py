#!/usr/bin/python3

import pprint

def magic_sort(data=[{}], order="id desc"):
    '''
    @param    data    list        item is a dict  
    @param    order   string      order like sql "id desc, status asc"
    '''
    orderArr = []
    for item in order.lower().split(","):
         orderArr.append(item.strip().split())
    orderArr.reverse()     # 先排最后的字段，第一个字段，最后排序
    size = len(data)
    for o in orderArr:
        key = int(o[0]) if o[0].isdigit() else o[0] # 如果key是数字字符，返回整数
        ad  = "asc" if len(o) < 2 else o[1] # asc or desc，默认 asc
        for i in range(size):
            for j in range(size-i-1):
                if (ad == 'desc' and data[j][key] < data[j+1][key]) or (ad == 'asc' and data[j][key] > data[j+1][key]):
                    data[j],data[j+1] = data[j+1],data[j]
    return data

def _test_sort(params):
    for param in params:
        res = magic_sort(param['data'],param['order'])
        myprint(res)
    
def myprint(param):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(param)
    
if __name__ == '__main__':
    data = [
            {"id":1,"status":3,"age":12},
            {"id":2,"status":1,"age":13},
            {"id":2,"status":2,"age":14},
            {"id":2,"status":3,"age":14},
            {"id":4,"status":2,"age":15},
    ]
    order = "id desc, age  , status desc"
    params = [{"data":data,"order":order}]
    ll = [
            [1,3,2,5],
            [3,2,3,5],
            [3,1,4,3],
            [2,3,4,2],
            [3,0,4,1],
            [5,3,1,5],
            ]
    llorder = "0 desc,1 asc,2 desc,3 desc"
    params.append({"data":ll,"order":llorder})
    _test_sort(params)
    
