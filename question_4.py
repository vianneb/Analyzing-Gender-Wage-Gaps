'''
'''


import pandas as pd
import plotly.express as px


def time_line_chart_plotly(data):
    '''
    Description of function *******
    '''
    filtered_data = data[data['Code'] == 'AUS']
    fig = px.line(filtered_data, x='Year', y='Gender wage gap (OECD 2017)')
    fig.write_html('time_line_chart_wage_gap.html')
