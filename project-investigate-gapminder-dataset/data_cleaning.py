#!/usr/bin/env python3

# imports
import pandas as pd
import numpy as np


def fillNaN(dataframe):
    print('test')


def removeYearsInFuture(df, present_year=2018):
    max_year = df.columns.max()
    years_to_drop = np.arange(present_year + 1, max_year + 1)
    df.drop(columns=years_to_drop, inplace=True)

def columns2Ints(df):
    df.columns = df.columns.astype(int)