# https://colab.research.google.com/drive/16tDWeIBlIJ3s2KyC8OiLteE7AZW7T8yH?authuser=1#scrollTo=qAI2uZbpeuj_

# Q1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joypy as jp
from seaborn_qqplot import pplot
import os

file_path = "./data/WorldCupMatches.csv"
tg = pd.read_csv(file_path)
# print(tg.head())


def q2():
    sns.displot(tg, x="Home Team Goals", hue="Year", kind="kde", palette="bright")
    plt.title('Home Goals by Year')
    plt.xlabel('Goals')
    plt.ylabel('Density')
    plt.savefig(os.path.join('./out', 'hw3Q2.png'))
    plt.show()


def q3():
    yr = sorted(tg['Year'].unique())

    plt.figure(figsize=(14, 8))
    ax = sns.violinplot(x='Year', y='Home Team Goals', data=tg, hue='Year', legend=False, palette='bright')
    plt.title('Home Goals by Year')
    plt.xlabel('Year')
    plt.ylabel('Goals')
    ax.set_xticks(range(len(yr)))
    ax.set_xticklabels([str(y) if str(y).endswith('0') else '' for y in yr])
    plt.savefig(os.path.join('./out', 'hw3Q3.png'))
    plt.show()


def q4():
    # plt.style.use('seaborn-white')  # This did not work in my version of Python (deprecated style)
    sns.displot(tg, x="Home Team Goals", hue="Year", kind="kde", height=7, aspect=1.5, palette="bright", legend=True)
    sns.displot(tg, x="Away Team Goals", hue="Year", kind="kde", height=7, aspect=1.5, palette="pastel", legend=True)
    plt.xlabel('Goals')
    plt.ylabel('Density')
    plt.savefig(os.path.join('./out', 'hw3Q4.png'))
    plt.show()


def q5():
    dg = tg.groupby('Home Team Initials')['Home Team Goals'].sum().reset_index()
    ds = dg.sort_values(by='Home Team Goals', ascending=False).head(5)

    plt.figure(figsize=(7, 3))
    sns.barplot(x='Home Team Initials', y='Home Team Goals', data=ds, hue='Home Team Initials', legend=False,
                palette='bright')
    plt.title('Home Goals, Top 5 Countries')
    plt.xlabel('Country Initials')
    plt.ylabel('Total Goals')
    plt.savefig(os.path.join('./out', 'hw3Q5.png'))
    plt.show()


def q6():
    gt = tg.groupby('Home Team Initials')['Home Team Goals'].sum().reset_index()
    ct = gt.sort_values(by='Home Team Goals', ascending=False).head(4)['Home Team Initials']
    dt = tg[tg['Home Team Initials'].isin(ct)]

    plt.style.use('dark_background')
    jp.joyplot(data=dt, by='Home Team Initials', column=['Home Team Goals', 'Away Team Goals'],
                           figsize=(7, 3), overlap=0.5, legend=True)
    plt.title('Home/Away Goals, Top 4 Countries', fontsize=14)
    plt.xlabel('Goals', fontsize=10)
    plt.ylabel('Country', fontsize=10)
    plt.savefig(os.path.join('./out', 'hw3Q6.png'))
    plt.show()


def q7():
    plt.style.use('ggplot')
    pplot(tg, x='Home Team Goals', y='Away Team Goals', kind='qq', height=3, aspect=2,
          display_kws={"identity": True})
    plt.title('Home/Away Goals')
    plt.savefig(os.path.join('./out', 'hw3Q7.png'))
    plt.show()

    # If the data points follow the trajectory of the diagonal line, home/away distributions are similar.
    # Since the angle of the dot trend is slightly different from that of the black line,
    # I would say the distributions are somewhat similar, but not exact.


q2()
q3()
q4()
q5()
q6()
q7()
