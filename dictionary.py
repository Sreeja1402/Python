Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a={'name':'sai','age':22}
a
{'name': 'sai', 'age': 22}
print(a{'name'})
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(a['name'])
sai


a=dict({1:'a',2:'b',3:'c'})
a
{1: 'a', 2: 'b', 3: 'c'}
type(a)
<class 'dict'>


employee={'name':'sai','age':22,'salary':25000,'company':'wipro'}
employee
{'name': 'sai', 'age': 22, 'salary': 25000, 'company': 'wipro'}
print('age:%d' %employee['age'])
age:22
print('company:%s' %employee['company'])
company:wipro


a.pop(1)
'a'
a
{2: 'b', 3: 'c'}
>>> employee.pop(1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    employee.pop(1)
KeyError: 1
>>> 
>>> a=dict({1:'a',2:'b',3:'c'})
>>> dict_values({1,2,3})
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dict_values({1,2,3})
NameError: name 'dict_values' is not defined
>>> dict_values({'a','b','c'})
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    dict_values({'a','b','c'})
NameError: name 'dict_values' is not defined
>>> a.values()
dict_values(['a', 'b', 'c'])
>>> a.keys()
dict_keys([1, 2, 3])
>>> a.get(1)
'a'
>>> a.get(2)
'b'
>>> a.get(3)
'c'
>>> 
>>> b=dict({1:'a',2:'b',3:'c'})
>>> b.update({2:'abc'})
>>> b
{1: 'a', 2: 'abc', 3: 'c'}
>>> len(b)
3
>>> sorted(b)
[1, 2, 3]
>>> 
>>> b=dict({1:'a',2:'b',4:'d',5:'e',3:'c'})
>>> dict(dorted(b.items()))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    dict(dorted(b.items()))
NameError: name 'dorted' is not defined. Did you mean: 'sorted'?
>>> dict(sorted(b.items()))
{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
