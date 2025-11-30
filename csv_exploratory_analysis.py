import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime
from functools import wraps
import time
import math
import os


def timeit(func):
    # This is from https://dev.to/kcdchennai/python-decorator-to-measure-execution-time-54hk for debugging.
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result

    return timeit_wrapper


df = pd.read_csv("enrollment_2022-11-05T20_09_38_WI23.csv")
df2 = pd.read_csv("enrollment_2022-11-06T04_14_05_WI23.csv")


def clean_data(dataframe_placeholder):
    subj_course_split = dataframe_placeholder['subj_course_id'].str.split(expand=True)

    clean = dataframe_placeholder.assign(ten_percent=(round(dataframe_placeholder['total'] * 0.1, 0)).astype(int),
                                         subj=subj_course_split[0],
                                         course_id=subj_course_split[1],
                                         time=pd.to_datetime(dataframe_placeholder['time'], unit='ms')
                                         )
    clean = clean[clean['subj'] == 'COGS']

    for i in clean.columns:
        if clean[i].hasnans:
            print(f'Column {i} has nan values.')

    # This removes course series endings such as the 'a' in Cogs 107a to check for certain classes that we want to remove.

    # Dropping specific classes such as cogs 190a or cogs 99

    clean = clean[
        (pd.to_numeric(clean['course_id'].str.rstrip('a-zA-Z'), errors='coerce') < 190) &
        (pd.to_numeric(clean['course_id'].str.rstrip('a-zA-Z'), errors='coerce') != 99)
        ].drop(['subj_course_id', 'subj'], axis=1)
    return clean


def combine_df_by_time(df_lists: list):
    clean_datasets = [clean_data(df) for df in df_lists]
    clean_datasets = pd.concat(clean_datasets, ignore_index=True).sort_values('time').reset_index()
    return clean_datasets


def clean_raw_folder(folder):
    term = []
    for files in os.listdir(folder):
        if files.endswith('.csv'):
            term.append(pd.read_csv(f'{folder}/' + str(files)))

    return term


