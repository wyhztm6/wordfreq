def freq(fruit):
    '''
    功能：把字符串转成列表。目的是得到每个单词的频率。
    输入：字符串
    输出：列表，列表里包含一组元组，每个元组包含单词与单词的频率。
    注意事项：首先要把字符串转成小写。原因是balala
    '''
    result = []
    
    fruit = fruit.lower()#字符串小写
    flst = fruit.split()#字符串转list
    unique_fruit = list(set(flst))#找到水果种类
    #遍历每种水果，统计出每种水果的出现次数
    #水果的种类用f表示，该种水果出现的次数用n表示
    for f in unique_fruit:
        n = flst.count(f)#数出每种水果出现的次数
        result.append( (f,n) ) 

    return result



def sort_in_descending_order(lst):
    import operator
    lst2 = sorted(lst, reverse=True, key=operator.itemgetter(1))
    return lst2#函数尾


def youdao_link(s):
    link = 'http://youdao.com/w/eng/' + s + '/#keyfrom=dict2.index'
    return link


def file2str(fname):#文件转字符
    f = open(fname)#打开
    s = f.read()#读取
    f.close()#关闭
    return s#函数尾


def remove_punctuation(s):#标点删除
    s = s.replace(',','').replace('.','').replace('?','')#replace函数
    s = s.strip() # remove whitespaces in the beginning or in the end
    return s#函数尾



## main（程序入口）


import sys

#print(sys.argv)

num = len(sys.argv)

#print(num)

if num == 1:
    s = input()

elif num == 2:
    fname = sys.argv[1]
    s = file2str(fname)

else:
    print('I can accept at most 2 arguments.')
    sys.exit()

#print(s)


print(s)
s = remove_punctuation(s)
L = freq(s)
L2 = sort_in_descending_order( L )
for x in L2:
    print('%s\t%d\t%s' % (x[0], x[1], youdao_link(x[0])))
















