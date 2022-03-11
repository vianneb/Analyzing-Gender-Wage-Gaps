"""
How does the wage gap differ between various occupations?
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

sns.set()


def occupations_wage_gap_plot(wage_data):
    # filter into male and female data
    is_male = wage_data['Gender'] == 'Male'
    is_female = wage_data['Gender'] == 'Female'

    male_df = wage_data[is_male]
    female_df = wage_data[is_female]

    # group by occupation and compute average
    male_comp = male_df.groupby('JobTitle')['BasePay'].mean()
    female_comp = female_df.groupby('JobTitle')['BasePay'].mean()

    df1 = pd.DataFrame({'JobTitle': male_comp.index,
                        'Male Pay': male_comp.values})
    df2 = pd.DataFrame({'JobTitle': female_comp.index,
                        'Female Pay': female_comp.values})
    merged = df1.merge(df2, left_on='JobTitle', right_on='JobTitle',
                       how='inner')
    # plot results
    merged.plot(x='JobTitle', y=['Male Pay', 'Female Pay'], kind="bar")
    plt.title("Male v. Female Average Base Pay by Occupation")
    plt.xlabel("Job Title")
    plt.ylabel("Dollars USD")

    plt.savefig('occupations_wage_gap.png', bbox_inches='tight')


def education_wage_gap_plot(wage_data):
    """
    """
    female = wage_data[wage_data['Gender'] == 'Female']
    male = wage_data[wage_data['Gender'] == 'Male']

    female_avg = female.groupby('Education')['BasePay'].mean()
    male_avg = male.groupby('Education')['BasePay'].mean()

    df_female = pd.DataFrame({'Education': female_avg.index,
                              'Female Pay': female_avg.values})
    df_male = pd.DataFrame({'Education': male_avg.index,
                            'Male Pay': male_avg.values})

    data_merge = df_female.merge(df_male, left_on='Education',
                                 right_on='Education', how='inner')

    data_merge.plot(x='Education', y=['Female Pay', 'Male Pay'], kind='bar')
    plt.title("Gender Base Pay Gap Based on Education")
    plt.xlabel("Level of Education")
    plt.ylabel("US Dollars")
    plt.savefig('education_wage_gap.png', bbox_inches='tight')


def countries_wage_gap_plot(wage_data, countries):
    '''
    *******COMMENTS HERE*********
    '''
    # manipulate the wage data
    filtered_data = wage_data[wage_data['Year'] == 2014]
    filtered_data = filtered_data[['Entity', 'Code',
                                   'Gender wage gap (OECD 2017)']]
    countries = countries[['ADM0_A3', 'geometry']]
    # merge with the geo data
    merged_df = countries.merge(filtered_data, left_on='ADM0_A3',
                                right_on='Code', how='left')
    # Plot the result and save
    fig, ax = plt.subplots(1)
    countries.plot(ax=ax, color='#EEEEEE')
    merged_df.plot(column='Gender wage gap (OECD 2017)', ax=ax, legend=True)
    fig.savefig('wage_gap_2014.png')


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


def gap_management_plot(wage_gap_data, management_data):
    '''
    Describe function
    '''
    # merge on an inner join
    wage_data_2014 = wage_gap_data[wage_gap_data['Year'] == 2014]
    management_data_2014 = management_data[management_data['Year'] == 2014]
    merged_data = wage_data_2014.merge(management_data_2014, left_on='Code',
                                       right_on='Code', how='inner')
    # rename longest column name
    long_column_name = '5.5.2 - Proportion of women in senior and' + \
        ' middle management positions (%) - IC_GEN_MGTN'
    merged_data = merged_data.rename(columns={long_column_name:
                                              'women_in_management'})
    # plot data using plotly
    labs = {'Gender wage gap (OECD 2017)': 'Percentage Gender Wage Gap',
            'women_in_management':
            'Percentage of women in senior/middle management positions',
            'Entity_x': 'Country'}
    plot_title = 'Wage Gap vs Proportion of women in senior/middle' + \
        ' management positions, 2014'
    fig = px.scatter(merged_data, x='Gender wage gap (OECD 2017)',
                     y='women_in_management',
                     hover_data=['Entity_x'],
                     title=plot_title,
                     labels=labs)
    fig.write_html('gap_management_plot.html')
