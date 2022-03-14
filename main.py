"""
Sarah Schafer, Vianne Nguyen, Jessica Robinson
CSE 163 Final Project
Analyzing Gender Wage Gaps

This module has a main method that calls the functions
defined in analysis.py, which create a series of data
visualizations that help represent the gender wage gap.
In order to call these methods, this file first has to
use the geopandas and pandas libraries to load in our data.
Our data consists of four data sets:
gender-wage-gap-oecd (1).csv -
"""


import geopandas as gpd
import pandas as pd
import analysis


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
    # Run Analysis Functions
    analysis.countries_wage_gap_plot(country_wage_df, countries)
    analysis.occupations_wage_gap_plot(occupations_education_df)
    analysis.time_line_chart_plotly(country_wage_df)
    analysis.education_wage_gap_plot(occupations_education_df)
    analysis.gap_management_plot(country_wage_df, management_positions_df)


if __name__ == '__main__':
    main()
