Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> nxt = input('what is your name?: ')
what is your name?: Haram
>>> print("Hello", nxt)
Hello Haram
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> hrs = input("hours that you have worked on")
hours that you have worked on 24
>>> float(hrs)
24.0
>>> class(hrs)
SyntaxError: invalid syntax
>>> type(hrs)
<class 'str'>
>>> float('hrs')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float('hrs')
ValueError: could not convert string to float: 'hrs'
>>> float(hrs)
24.0
>>> rate = input("rate per hour")
rate per hour 8350
>>> float(rate)
8350.0
>>> total = hrs * rate
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    total = hrs * rate
TypeError: can't multiply sequence by non-int of type 'str'
>>>  x = float(hrs)
 
SyntaxError: unexpected indent
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> hrs = input('working hours?: ')
working hours?: 25
>>> x = float(hrs)
>>> type(x)
<class 'float'>
>>> 
>>> rate = input('rate per hours?: ')
rate per hours?: 8350
>>> y = float(rate)
>>> type(y)
<class 'float'>
>>> total = x * y
>>> print(total)
208750.0
>>> print('your total fees are', total)
your total fees are 208750.0
>>> 
