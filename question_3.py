import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd


# Define a function to make the plot
def countries_wage_gap_plot(wage_data, countries):
    '''
    *******COMMENTS HERE*********
    '''
    # manipulate the wage data
    filtered_data = wage_data[wage_data['Year'] == 2014]
    filtered_data = filtered_data[['Entity', 'Code', 'Gender wage gap (OECD 2017)']]
    countries = countries[['ADM0_A3', 'geometry']]
    # merge with the geo data
    merged_df = countries.merge(filtered_data, left_on='ADM0_A3', right_on='Code', how='left')
    # Plot the result and save
    fig, ax = plt.subplots(1)
    countries.plot(ax=ax, color='#EEEEEE')
    merged_df.plot(column='Gender wage gap (OECD 2017)', ax=ax, legend=True)
    fig.savefig('wage_gap_2014.png')
