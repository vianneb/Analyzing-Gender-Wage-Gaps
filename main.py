"""
Sarah Schafer, Vianne Nguyen, Jessica Robinson
CSE 163 Final Project
Analyzing Gender Wage Gaps

This module has a main method that calls the functions
defined in analysis.py, which create a series of data
visualizations that help represent the gender wage gap.
In order to call these methods, this file first has to
use the geopandas and pandas libraries to load in our data.

It also has the function compute_statistics, which takes our
three data sets pertaining to gender wage gap data, and computes
and prints summary statistics about them.

Our data consists of four data sets:
- gender-wage-gap-oecd (1).csv - a dataset from OECD that has
columns representing the country the data is for (entity),
the year, and the Gender Wage gap for that country and year
as a percentage.
- women-in-senior-and-middle-management-positions.csv - a dataset
from Our World in Data that has columns relating to the country
the data is for (entity), the year, and the proportion of women
in senior and middle management positions (as a percentage).
- glassdoor_gender_pay_gap.csv - a dataset from Kaggle from Glassdoor
that has columns for the type of job, the gender of the individual,
their performance evaluation, their highest education level, their
department, their seniority, their base pay, and their bonus.  For
our analysis, we primarily looked at job titles, gender, education,
base pay, and bonus information.
- countries.json, which is a geospatial dataset that is used to
create a map of the world to analyze differences in the gender wage gap
"""


import geopandas as gpd
import pandas as pd
import analysis


def compute_statistics(oecd_data, glassdoor_data, management_data):
    grouped_oecd = oecd_data.groupby('Entity')
    print('There are', len(grouped_oecd), 'countries in the OECD data.')
    print('The average wage gap, over all years for any country, is',
          round(oecd_data['Gender wage gap (OECD 2017)'].mean(), 2))
    men_glassdoor = glassdoor_data[glassdoor_data['Gender'] == 'Male']
    women_glassdoor = glassdoor_data[glassdoor_data['Gender'] == 'Female']
    num_men_glassdoor = len(men_glassdoor)
    num_women_glassdoor = len(women_glassdoor)
    print("In the Glassdoor data set, there are", num_men_glassdoor, "men",
          "and", num_women_glassdoor, "women.")
    print("This means there are", round(num_men_glassdoor / num_women_glassdoor, 2),
          "times more men than women included in the dataset.")
    men_avg_seniority = round(men_glassdoor['Seniority'].mean(), 2)
    women_avg_seniority = round(women_glassdoor['Seniority'].mean(), 2)
    print('For men, the average seniority was', men_avg_seniority,
          'while for women the average seniority was', women_avg_seniority)
    copy_management_data = management_data.copy()
    long_column_name = '5.5.2 - Proportion of women in senior and' + \
        ' middle management positions (%) - IC_GEN_MGTN'
    copy_management_data = copy_management_data.rename(columns={long_column_name:
                                              'women_in_management'})
    print('The average proportion of women in senior and middle management',
          'positions, for any country and across all years, is',
          round(copy_management_data['women_in_management'].mean(), 2))
    


def main():
    # Load in data
    # Geo-spatial data for world countries (geopandas)
    countries = gpd.read_file('Data/countries.geojson')
    # Wage Gap Data From OECD, 2017 (pandas)
    country_wage_df = pd.read_csv('Data/gender-wage-gap-oecd (1).csv')
    # Proportion of women in senior/middle management positions data (pandas)
    management_positions_df = \
        pd.read_csv('Data/women-in-senior-and-middle-management-positions.csv')
    # Glassdoor Data on occupations and education (pandas)
    occupations_education_df = pd.read_csv('Data/glassdoor_gender_pay_gap.csv')
    # Compute basic statistics
    compute_statistics(country_wage_df, occupations_education_df,
                       management_positions_df)
    # Run Analysis Functions
    analysis.countries_wage_gap_plot(country_wage_df, countries)
    analysis.occupations_wage_gap_plot(occupations_education_df)
    analysis.time_line_chart(country_wage_df)
    analysis.education_wage_gap_plot(occupations_education_df)
    analysis.gap_management_plot(country_wage_df, management_positions_df)


if __name__ == '__main__':
    main()
