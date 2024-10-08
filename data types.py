Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
print(a,type(a))
10 <class 'int'>

# float
a=3.45
a
3.45

# complex
a=1+2j
a
(1+2j)
type(a)
<class 'complex'>

# strin
# string
a='hello'
a
'hello'

b="hello"
b
'hello'
a='''sreeja'''
a
'sreeja'
print(type(a))
<class 'str'>

# string methods

a="hello world"
print(len(a))
11
>>> print(a.lower())
hello world
>>> print(a.upper)
<built-in method upper of str object at 0x000001F8E29352F0>
>>> print(a.upper())
HELLO WORLD
>>> a=" hello world"
>>> print(a.strip())
hello world
>>> print(a.replace("world","python"))
 hello python
>>> a='apple,banana,mango'
>>> print(a.split())
['apple,banana,mango']
>>> print(a.split(','))
['apple', 'banana', 'mango']
>>> a="hello hello world"
>>> a.count("hello")
2
>>> print(a.find('w'))
12
>>> 
>>> 
>>> 
>>> 
>>> 
>>> # list
>>> a=[10,1.9,'sai',2+3j]
>>> a
[10, 1.9, 'sai', (2+3j)]
>>> print(a[2])
sai
>>> a[1]=2.5
>>> a
[10, 2.5, 'sai', (2+3j)]
>>> 
>>> a=[2,3,4,5,6,7,8]
>>> b=[1,23,56,7,889,4]
>>> print(a+b)
[2, 3, 4, 5, 6, 7, 8, 1, 23, 56, 7, 889, 4]
>>> b.sort()
>>> b
[1, 4, 7, 23, 56, 889]
>>> a=[[1,2,3],12.4,334,'sai']
>>> print(a[3])
sai
