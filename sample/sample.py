__author__ = 'wei'

import random
import connect_db as cdb

# items=('a', 'b', 'c', 'd', 'e', 'f')
# sample=[['b', 'a', 'f', 'c'], ['e', 'b', 'a'], ['e', 'c', 'd', 'a', 'f', 'b'], ['d', 'c'],
# 定义全部商品类和流水商品集合
#items=('chips','eggs','bread','milk','beer','popcorn','butter')
# sample=[
#     ['milk','eggs','bread','chips'],
#     ['eggs','popcorn','chips','beer'],
#     ['eggs','bread','chips'],
#     ['milk','eggs','bread','popcorn','chips','beer'],
#     ['milk','bread','beer'],
#     ['eggs','bread','beer'],
#     ['milk','bread','chips'],
#     ['milk','eggs','bread','butter','chips'],
#     ['milk','eggs','butter','chips']
# ]


items = []
sample = cdb.GetSample()
for i in sample:
    for j in i:
        items.append(j)
items = set(items)
items = tuple(items)
print(len(sample))


# 产生随机样本
def createsample(factnum=20, itemrange=6):
    if itemrange > 26 or itemrange < 2:
        itemrange = 6  # a-f
    items = tuple([chr(i) for i in range(97, 97 + itemrange)])  # 根据chr得到一个元组
    print(items)
    facts = []
    strongitems = random.sample(items, int(len(items) * .5))
    print('高频特征:' + i for i in strongitems)
    for i in range(0, factnum):
        facts.append(createfact(items, strongitems))
    print(facts)
    return items, facts


def createfact(items, strongitems):
    r = random.random()
    if r > 0.5:
        l = 2
    elif r > 0.35:
        l = 3
    elif r > 0.2:
        l = 4
    elif r > 0.1:
        l = 5
    else:
        l = 6
    fact = random.sample(items, l)
    r2 = random.random()
    if len(strongitems) > 0:
        if r2 > 0.6:
            if strongitems[0] not in fact:
                fact.pop(0)
                fact.append(strongitems[0])
        elif r2 > 0.45:
            if strongitems[0] not in fact and len(fact) < len(items):
                fact.append(strongitems[0])
        else:
            sitem = strongitems[random.randint(1, len(strongitems) - 1)]
            if sitem not in fact:
                if r2 > 0.15:
                    fact.pop(0)
                    fact.append(sitem)
                else:
                    if len(fact) < len(items):
                        fact.append(sitem)
    return fact


if __name__ == '__main__':
    createsample(factnum=20, itemrange=6)
