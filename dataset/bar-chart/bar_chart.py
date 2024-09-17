import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.randn(50, 2), columns=["x","y"])

bar_data = data.copy()
bar_data['index'] = bar_data.index
sns.barplot(x='index', y='y', data=bar_data)
plt.title("Bar Chart")
plt.show()

# Line plot
sns.lineplot(x='x', y='y', data=data)
plt.title("Line Chart")
plt.show()

# Fill between (this needs to be done after creating a line plot or scatter plot with Matplotlib)
data = data.sort_values('x')
plt.figure()  # Create a new figure
plt.plot(data['x'], data['y'], color='blue')  # Line plot for the fill_between function
plt.fill_between(data['x'], data['y'], color='blue', alpha=0.2)
plt.title("Area Chart")
plt.show()
