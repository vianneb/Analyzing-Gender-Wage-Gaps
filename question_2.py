"""
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

def education_wage_gap_plot(wage_data):
    """
    """


    female = .groupby('Education')['BasePay'].mean()
    male = .groupby('Education')['BasePay'].mean()

    plt.title("Gender Base Pay Gap Based on Education")
    plt.xlabel("Level of Education")
    plt.ylabel("US Dollars")
    plt.savefig('/home/education_wage_gap.png', bbox_inches='tight')
