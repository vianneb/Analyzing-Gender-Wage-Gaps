'''
Description / Header
'''
import pandas as pd
import geopandas as gpd


def test_occupations_wage_gap_plot(test_data):
    '''
    Description
    '''
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


def main():
    test_data = pd.read_csv('Data/test_wage_data.csv')
    test_occupations_wage_gap_plot(test_data)


if __name__ == '__main__':
    main()
