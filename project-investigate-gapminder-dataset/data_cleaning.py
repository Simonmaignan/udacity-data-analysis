#!/usr/bin/env python3

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def fillNaN(df):
    '''Output: DataFrame whose NaN values have been filled with previ
               next or previous valid value
       Input: df (DataFrame)'''
    # Start by propagating the next valid value to fill the NaNs 
    # (this will fill all NaN except if there is just NaN until the end of the row)
    df.fillna(method='bfill', axis='columns', inplace=True)
    # Propagate the last valid value to fill the rest of the NaNs
    df.fillna(method='ffill', axis='columns', inplace=True)


def removeYearsInFuture(df, present_year=2018):
    '''Output: DataFrame with removed columns
       Input: df (DataFrame)
              present_year (int): the year from which to remove the columns'''
    # Retrieve the highest year (last)
    max_year = df.columns.max()
    # and create a vector of year to remove from DataFrame
    years_to_drop = np.arange(present_year + 1, max_year + 1)
    
    df.drop(columns=years_to_drop, inplace=True)


def columns2Int(df):
    '''Output: DataFrame whose column type has been changed to int
       Input: df (DataFrame)'''
    df.columns = df.columns.astype(int)


def values2Float(df):
    '''Output: DataFrame whose value type has been changed to float
       Input: df (DataFrame)'''
    return df.astype(float)