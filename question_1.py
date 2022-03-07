"""
How does the wage gap differ between various occupations?
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()

# Define a function to make the plot
def occupations_wage_gap_plot(wage_data):

    # filter into male and female data
    is_male = wage_data['Gender'] == 'Male'
    is_female = wage_data['Gender'] == 'Female'

    male_df = wage_data[is_male]
    female_df = wage_data[is_female]

    # group by occupation and compute average
    male_comp = male_df.groupby('JobTitle')['BasePay'].mean()
    female_comp = female_df.groupby('JobTitle')['BasePay'].mean()

    df1 = pd.DataFrame({'JobTitle':male_comp.index, 'Male Pay':male_comp.values})
    df2 = pd.DataFrame({'JobTitle':female_comp.index, 'Female Pay':female_comp.values})

    merged = df1.merge(df2, left_on='JobTitle', right_on='JobTitle',
                   how='inner')

    #plot results
    merged.plot(x='JobTitle', y=['Male Pay', 'Female Pay'], kind="bar")
    plt.title("Male v. Female Average Base Pay by Occupation")
    plt.xlabel("Job Title")
    plt.ylabel("Dollars USD")

    plt.savefig('/home/occupations_wage_gap.png', bbox_inches='tight')

