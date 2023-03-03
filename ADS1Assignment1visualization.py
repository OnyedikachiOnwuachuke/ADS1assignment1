# Import the Libraries or packages

import pandas as pd
import matplotlib.pyplot as plt

# Reading the data into a DataFrame
data_eu = pd.read_csv('GDP_per_capita.csv', index_col=0)
print(data_eu)

# Creating a variable as the list of years as strings
data_year = ['2017', '2018', '2019', '2020', '2021']

# Defining a function that creates a line plot with one line for each country.

def plot_line_gdp_per_capita(data_eu, x_country, y_countries, plot_title, x_label, y_label, legend_loc='best'):
    """
    Plots a line graph given a dataframe, x column, y columns, plot title, x label, and y label.

    Args:
        data_eu (pandas.DataFrame): The dataframe containing thex_col=0)
        x_country (str): The name of the column containing the x-axis data.
        y_countries (list of str): The names of the columns containing the y-axis data.
        plot_title (str): The line plot title.
        x_label (str): The Line plot label for the horizontal-axis.
        y_label (str): The line plot label for the vertical-axis.
        legend_loc (str or int, optional): This set the legend to 'best' as default.

    """

    plt.figure()
    for country in data_eu:
        plt.plot(data_year, data_eu[country], label=country)
    plt.title(plot_title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend(loc=legend_loc)
    plt.savefig('line plot.png')
    plt.show()


plot_line_gdp_per_capita(data_eu, 'year', list(data_eu.columns),
                         'GDP Per Capita of Six(6) European Countries (2017-2021)',
                         'Year', 'GDP per capita(in US dollars)')

# Defining the function plot_bar_gdp_per_capita is to create a bar chart for the countries for a particular year in the dataset

def plot_bar_gdp_per_capita(data_eu, year):
    """Create a bar chart showing the GDP of each country in a specific year.

    Args:
        data_eu (pd.DataFrame): The GDP per capita data.
        year (int): The year to plot.

    Returns:
        None.
    """
# Selecting the columns and assigning the values to the corresponding year 
    gdp_eu = data_eu.loc[year]
    
    plt.bar(gdp_eu.index, gdp_eu.values)
    plt.title(f'GDP per capita of six(6) European Countries ({year})')
    plt.xlabel('Country')
    plt.ylabel('GDP per capita (in US dollars)')
    plt.savefig('GDP per capita for year 2020.png')
    plt.show()


plot_bar_gdp_per_capita(data_eu, 2020)


# The below function plot_scatter_gdp_per_capita is used to compare the GDP per capita of any two countries in the dataset

def plot_scatter_gdp_per_capita(data_eu, country1, country2):
    """Create a scatter plot showing the GDP of two countries over time.

    Args:
        data_eu (pd.DataFrame): The GDP per capita data.
        country1 (str): The first country to plot.
        country2 (str): The second country to plot.

    Returns:
        None.
    """
    plt.scatter(data_eu[country1], data_eu[country2])
    plt.title(f'GDP per capita($) of {country1} vs {country2} (2017-2021)')
    plt.xlabel(country1)
    plt.ylabel(country2)
    plt.savefig('scatter plot of Belgium vs Germany.png')

    plt.show()


plot_scatter_gdp_per_capita(data_eu, 'Belgium', 'Germany')
