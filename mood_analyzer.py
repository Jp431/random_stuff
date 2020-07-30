import pandas as pd
import matplotlib.pyplot as plt
import squarify
import seaborn as sns

file_name = 'moods_2019.csv'

df = pd.read_csv(file_name)

df = df.replace({"mouais": "so-so", "bien": "good",
                 "mauvais": "sad", "super": "happy"})

moods = df['mood'].value_counts().to_frame().reset_index(drop=False)
moods = moods.rename(columns={'index': 'mood', "mood": "count"})
colors = ["aquamarine", "c", "lightsteelblue", "darkviolet"]


# Creating and plotting the data into the chart
squarify.plot(sizes=moods['count'],
              label=moods['mood'],
              color=colors,
              alpha=.4)
plt.axis('off')
plt.title("My mood for 2019")
plt.show()
