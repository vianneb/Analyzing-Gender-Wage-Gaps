"""
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

def education_wage_gap_plot(wage_data):
    """
    """
    female = wage_data[wage_data['Gender'] == 'Female']
    male = wage_data[wage_data['Gender'] == 'Male']

    female_avg = female.groupby('Education')['BasePay'].mean()
    male_avg = male.groupby('Education')['BasePay'].mean()

    df_female = pd.DataFrame({'Education': female_avg.index, 'Female Pay':female_avg.values})
    df_male = pd.DataFrame({'Education': male_avg.index, 'Male Pay':male_avg.values})

    data_merge = df_female.merge(df_male, left_on='Education', right_on='Education', how='inner')

    data_merge.plot(x='Education', y=['Female Pay', 'Male Pay'], kind='bar')
    plt.title("Gender Base Pay Gap Based on Education")
    plt.xlabel("Level of Education")
    plt.ylabel("US Dollars")
    plt.savefig('education_wage_gap.png', bbox_inches='tight')