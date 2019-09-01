Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> 
>>> input('korean age?: ')
korean age?: 23
'23'
>>> x = input('korean age?; ')
korean age?; 23
>>> print(x)
23
>>> type(x)
<class 'str'>
>>> int(x)
23
>>> type(x)
<class 'str'>
>>> float(x)
23.0
>>> type(x)
<class 'str'>
>>> type(x)
<class 'str'>
>>> y = x + 1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    y = x + 1
TypeError: can only concatenate str (not "int") to str
>>> x=x+1
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    x=x+1
TypeError: can only concatenate str (not "int") to str
>>> flaot(x)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    flaot(x)
NameError: name 'flaot' is not defined
>>> float(x)
23.0
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> type('x')
<class 'str'>
>>> x=input('what is your korean age?')
what is your korean age?23
>>> print(x)
23
>>> type(x)
<class 'str'>
>>> float(x)
23.0
>>> print('your USA age is', x)
your USA age is 23
>>> 
