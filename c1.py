# -*- encoding=UTF-8 -*-
import requests
import random
import re
from bs4 import BeautifulSoup


def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print div.text.strip()




def demo_string():
    stra = 'hello world'
    print stra.capitalize()
    print stra.replace('world', 'nowcoder')
    strb = '  \n\rhello nowcoder \r\n'
    print 1, strb.lstrip()
    print 2, strb.rstrip()
    strc = 'hello w'
    print 3, strc.startswith('hel')
    print 4, strc.endswith('x')
    print 5, stra + strb + strc
    print 6, len(strc)
    print 7, '-'.join(['a', 'b', 'c'])
    print 8, strc.split(' ')
    print 9, strc.find('ello') # ello开头则为1

def demo_operation():
    print 1, 1 + 2, 5 / 2, 5 * 2, 5 - 2
    print 2, True, not True
    print 3, 1 < 2, 5 > 2
    print 4, 2 << 3
    print 5, 5 | 3, 5 & 3, 5 ^ 3
    x = 2
    y = 3.3
    print x, y, type(x), type(y)
def demo_buildinfunction():
    print 1,max(2,1),min(5,3)
    print 2,len('xxx'),len([1,2,3])
    print 3,abs(-2) # 绝对值
    print 4,range(1,10,3) # for中的step
    print 5,dir(list) # 其实打印出来之后就是一个list集合 win下的dir就是一个目录的list集合
    x=2
    print 6,eval('x+3')
    print 7,chr(97),ord('a')
    print 8,divmod(11,3) # 得3 余2
def demo_controlflow():
    score =65
    if score > 90:
        print 1,'A'
    elif score > 80:
        print 2,'B'
    else:
        print 3,'C'

    while score < 100:
        print score
        score+=10
    score=65
    # for (int i = 0; i < 10; ++i)
    # continue ,break, pass
    for i in range(0, 10, 2):
        if i == 0:
            pass  # do_special
            # print 3, i
        if i < 5:
            continue
        print 3, i
        if i == 6:
            break

# 数据结构 list dictionary set temp
def demo_list():
    lista = [1, 2, 3]  # vector<int> Arraylist
    print 1, lista
    listb = ['a', 1, 'c', 1.1]
    print 2, listb
    lista.extend(listb)
    print 3, lista
    print 4, len(lista)
    print 5, 'a' in listb
    lista = lista + listb
    print 6, lista
    listb.insert(0, 'www')
    print 7, listb
    listb.pop(1)
    print 8, listb
    listb.reverse()
    print 9, listb
    print 10, listb[0], listb[1]
    listb.sort()
    print 11, listb
    listb.sort(reverse=True)
    print 12, listb
    print 13, listb * 2
    print 14, [0] * 14  # memset(src, 0, len)
    tuplea = (1, 2, 3)
    listaa = [1, 2, 3]
    listaa.append(4)
    print 15, listaa
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def demo_dict():
    dicta ={4:16,1:1,2:4,3:9}
    print 1,dicta
    print 2,dicta.keys(),dicta.values()
    print dicta.has_key(1),dicta.has_key('3')
    for key,value in dicta.items():
        print 'key-value:',key,value
    dictb={'+':add,'-':sub}
    print 4,dictb['+'](1,2)
    print 5,dictb.get('-')(15,3)
    dictb['*']='x'
    print 6, dictb
    dicta.pop(4)
    print 7, dicta
    del dicta[1]
    print 8,dicta

def demo_set():
    lista = [1, 2, 3]
    seta = set(lista)
    setb = set((2, 3, 4))
    print 1, seta
    print 3, seta.intersection(setb), seta & setb
    print 4, seta | setb, seta.union(setb)
    print 5, seta - setb
    seta.add('x')
    print 6, seta
    print len(seta)
    print seta.isdisjoint(set((1, 2)))
# 面向对象
class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)


class Guest(User):
    def __repr__(self):
        return 'im guest:' + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid) + ' ' + self.group

def create_user(type):
    if type == 'USER':
        return User('u1', 1)
    elif type == 'ADMIN':
        return Admin('a1', 101, 'g1')
    else:
        return Guest('gu1', 201)
        # raise ValueError('error')

def demo_exception():
    try:
        print 2 / 1
        # print 2 / 0
        # if type == 'c':
        raise Exception('Raise Error', 'NowCoder')
    except Exception as e:
        print 'error:', e
    finally:
        print 'clean up'

def demo_random():
    # 1 - 100
    # random.seed(1)
    # x = prex * 100007 % xxxx
    # prex  = x 幂等性
    print 1, int(random.random() * 100)
    print 2, random.randint(0, 200)
    print 3, random.choice(range(0, 100, 10))
    print 4, random.sample(range(0, 100), 4)
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)
    print 5, a

def demo_re():
    str = 'abc123def12gh15'
    p1 = re.compile('[\d]+')
    p2 = re.compile('\d')
    print 1, p1.findall(str)
    print 2, p2.findall(str)
    # \t\n
    str = 'a@163.com;b@gmail.com;c@qq.com;e0@163.com;z@qq.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    print 3, p3.findall(str)

    str = '<html><h>title</h><body>xxx</body></html>'
    p4 = re.compile('<h>[^<]+</h>')
    print 4, p4.findall(str)
    p4 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print 5, p4.findall(str)

    str = 'xx2016-06-11yy'
    p5 = re.compile('\d{4}-\d{2}-\d{2}')
    print p5.findall(str)

if __name__=='__main__':
    # 代码块注释
    """
    user1 =User('u1',1)
    print user1
    admin1 =Admin("a1",101,'g1')
    print admin1
    print create_user('USER')

    print create_user('USERX')
    """

    # qiushibaike()
    # print "hello nowcoder"
    # demo_string()
    # demo_operation()
    # demo_buildinfunction()
    # demo_controlflow()
    # demo_list()
    # demo_dict()
    # demo_set()
    # demo_exception()
    # demo_random()
    demo_re()