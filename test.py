import geopandas as gpd
import pandas as pd
import question_1
# import question_2
import question_3
import question_4
import question_5


def main():
    countries = gpd.read_file('Data/countries.geojson')
    country_wage_data = pd.read_csv('Data/gender-wage-gap-oecd (1).csv')
    management_positions = pd.read_csv('Data/women-in-senior-and-middle-management-positions.csv')
    occupations_wage_data = pd.read_csv('Data/glassdoor_gender_pay_gap.csv')
    question_3.countries_wage_gap_plot(country_wage_data, countries)
    question_1.occupations_wage_gap_plot(occupations_wage_data)
    question_4.time_line_chart_plotly(country_wage_data)
    # question_2.education_wage_gap_plot(education_wage_data)
    question_5.gap_management_plot(country_wage_data, management_positions)


if __name__ == '__main__':
    main()
