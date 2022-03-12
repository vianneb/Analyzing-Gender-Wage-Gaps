'''
Sarah Schafer, Vianne Nguyen, Jessica Robinson
CSE 163 Final Project
Analyzing Gender Wage Gaps

*** Describe purpose
*** Describe what it does
*** Describe data
'''
import pandas as pd
import geopandas as gpd


def test_occupations_wage_gap_plot(test_data):
    """
    Takes a subset of the Glassdoor data and tests
    the occupations_wage_gap_plot function to determine
    if the data is filtered correctly and groupby mean
    values are computed correctly.
    """
    # test filtering by male
    df1 = test_data[test_data['Gender'] == 'Male']
    print('Are there Female values in the Gender column: ',
          'Female' in df1.Gender)
    print(df1)
    # test filtering by female
    df2 = test_data[test_data['Gender'] == 'Female']
    print('Are there Male values in the Gender column: ', 'Male' in df1.Gender)
    print(df2)
    # test groupby and finding average values
    df1_avg_pay = df1.groupby('JobTitle')['BasePay'].mean()
    df2_avg_pay = df2.groupby('JobTitle')['BasePay'].mean()
    print('Male Graphic Designer avg pay matches expected: ',
          df1_avg_pay['Graphic Designer'] == 99464)
    print('Male Software Engineer avg pay matches expected: ',
          df1_avg_pay['Software Engineer'] == 108278)
    print('Female Graphic Designer avg pay matches expected: ',
          df2_avg_pay['Graphic Designer'] == 42363)
    print('Female Warehouse Associate avg_pay matches expected: ',
          df2_avg_pay['Warehouse Associate'] == 90208)
    print('Male Average Pays')
    print(df1_avg_pay)
    print('Female Average Pays')
    print(df2_avg_pay)


def test_time_line_chart(data):
    '''
    Takes a small subset of the OECD data and performs the same data
    manipulation as occurs to the larger, analogous data that is used
    to create the plotly line chart in time_line_chart_plotly() in the
    analysis file.
    Prints out information that shows whether the information contained in
    the filtered data set shows the expected information at each step in
    data filtering.
    '''
    # filter the data
    # filter the data to years pre 1990
    data_pre_1990 = data[data['Year'] <= 1990]
    # check that the maximum year equals 1990
    print(data_pre_1990['Year'].max() == 1990)
    # create a list of the country codes that have data before 1990
    countries_in_pre_1990 = list(data_pre_1990['Code'].unique())
    # check that the only country is Australia
    print('Countries left is only Australia: ',
          countries_in_pre_1990 == ['AUS'])
    print('Countries are formatted as a list: ',
          type(countries_in_pre_1990) == list)
    # filter the original data to only the countries in the above list
    filtered_data = data[data.Code.isin(countries_in_pre_1990)]
    print('Countries represented in data set used to plot: ',
          filtered_data['Entity'].unique())
    # filter the resulting data to years since 1990
    filtered_data = filtered_data[filtered_data['Year'] >= 1990]
    # Check that the maximum year is 2016, and minimu is 1990
    print('Maximum year in filtered_data is 2016: ',
          filtered_data['Year'].max() == 2016)
    print('Minimum year in filtered_data is 1990: ',
          filtered_data['Year'].min() == 1990)
    # Print out whole data frame, just to check it as well
    print(filtered_data)


def main():
    test_wage_data = pd.read_csv('Data/test_wage_data.csv')
    test_oecd_data = pd.read_csv('Data/test_oecd_data.csv')
    test_occupations_wage_gap_plot(test_wage_data)
    test_time_line_chart(test_oecd_data)


if __name__ == '__main__':
    main()
