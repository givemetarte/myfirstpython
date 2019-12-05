import pandas as pd
import numpy as np

data = {'state': ['Ohio', 'Nevada'],
        'year': [2000, 2001],
        'pop': [1.5, 1.7]}
df = pd.DataFrame(data)

df.debt = np.arange(5.)

print(df)
