import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sb
hs = pd.read_csv("./data/Housing.csv")

def toM(s):
    return "${:,.2f}M".format(s / 1000000)

print(hs.head())
print(hs.describe())
print(hs['mainroad'].unique())
print(hs.dtypes)
prMin = hs['price'].min()
prMax = hs['price'].max()
print(f"Min price: {prMin}, Max price: {prMax}")

mp.figure(figsize=(10, 6))
sb.histplot(data=hs, x='price', hue='mainroad', bins=30, kde=False, palette=['blue', 'red'])
mp.title('Effect of Proximity to Main Roads on Housing Prices (range: ' + toM(prMin) + ' - ' + toM(prMax) + ')')
mp.xlabel('Price')
mp.ylabel('Frequency')
mp.grid(True)
mp.grid(color='#ccc', linestyle='--', linewidth=0.5)
mp.legend(title='Near Main Road', labels=['Yes', 'No'])
mp.tight_layout()
mp.show()
