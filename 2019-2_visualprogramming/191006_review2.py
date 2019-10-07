Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(2**10)
1024
>>> int(2.9)
2
>>> print(3.9)
3.9
>>> print(int(3.9))
3
>>> int(3.141592 * 100)
314
>>> print(int(3.141592 * 100)/100)
3.14
>>> round(1.5)
2
>>> round(2.3)
2
>>> round(3.8)
4
>>> round(4.5)
4
>>> round(4.5)
4
>>> round(4.6)
5
>>> round(3.5)
4
>>> import math
>>> math.ceil(1.2)
2
>>> math.ceil(3.9)
4
>>> math.ceil(9.5)
10
>>> math.floor(9.5)
9
>>> math.floor(38.7)
38
>>> math.floor(49.5)
49
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
>>> print(12345678901234567890 * 98765432109876543210)
1219326311370217952237463801111263526900
>>> print(0xAA + 55)
225
>>> print(1/3 + 1/3 + 1/3)
1.0
>>> print( 0.1 * 3)
0.30000000000000004
>>> print(0.1+0.1+0.1)
0.30000000000000004
>>> print(int(1.2 * 3.4 * 5.6 * 7.8))
178
>>> a = 1.2 * 3.4 * 5.6 * 7.8
>>> print(a - int(a))
0.2143999999999835
>>> print(1.234e-10)
1.234e-10
>>> pritn(1.234e-10 * 9876)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    pritn(1.234e-10 * 9876)
NameError: name 'pritn' is not defined
>>> print(1.234e-10 * 9876)
1.2186984e-06
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
3.141592653589793
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
3.141592653589793
3.141592653589793
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
3.141592653589793
3.141592653589793
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
5/6
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
5/6
4/3
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
0.30000000000000004
Traceback (most recent call last):
  File "/Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py", line 4, in <module>
    Fraction((0,1) * 3)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/fractions.py", line 161, in __new__
    raise TypeError("argument should be a string "
TypeError: argument should be a string or a Rational instance
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
0.30000000000000004
Traceback (most recent call last):
  File "/Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py", line 4, in <module>
    print(Fraction((0,1) * 3))
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/fractions.py", line 161, in __new__
    raise TypeError("argument should be a string "
TypeError: argument should be a string or a Rational instance
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
0.30000000000000004
0
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
0.30000000000000004
1/10
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
0.30000000000000004
3/10
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
0.30000000000000004
3/10
3.141592653589793
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
0.30000000000000004
3/10
84.94866535306801
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
0.30000000000000004
3/10
84.94866535306801
84.94866535306801
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 2**3
8
>>> 3**2
9
>>> 7 % 3
1
>>> 2 // 3
0
>>> 50//9
5
>>> 50%9
5
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
2
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
4096
2417851639229258349412352
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
4096
2417851639229258349412352
8
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
4096
2417851639229258349412352
8
4096
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
4096
2417851639229258349412352
8
4096
2417851639229258349412352
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
2
13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084125
Traceback (most recent call last):
  File "/Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py", line 6, in <module>
    print(fractions.Fracion(3**4, 5**-2))
AttributeError: module 'fractions' has no attribute 'Fracion'
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
2
13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084125
Traceback (most recent call last):
  File "/Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py", line 6, in <module>
    print(fractions.Fraction(3**4, 5**-2))
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/fractions.py", line 174, in __new__
    raise TypeError("both arguments should be "
TypeError: both arguments should be Rational instances
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py TypeError: both arguments should be Rational instances
4
3.141592653589793
3
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
4
3.141592653589793
3141.592653589793
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
4
3.141592653589793
3141.592653589793
3141
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
4
3.141592653589793
3141.592653589793
3141
3.141
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
4
Traceback (most recent call last):
  File "/Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py", line 5, in <module>
    from math import pi, round
ImportError: cannot import name 'round' from 'math' (/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload/math.cpython-37m-darwin.so)
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
4
3.141592653589793
3141.592653589793
3141
3.141
3
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
4
3.141592653589793
3141.592653589793
3141
3.141
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
Traceback (most recent call last):
  File "/Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py", line 4, in <module>
    print(sign(30 * pi / 180))
NameError: name 'sign' is not defined
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
0.49999999999999994
>>> 
 RESTART: /Users/harampark/Documents/myfirstpython/2019-2_visualprogramming/191006_review.py 
0.49999999999999994
0.7071067811865475
0.8660254037844386
1.0
>>> 
