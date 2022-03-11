import geopandas as gpd
import pandas as pd
import analysis
import test


def main():
    countries = gpd.read_file('Data/countries.geojson')
    country_wage_data = pd.read_csv('Data/gender-wage-gap-oecd (1).csv')
    management_positions = \
        pd.read_csv('Data/women-in-senior-and-middle-management-positions.csv')
    occupations_wage_data = pd.read_csv('Data/glassdoor_gender_pay_gap.csv')
    analysis.countries_wage_gap_plot(country_wage_data, countries)
    analysis.occupations_wage_gap_plot(occupations_wage_data)
    analysis.time_line_chart_plotly(country_wage_data)
    analysis.education_wage_gap_plot(occupations_wage_data)
    analysis.gap_management_plot(country_wage_data, management_positions)


if __name__ == '__main__':
    main()
