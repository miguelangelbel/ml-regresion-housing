import pandas as pd
import numpy as np


def prepare_data(df_raw):
    """Cleans the data. Eliminates the duplicates, outliers, nulls. Normalization and other features.

    Args:
        df_raw (dataframe): dataframe containing all features of house pricing of Madrid

    Returns:
        dataframe: dataframe cleaned 
    """ """"""
    ## 1) Duplicates
    df_not_duplicates = df_raw.drop_duplicates()

    # 2) Converting into numeric types the variables price and m2
    df_not_duplicates["price"] = pd.to_numeric(
        df_not_duplicates["price"], errors="coerce"
    )
    df_not_duplicates["m2"] = pd.to_numeric(df_not_duplicates["m2"], errors="coerce")

    ## 3) Nulls - Only nulls on the house_type_2 variable
    df_not_duplicates["house_type_2"] = df_not_duplicates["house_type_2"].fillna(
        "unknown"
    )

    ## 4) Outliers - After analyzing the distribution over price and m2, we eliminate the houses below 10k price, because they are not reasonable in Madrid
    df_not_outliers_1 = df_not_duplicates[df_not_duplicates["price"] >= 10000]
    df_not_outliers = df_not_outliers_1[df_not_outliers_1["m2"] > 0]

    ## 5) Creation of price per m2
    df_not_outliers["eur_m2"] = df_not_outliers["price"] / df_not_outliers["m2"]

    df_processed = df_not_outliers
    return df_processed
