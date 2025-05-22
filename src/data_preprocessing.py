import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def clean():
    encoder = OneHotEncoder(sparse_output=False)
    RESULT = encoder.fit_transform(input)
    return RESULT



