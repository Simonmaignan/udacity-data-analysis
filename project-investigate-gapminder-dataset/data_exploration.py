#!/usr/bin/env python3

# imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plotLine(df, countries_to_plot, title, ylabel):
    plt.figure(figsize=(8, 8))

    for country in countries_to_plot:
        plt.plot(df.columns, df.loc[country], label=country)
    plt.legend()
    plt.title(title)
    plt.xlabel("Years")
    plt.ylabel(ylabel)