from typing import List, Tuple
from sklearn.datasets import load_wine
from sklearn.utils import Bunch
import pandas as pd

def get_data_target_and_features() -> Bunch:
    bunch = load_wine(return_X_y=False, as_frame=True)
    return bunch