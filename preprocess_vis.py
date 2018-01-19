import io
import pandas as pd
import pandas_profiling as pdp
from IPython.display import display
import numpy as np


def info(df):
    buf = io.StringIO()
    df.info(buf=buf)
    df_info_str = buf.getvalue()
    dict_df = {"Feature": [], "Non NA": [], "Type": []}
    for line in df_info_str.split("\n")[3:-3]:
        dict_df["Feature"].append(line.split("    ")[0])
        dict_df["Non NA"].append(line.split("    ")[1].split(" ")[0])
        dict_df["Type"].append(line.split("    ")[1].split(" ")[2])
    display(pd.DataFrame(dict_df))


def desc(df):
    try:
        display(df.select_dtypes(include=['object']).describe())
        print("")
    except:
        print("There are no object columns")
        print("")
    try:
        display(df.select_dtypes(include=[np.float, np.int]).describe())
    except:
        print("There are no float or int columns")
    return None


def report(df):
    try:
        return pdp.ProfileReport(df)
    except:
        print("Error: can't show report")


def headd(df, num_rows=5, max_columns=3):
    if len(list(df)) / max_columns > 1:
        for i in range(len(list(df)) / max_columns):
            print i
            display(df.iloc[0:num_rows, i*max_columns:max_columns*(i+1)])
    else:
        display(df.head(num_rows))
