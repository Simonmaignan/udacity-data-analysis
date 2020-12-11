#!/usr/bin/env python3

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plotLine(df, countries_to_plot, title, ylabel):
    '''Output: Line plot of the value in df for the given countries (index)
       Input: df (DataFrame)
              countries_to_plot ([str]): a list of countries from df to plot
              title (str): the title of the plot
              ylabel (str): the ylabel of the plot'''
    plt.figure(figsize=(8, 8))

    for country in countries_to_plot:
        plt.plot(df.columns, df.loc[country], label=country)
    plt.legend()
    plt.title(title)
    plt.xlabel("Years")
    plt.ylabel(ylabel)