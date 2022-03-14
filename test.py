'''
Sarah Schafer, Vianne Nguyen, Jessica Robinson
CSE 163 Final Project
Analyzing Gender Wage Gaps

For our project, we decided to create a number of data visualizations
to help us better understand the gender wage gap on a variety of different
factors, including country, year, and occupation.  To do this, we had to
do a lot of data wrangling, and in order to make sure we did this
correctly, we created this file.
This file defines and calls testing functions that follow the same data
filtering processes as the functions in the analysis file, but also use
print statements to make sure that the results of each step of data filtering
are what is expected.  These functions do all of the data processing in the
analysis file, but they do not create the plots.
Instead of using the whole data sets for this file, we only load in and
process small subsets of the data that are identical in structure to the
actual data sets.  These tests will not be called when main.py is run, but
rather are run by running the main method of this file, test.py.
test_management_data.csv mirrors the
women-in-senior-and-middle-management-positions.csv file, which has columns
relating to the country the data is for (entity), the year, and the proportion
of women in senior and middle management positions (as a percentage).
test_oecd_data.csv mirros the gender-wage-gap-oecd (1).csv file, which has
columns representing the country the data is for (entity), the year, and the
Gender Wage gap for that country and year as a percentage. ****
test_wage_data.csv mirrors the glassdoor_gender_pay_gap.csv file, which has
columns for the type of job, the gender of the individual, their performance
evaluation, their highest education level, their department, their seniority,
their base pay, and their bonus.  For our analysis, we primarily looked at
job titles, gender, education, base pay, and bonus information. ***
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
    print('Testing Occupation data filtering:')
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


def test_education_wage_gap_plot(test_data):
    """
    Tests the education_wage_gap_plot function using
    a smaller group of data taken from the Glassdoor
    dataset.
    """
    print()
    print('Testing filtering for Education plot')
    # tests the filtering by female and male
    female = test_data[test_data['Gender'] == 'Female']
    male = test_data[test_data['Gender'] == 'Male']
    print('Female' in female.Gender)
    print(female)
    print('Male' in female.Gender)
    print(male)

    # tests the groupby as well as the values for the average
    female_avg = female.groupby('Education')['BasePay'].mean()
    male_avg = male.groupby('Education')['BasePay'].mean()
    print(female_avg)
    print(male_avg)
    print(female_avg['College'] == 42363)
    print(male_avg['College'] == 108476)
    print(female_avg['PhD'] == 90208)


def test_countries_plot(wage_data, countries):
    '''
    *******COMMENTS HERE*********
    '''
    print()
    print('Testing data filtering for wage gap map')
    # manipulate the wage data
    filtered_data = wage_data[wage_data['Year'] == 2014]
    # Check (visually) if data is only in year 2014
    print('Filtered data to 2014: ', filtered_data)
    countries = countries[['ADM0_A3', 'geometry']]
    # merge with the geo data
    merged_df = countries.merge(filtered_data, left_on='ADM0_A3',
                                right_on='Code', how='left')
    # Check columns visually, and check if did a left merge (all countries)
    print('Columns for merged data: ', merged_df.columns)
    print('Length of merged data is the same as length of geo data: ',
          len(merged_df) == len(countries))


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
    print()
    print('Testing data filtering for wage gap over time')
    # filter the data
    # filter the data to years pre 1990
    data_pre_1990 = data[data['Year'] <= 1990]
    # check that the maximum year equals 1990
    print('Maximum Year in data_pre_1990 is 1990: ',
          data_pre_1990['Year'].max() == 1990)
    # create a list of the country codes that have data before 1990
    countries_in_pre_1990 = list(data_pre_1990['Code'].unique())
    # check that the only country is Australia
    print('Countries left is only UK: ',
          countries_in_pre_1990 == ['GBR'])
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


def test_gap_management(wage_gap_data, management_data):
    '''
    Describe function
    '''
    print()
    print('Testing Data Filtering for Wage Gap and Management Data')
    # merge on an inner join
    wage_data_2014 = wage_gap_data[wage_gap_data['Year'] == 2014]
    management_data_2014 = management_data[management_data['Year'] == 2014]
    merged_data = wage_data_2014.merge(management_data_2014, left_on='Code',
                                       right_on='Code', how='inner')
    # See if the merged data frame has one row
    print('Merged data, should have one row: ', merged_data)
    # rename longest column name
    long_column_name = '5.5.2 - Proportion of women in senior and' + \
        ' middle management positions (%) - IC_GEN_MGTN'
    merged_data = merged_data.rename(columns={long_column_name:
                                              'women_in_management'})
    # Test that the column names are as expected
    print('Merged data column names: ', merged_data.columns)


def main():
    countries = gpd.read_file('Data/countries.geojson')
    test_wage_data = pd.read_csv('Data/test_wage_data.csv')
    test_oecd_data = pd.read_csv('Data/test_oecd_data.csv')
    test_management_data = pd.read_csv('Data/test_management_data.csv')
    test_occupations_wage_gap_plot(test_wage_data)
    test_education_wage_gap_plot(test_wage_data)
    test_countries_plot(test_oecd_data, countries)
    test_time_line_chart(test_oecd_data)
    test_gap_management(test_oecd_data, test_management_data)


if __name__ == '__main__':
    main()
