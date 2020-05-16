from abc import ABC, abstractmethod
from functools import reduce

import pandas as pd


class PreProcess(ABC):
    def __init__(self):
        self._df = None
        pass

    @abstractmethod
    def process(self):
        pass

    @staticmethod
    def merge_data(dfs):
        df_result = reduce(lambda left, right: pd.merge(left, right, on='user_id', how="outer"), dfs)
        df_result = df_result.fillna(0).drop_duplicates("user_id").reset_index(drop=True)
        return df_result
