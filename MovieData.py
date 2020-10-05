
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

mov5 = pd.read_csv('MovieR.csv',encoding ='latin1')



listdel = ['horror','biography','musical','sci-fi','crime','romance','fantasy','mystery','thriller','documentary']
listuse = ['Lionsgate','WB/New Line','Screen Gems','StudioCanal', 'Fox Searchlight Pictures', 'Path_ Distribution','DreamWorks', 'Revolution Studios', 'New Line Cinema','Dimension Films', 'Lionsgate/Summit', 'TriStar','Sony Picture Classics', 'Pacific Data/DreamWorks', 'Disney','MiraMax', 'Weinstein Company', 'Gramercy Pictures','Colombia Pictures', 'Summit Entertainment', 'Vestron Pictures','IFC', 'MGM', 'UA Entertainment', 'New Market Films', 'Orion']
len(listuse)



for each in listdel:
    mov5 = mov5.drop(mov5[mov5['Genre'] == each].index)
for every in listuse:
    mov5 = mov5.drop(mov5[mov5.Studio == every].index)


sns.set_style("darkgrid")
ax = sns.boxplot(data=mov5,x='Genre',y='Gross % US',color = 'lightgray',showfliers=False)
sns.stripplot(data=mov5,x='Genre',y='Gross % US',hue='Studio')
ax.legend(bbox_to_anchor=(1.1,1))
