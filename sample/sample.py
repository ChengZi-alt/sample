__author__ = 'wei'

import random

# items=('a', 'b', 'c', 'd', 'e', 'f')
# sample=[['b', 'a', 'f', 'c'], ['e', 'b', 'a'], ['e', 'c', 'd', 'a', 'f', 'b'], ['d', 'c'], ['e', 'd', 'b', 'c'], ['e', 'b', 'a', 'c'], ['e', 'd', 'b', 'c'], ['a', 'd', 'b'], ['f', 'e', 'b', 'c', 'd', 'a'], ['d', 'a', 'b', 'f', 'c'], ['d', 'e'], ['c', 'b', 'f', 'd'], ['a', 'e'], ['a', 'f', 'e'], ['a', 'c', 'e', 'd', 'b'], ['e', 'c'], ['e', 'f', 'c'], ['f', 'b'], ['e', 'd', 'a', 'b', 'f', 'c'], ['f', 'c', 'd', 'e', 'a', 'b'], ['b', 'c'], ['b', 'f', 'a', 'd', 'c', 'e'], ['a', 'c'], ['a', 'f', 'e', 'c'], ['b', 'f', 'e'], ['a', 'e'], ['b', 'c'], ['a', 'b'], ['c', 'e'], ['e', 'c', 'b', 'a', 'f'], ['b', 'f', 'a', 'c', 'd'], ['f', 'b', 'e', 'c', 'a'], ['d', 'c', 'b'], ['c', 'd'], ['b', 'c'], ['e', 'a', 'b', 'f', 'c'], ['f', 'b', 'c'], ['b', 'e'], ['d', 'b'], ['d', 'e', 'f'], ['d', 'a', 'c'], ['f', 'b', 'c', 'd', 'a'], ['a', 'b'], ['b', 'c'], ['f', 'd', 'b', 'c'], ['a', 'b'], ['e', 'c', 'b', 'f'], ['c', 'd'], ['b', 'e'], ['c', 'a', 'b', 'd', 'e', 'f'], ['d', 'c', 'f', 'a', 'e', 'b'], ['f', 'c'], ['e', 'f', 'b'], ['b', 'c', 'f', 'e'], ['f', 'b'], ['b', 'e'], ['b', 'f', 'c', 'a', 'd'], ['b', 'c'], ['b', 'a'], ['a', 'd', 'c']]

items=('chips','eggs','bread','milk','beer','popcorn','butter')
sample=[
    ['milk','eggs','bread','chips'],
    ['eggs','popcorn','chips','beer'],
    ['eggs','bread','chips'],
    ['milk','eggs','bread','popcorn','chips','beer'],
    ['milk','bread','beer'],
    ['eggs','bread','beer'],
    ['milk','bread','chips'],
    ['milk','eggs','bread','butter','chips'],
    ['milk','eggs','butter','chips']
]



#产生随机样本
def createsample(factnum=20,itemrange=6):
    if itemrange>26 or itemrange<2:
        itemrange=6 #a-f
    items=tuple([chr(i) for i in range(97,97+itemrange)])
    print(items)
    facts=[]
    strongitems=random.sample(items,int(len(items)*.5))
    print('高频特征:'+strongitems)
    for i in range(0,factnum):
        facts.append(createfact(items,strongitems))
    print(facts)
    return items,facts

def createfact(items,strongitems):
    r=random.random()
    if r>0.5:
        l=2
    elif r>0.35:
        l=3
    elif r>0.2:
        l=4
    elif r>0.1:
        l=5
    else:
        l=6
    fact=random.sample(items,l)
    r2=random.random()
    if len(strongitems)>0:
        if r2>0.6:
            if strongitems[0] not in fact:
                fact.pop(0)
                fact.append(strongitems[0])
        elif r2>0.45:
            if strongitems[0] not in fact and len(fact)<len(items):
                fact.append(strongitems[0])
        else:
            sitem=strongitems[random.randint(1,len(strongitems)-1)]
            if sitem not in fact:
                if r2>0.15:
                    fact.pop(0)
                    fact.append(sitem)
                else:
                    if len(fact)<len(items):
                        fact.append(sitem)
    return fact