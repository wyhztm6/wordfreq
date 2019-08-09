#s = input()

def freq(fruit): # 函数头
    result = []
    
    fruit = fruit.lower()
    flst = fruit.split()
    unique_fruit = list(set(flst))
    for f in unique_fruit:
        n = flst.count(f)
        result.append( (f,n) ) # 把(f,n)这个元组添加到result列表后面
        
    return result


def sort_in_descending_order(lst):
    import operator
    lst2 = sorted(lst, reverse=True, key=operator.itemgetter(1))
    return lst2


def youdao_link(s):
    link = 'http://youdao.com/w/eng/' + s + '/#keyfrom=dict2.index'
    return link


def file2str(fname):
    f = open(fname)
    s = f.read()
    f.close()
    print(s)
    return s

s = file2str('a.txt')     
L = freq(s)
L2 = sort_in_descending_order( L )
for x in L2:
    print('%s\t%d\t%s' % (x[0], x[1], youdao_link(x[0])))

