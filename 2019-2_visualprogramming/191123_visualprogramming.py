import os
'''
os.path.exists(
    "/Users/harampark/Library/Mobile\ Documents/com\~apple\~CloudDocs/Documents/myfirstpython/2019-2_visualprogramming")
'''

files = os.listdir(
    "/Users/harampark/Library/Mobile\ Documents/com\~apple\~CloudDocs/Documents/myfirstpython/2019-2_visualprogramming")
for f in files:
    print(f)
