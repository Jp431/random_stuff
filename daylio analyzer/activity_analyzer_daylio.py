import squarify
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import style
from collections import Counter
import matplotlib.pyplot as plt


# Activate Seaborn
sns.set()

# 'Root' variables
chart_name = "My activity - 2019"
file_name = "daylio_data_2019.csv"

# Reads the file and replace " | " with "|"
data = ""

with open(file_name) as file:
    data = file.read().replace(" | ", "|")

with open("update_" + file_name, "w") as file:
    file.write(data)


# Imports the file
df = pd.read_csv("update_" + file_name)


activities = df["activities"]
activities = activities.str.strip()
activities = activities.str.upper()
activities = activities.str.split("|", expand=True)
activities = activities.applymap(
    lambda x: x.strip() if isinstance(x, str) else x)
activities = activities.apply(pd.value_counts)
activities["Total"] = (activities.iloc[:, 0:]).sum(axis=1)
activities["Percentage"] = round(
    100 * activities["Total"] / sum(activities["Total"]), 2)
activities = activities.reset_index()
activities = activities.rename(columns={'index': 'activity'})
activities = activities[['activity', 'Total', "Percentage"]]
activities = activities.sort_values(by='Total', ascending=False)

label_for_chart = activities[['Total']].to_string(index=False)

"""
************************************************
    CREATING THE CHART
************************************************
"""

params = {'xtick.labelsize': 6, 'ytick.labelsize': 10}
plt.rcParams.update(params)
plt.title(chart_name)
plt.bar(activities['activity'], activities['Total'],
        align="center", label=label_for_chart)


# To add labels
plt.legend()
plt.show()
