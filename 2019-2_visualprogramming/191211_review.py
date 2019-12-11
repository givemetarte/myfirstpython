import pandas as pd
import numpy as np
import json

with open('bithub.json') as json_file:
    result = json.loads(json_file)
print(result)
