import plotly.express as px
import pandas as pd


def gap_management_plot(wage_gap_data, management_data):
    '''
    Describe function
    '''
    # merge on an inner join
    wage_data_2014 = wage_gap_data[wage_gap_data['Year'] == 2014]
    management_data_2014 = management_data[management_data['Year'] == 2014]
    merged_data = wage_data_2014.merge(management_data_2014, left_on='Code', right_on='Code', how='inner')
    # plot data using plotly
    labels = {'Gender wage gap (OECD 2017)': 'Percentage Gender Wage Gap',
              '5.5.2 - Proportion of women in senior and middle management positions (%) - IC_GEN_MGTN': 
              'Percentage of women in senior and middle management positions',
              'Entity_x': 'Country'}
    fig = px.scatter(merged_data, x='Gender wage gap (OECD 2017)',
                     y='5.5.2 - Proportion of women in senior and middle management positions (%) - IC_GEN_MGTN',
                     hover_data=['Entity_x'], 
                     title='Wage Gap vs Proportion of women in senior and middle management positions, 2014',
                     labels=labels)
    fig.write_html('gap_management_plot.html')