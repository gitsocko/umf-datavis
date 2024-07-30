import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = pd.read_csv('./data/titanic.csv')

sv = titanic["Survived"]
titanic.loc[sv == 1, "Survived"] = "Survived"
titanic.loc[sv == 0, "Survived"] = "Died"
titanic = titanic[titanic["Pclass"] != "?"]
titanic["Pclass"] = pd.to_numeric(titanic["Pclass"])

g = sns.FacetGrid(titanic, row="Survived", col="Pclass", hue="Sex", margin_titles=True)
g.map(sns.kdeplot, "Age").add_legend()
g.set_axis_labels("Age", "Density")
g.set_titles(row_template="{row_name} Class", col_template="{col_name}")
titles = ['Died in Class 1','Died in Class 2', 'Died in Class 3', 'Survived in Class 1','Survived in Class 2',
          'Survived in Class 3']
for ax,title in zip(g.axes.flatten(),titles):
   ax.set_title(title )

plt.show()