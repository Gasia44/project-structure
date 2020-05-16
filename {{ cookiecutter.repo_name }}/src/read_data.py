import glob
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import timedelta

import pandas as pd


class ReadData:
    def __init__(self):
        pass

    def _read_csv_file(self, file):
        return pd.read_csv(file, low_memory=False)

    def read_in_parallel(self, file_path):
        print('reading...')
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=60) as executor:
            all_files = [file for file in glob.glob(file_path, recursive=True)]
            result = executor.map(self._read_csv_file, all_files)

        df_temp = pd.concat(result)
        df_temp['created_at'] = pd.to_datetime(df_temp['created_at'])
        time_elapsed = time.time() - start_time
        print('done with time:', str(timedelta(seconds=time_elapsed)))
        return df_temp
