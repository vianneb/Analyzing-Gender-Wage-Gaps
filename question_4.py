'''
'''


import plotly.express as px


def time_line_chart_plotly(data):
    '''
    Description of function *******
    '''
    filtered_data = filter_countries_1990(data)
    fig = px.line(filtered_data, x='Year', y='Gender wage gap (OECD 2017)',
                  color='Entity', title='Gender Wage Gap Over Time by Country')
    fig.write_html('time_line_chart_wage_gap.html')


def filter_countries_1990(data):
    '''
    Description of function ***********
    '''
    data_pre_1990 = data[data['Year'] <= 1990]
    countries_in_pre_1990 = list(data_pre_1990['Code'].unique())
    filtered_data = data[data.Code.isin(countries_in_pre_1990)]
    filtered_data = filtered_data[filtered_data['Year'] >= 1990]
    return filtered_data
