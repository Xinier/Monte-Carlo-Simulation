import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Return the commission rate
def rate(x):
    if x <= 0.9:
        return 0.02
    elif x <= 0.99:
        return 0.03
    else:
        return 0.04


# Historical data for percent to target performance
mean = 1
sd = 0.1

# Historical data for actual sales target
sale_target_values = [75000, 100000, 200000, 300000, 400000, 500000]
sale_target_prob = [0.3, 0.3, 0.2, 0.1, 0.05, 0.05]

# Number of people in the sales force and the number of simulations
agent = 500
simulation = 1000

# Define a list to keep all the results from each simulation that we want to analyze
stats = []

# Loop through many simulations
for i in range(simulation):
    per_to_tar = np.random.normal(mean, sd, agent)
    sale_target = np.random.choice(sale_target_values, agent, p=sale_target_prob)

    df = pd.DataFrame(data={"Percentage to Target": per_to_tar, "Sales Target": sale_target})

    df["Commission Rate"] = df["Percentage to Target"].apply(rate)
    df["Commission Amount"] = df["Percentage to Target"] * df["Sales Target"] * df["Commission Rate"]

    stats.append(df["Commission Amount"].sum())

result_df = pd.DataFrame(stats, columns=["Total Commission Amount"])
print(result_df.describe())

sns.histplot(data=result_df,x="Total Commission Amount",kde=True)
plt.show()
