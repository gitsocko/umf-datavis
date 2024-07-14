import pandas as pd
filename = './data/lego_setsHB.csv'
lego=pd.read_csv(filename)

print(lego.head())
print(lego.info())
print(lego.describe())
print(lego[lego['star_rating']>=4])
print(lego[lego['star_rating']>=4]['star_rating'].count())
print(lego.loc[lego['star_rating']>=4,['list_price']].mean().round(2))