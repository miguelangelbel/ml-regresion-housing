import pandas as pd
import numpy as np
import src.constants as ct


def read_raw_data():
    """Read the csv into a pandas dataframe

    Returns:
        dataframe: dataframe containing features of Madrid house pricing
    """
    path_read = ct.PATH_ROOT + ct.PATH_DATA_RAW

    df = pd.read_csv(path_read)

    return df
