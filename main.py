"""
Sarah Schafer, Vianne Nguyen, Jessica Robinson
CSE 163 Final Project
Analyzing Gender Wage Gaps

** Describe the purpose of the main.py file
** Describe what it runs, where results are saved
** Describe data sets used
"""


import geopandas as gpd
import pandas as pd
import analysis
import test


def main():
    # Load in data
    # Geo-spatial data for world countries (geopandas)
    countries = gpd.read_file('Data/countries.geojson')
    # Wage Gap Data From OECD, 2017 (pandas)
    country_wage_data = pd.read_csv('Data/gender-wage-gap-oecd (1).csv')
    # Proportion of women in senior/middle management positions data (pandas)
    management_positions = \
        pd.read_csv('Data/women-in-senior-and-middle-management-positions.csv')
    # Glassdoor Data on occupations and education (pandas)
    occupations_education_data = pd.read_csv('Data/glassdoor_gender_pay_gap.csv')
    # Run Analysis Functions
    analysis.countries_wage_gap_plot(country_wage_data, countries)
    analysis.occupations_wage_gap_plot(occupations_education_data)
    analysis.time_line_chart_plotly(country_wage_data)
    analysis.education_wage_gap_plot(occupations_education_data)
    analysis.gap_management_plot(country_wage_data, management_positions)


if __name__ == '__main__':
    main()
