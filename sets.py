Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#set
a={1,2,3,2,3,4,5,6}
a
{1, 2, 3, 4, 5, 6}
a
{1, 2, 3, 4, 5, 6}

b={[1,2,'sai'],'sreeja',4.6,8}
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b={[1,2,'sai'],'sreeja',4.6,8}
TypeError: unhashable type: 'list'
a={1,2,3.7,2+6j,'sai'}
a
{1, 2, 3.7, 'sai', (2+6j)}
type(a)
<class 'set'>
b=set[1,23,4]
b
set[1, 23, 4]
b=set([1,2,3])
b
{1, 2, 3}
s=['w','e','r','t']
set(s)
{'w', 'e', 't', 'r'}
s.add('s')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.add('s')
AttributeError: 'list' object has no attribute 'add'

s={'monday','tuesday','wednesday'}
s.discard('tuesday')
s
{'wednesday', 'monday'}
s={'monday','tuesday','wednesday'}
>>> s.remove('tuesday')
>>> 
>>> s
{'wednesday', 'monday'}
>>> s={'monday','tuesday','wednesday'}
>>> s.discard('tusday')
>>> a
{1, 2, 3.7, 'sai', (2+6j)}
>>> s
{'wednesday', 'monday', 'tuesday'}
>>> 
>>> 
>>> #pop
>>> a={'a','b','c','d'}
>>> a.pop()
'a'
>>> a
{'c', 'b', 'd'}
>>> 
>>> 
>>> # union
>>> a={1,2,3,6}
>>> b={7,5,9,8}
>>> a.union(b)
{1, 2, 3, 5, 6, 7, 8, 9}
>>> 
>>> a={1,2,4,5,8,3,6}
>>> b={7,5,9,8}
>>> q.imtersection(b)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    q.imtersection(b)
NameError: name 'q' is not defined
>>> a.intersection(b)
{8, 5}
>>> 
>>> 
>>> a={'name':'sai','age':22}
>>> a
{'name': 'sai', 'age': 22}
>>> type(a)
<class 'dict'>
>>> print(a['name'])
sai
>>> a=dict([1:'a',2:'b',3:'c'])
SyntaxError: invalid syntax
