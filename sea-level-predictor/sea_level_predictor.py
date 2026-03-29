import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    plt.clf()  # clears everything

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = range(df["Year"].min(), 2051)  # extend to 2050
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, "r", label="Best fit line (all data)")

    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    res_recent = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_recent = range(2000, 2051)
    y_recent = res_recent.intercept + res_recent.slope * x_recent
    plt.plot(x_recent, y_recent, "g", label="Best fit line (2000+ data)")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()