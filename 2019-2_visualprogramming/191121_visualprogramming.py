import matplotlib.pyplot as plt
import numpy as np

plt.plot([1.5, 3.5, -2, 1.6, 1.5, 3.5, -2, 1.6])
plt.plot(np.random.randn(50).cumsum(), 'k--')
plt.show()
