Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> x = 3
>>> type(x)
<class 'int'>
>>> x = '123'
>>> type(x)
<class 'str'>
>>> float(x)
123.0
>>> type(x)
<class 'str'>
>>> 
>>> 
>>> 
>>> 
>>> input<your korean age?: >
SyntaxError: invalid syntax
>>> input<'your Korean age?; >
SyntaxError: EOL while scanning string literal
>>> input<'your Korean age?: '>
SyntaxError: invalid syntax
>>> input <your age?>
SyntaxError: invalid syntax
>>> input<'your age?'>
SyntaxError: invalid syntax
>>> input('your Korean age?: ')
your Korean age?: 23
'23'
>>> x = input('your Korean age?: ')
your Korean age?: 23
>>> print(x, 'years')
23 years
>>> x = x + 1
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x = x + 1
TypeError: can only concatenate str (not "int") to str
>>> 
