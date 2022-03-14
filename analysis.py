"""
Sarah Schafer, Vianne Nguyen, Jessica Robinson
CSE 163 Final Project
Analyzing Gender Wage Gaps

In this module, we define functions that create visualizations that show
various aspects of the gender wage gap.
These visualizations are:
- occupations_wage_gap.png, which is created by the occupations_wage_gap_plot
function, and is a bar chart comparing the base pay of various occupations
between genders.  This function takes as a parameter a dataframe of the Kaggle
Glassdoor data.
- education_wage_gap.png, which is created by the education_wage_gap_plot
function, and is a bar chart comparing the base pay of various occupations
between genders.  This function takes as a parameter a dataframe of the Kaggle
Glassdoor data.
- wage_gap_2014.png, which is created by the countries_wage_gap_plot function,
and is a world map that shows the relative gender wage gap of the countries
included in the OECD data set in 2014.  Countries without data are filled in
with grey.
- time_line_chart_wage_gap.html, which is created by the time_line_chart
function, and is an html file that represents a plotly visualization that shows
how a few countries' wage gaps have changed over time since 1990. The countries
we filtered to are countries in the OECD data set that had data before or
starting in 1990.
- gap_management_plot.html, which is creeated by the gap_management_plot
function, which takes both the OECD gender wage gap data and the Our World in
Data management data set and merges them to analyze how the proportion of women
in senior and middle management positions of a country impacts the wage gap of
the country.  The html file that is produced represents a plotly visualization
that is a scatter plot, where each point represents a different country in the
year 2014.

To create these plots, we used the libraries:
- matplotlib
- pandas
- seaborn
- plotly
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px


sns.set()


def occupations_wage_gap_plot(wage_data):
    """
    Takes the Glassdoor dataset with income for various occupations
    based on gender and plots a bar chart depicting the average male
    and female pay for each occupation. The figure is saved in a file
    occupations_wage_gap.png.
    """
    # filter into male and female data
    is_male = wage_data['Gender'] == 'Male'
    is_female = wage_data['Gender'] == 'Female'
    male_df = wage_data[is_male]
    female_df = wage_data[is_female]
    # group by occupation and compute average
    male_comp = male_df.groupby('JobTitle')['BasePay'].mean()
    female_comp = female_df.groupby('JobTitle')['BasePay'].mean()
    # turn series into a dataframe to plot
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
    '''
    A bar graph is plotted from the information in the Glassdoor dataset to
    show the average pay gap between men and women depending on their levels of
    education.
    '''
    # female and male data is filtered
    female = wage_data[wage_data['Gender'] == 'Female']
    male = wage_data[wage_data['Gender'] == 'Male']
    # computes average after it is grouped by education
    female_avg = female.groupby('Education')['BasePay'].mean()
    male_avg = male.groupby('Education')['BasePay'].mean()
    # in order to plot, series is turned into a dataframe
    df_female = pd.DataFrame({'Education': female_avg.index,
                              'Female Pay': female_avg.values})
    df_male = pd.DataFrame({'Education': male_avg.index,
                            'Male Pay': male_avg.values})
    data_merge = df_female.merge(df_male, left_on='Education',
                                 right_on='Education', how='inner')
    # plot information and results
    data_merge.plot(x='Education', y=['Female Pay', 'Male Pay'], kind='bar')
    plt.title("Gender Base Pay Gap Based on Education")
    plt.xlabel("Level of Education")
    plt.ylabel("US Dollars")
    plt.savefig('education_wage_gap.png', bbox_inches='tight')


def countries_wage_gap_plot(wage_data, countries):
    '''
    Takes the OECD wage gap data set as a pandas DataFrame and the geospatial
    data set as a GeoPandas data frame, and creates a map visualization that
    encodes the relative Gender Wage Gap of each country included in the data
    set by color. All countries that have no data on the gender wage gap are
    colored grey (#EEEEEE).  The map is saved as: wage_gap_2014.png
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
    plt.title("Gender Wage Gap for OECD Countries as a Percentage, 2014")
    fig.savefig('wage_gap_2014.png')


def time_line_chart(data):
    '''
    This function takes the OECD dataset and produces a line chart using plotly
    that shows how the wage gap has changed over time.
    The resulting plotly chart will be stored in
    'time_line_chart_wage_gap.html'
    The OECD dataset has the columns: Entity, Code, Year, and
    Gender wage gap (OECD 2017).
    In order to see the trends over long periods of time, we only plotted
    entities with data before 1990.  This gave us roughly 25 years of
    data to analyze trends.
    This analyzes question 4 of our report.
    '''
    # filter the data
    # filter the data to years pre 1990
    data_pre_1990 = data[data['Year'] <= 1990]
    # create a list of the country codes that have data before 1990
    countries_in_pre_1990 = list(data_pre_1990['Code'].unique())
    # filter the original data to only the countries in the above list
    filtered_data = data[data.Code.isin(countries_in_pre_1990)]
    # filter the resulting data to years since 1990
    filtered_data = filtered_data[filtered_data['Year'] >= 1990]
    # plot figure
    fig = px.line(filtered_data, x='Year', y='Gender wage gap (OECD 2017)',
                  color='Entity', title='Gender Wage Gap Over Time by Country')
    fig.write_html('time_line_chart_wage_gap.html')


def gap_management_plot(wage_gap_data, management_data):
    '''
    Takes the OECD data and the Our World in Data management data as pandas
    DataFrames, filters the data to the year 2014, and merges the data by
    entity using an inner join.  Then creates a plotly scatter plot that
    shows the relationship between countries' wage gap and proportion of
    women in senior and middle management.  Each point represents a
    different country, so hovering over each point shows the data for each
    country.
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
