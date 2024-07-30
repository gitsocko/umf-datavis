import pandas as pd
import matplotlib.pyplot as plt

boxoffice = pd.read_csv('./data/boxoffice.csv')
print(boxoffice.head())
swAmt = boxoffice.loc[boxoffice['title'] == 'Star Wars: The Last Jedi', 'amount'].iloc[0]
print(swAmt)

plt.figure(figsize=(15, 3))
plt.bar(boxoffice['title'],boxoffice['amount'])
plt.show() # [./out/ica7a.png](https://github.com/gitsocko/umf-datavis/blob/master/out/ica7a.png)

boRkDsc=boxoffice.sort_values(by='rank', ascending=False)
print(boRkDsc.head())

plt.figure(figsize=(15, 3))
plt.bar(boRkDsc['title'],boRkDsc['amount_text']+"M")
plt.title('Ticket Sales (in millions)')
plt.show() # [./out/ica7b.png](https://github.com/gitsocko/umf-datavis/blob/master/out/ica7b.png)

plt.figure(figsize=(10, 3))
plt.bar(boRkDsc['title_short'],boRkDsc['amount_text']+"M")
plt.title('Ticket Sales (in millions), Short Titles')
plt.show() # [./out/ica7c.png](https://github.com/gitsocko/umf-datavis/blob/master/out/ica7c.png)