Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=50
>>> a
50
>>> b=a
>>> b
50
>>> a=40
>>> b=90
>>> a,b=b,a
>>> a
90
>>> b
40
>>> print(type(a))
<class 'int'>
>>> print(id(a))
140713094763736
>>> name='sreeja'
>>> age=22
>>> marks=75
>>> print(name)
sreeja
>>> print(age)
22
>>> print(marks)
75
>>> print(name,',',age,',',marks)
sreeja , 22 , 75
>>> x=y=z=50
>>> x
50
>>> y
50
>>> z
50
>>> a,b,c=3,4,5
>>> a
3
>>> b
4
>>> c
5
