import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd

random1 = []
for i in range(100):
    number = random.randint(0, 100)
    random1.append(number)
random1.sort()

count1 = []
for i in random1:
    count1.append(random1.count(i))


random2 = np.random.normal(50, 18, size=100)
random2 = np.array(random2, dtype=np.int)
random2 = np.sort(random2)

count2 = np.bincount(random2, minlength=100)

df1 = pd.DataFrame(random2)
df2 = pd.DataFrame(count2)
print(df1, df2)

plt.plot(random1, count1, marker='o')
plt.plot(df1, df2, marker='o')
plt.show()
