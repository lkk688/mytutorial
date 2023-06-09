import numpy as np
import pandas as pd
import matplotlib.pyplot as plt#pip install matplotlib
#plt.style.use('seaborn-whitegrid')
import seaborn as sns

#Grouped Bar Chart
labels = ['Car@0.7 Hard', 'Car@0.7 Moderate', 'Car@0.7 Easy', 'Ped@0.5 Hard', 'Ped@0.5 Moderate', 'Ped@0.5 Easy', 'Cyclist@0.5 Hard', 'Cyclist@0.5 Moderate', 'Cyclist@0.5 Easy']
group1 = [38.54, 48, 48.8, 43.5, 39.1, 38.8, 46.6, 52.8, 51.6]
group2 = [80.9, 77.7, 76.1, 51.4, 41.9, 41.4, 72.4, 69.6, 68.3]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, group1, width, label='Vehicle Lidar')
rects2 = ax.bar(x + width/2, group2, width, label='Fusion with Infrastructure')

# # Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Cases')
ax.set_title('BEV AP')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()

#save figure as vector-format images (.pdf, eps, svg)
fig.savefig('bevap.pdf')


#Grouped Bar Chart
labels = ['Car@0.7 Hard', 'Car@0.7 Moderate', 'Car@0.7 Easy', 'Ped@0.5 Hard', 'Ped@0.5 Moderate', 'Ped@0.5 Easy', 'Cyclist@0.5 Hard', 'Cyclist@0.5 Moderate', 'Cyclist@0.5 Easy']
group1 = [29.7, 35, 34.9, 39.2, 33.5, 33, 42.3, 46.8, 45.8]
group2 = [74.2, 65.9, 63.3, 47.6, 36.5, 35.7, 70.3, 65, 63.4]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, group1, width, label='Vehicle Lidar')
rects2 = ax.bar(x + width/2, group2, width, label='Fusion with Infrastructure')

# # Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Cases')
ax.set_title('3D AP')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()

#save figure as vector-format images (.pdf, eps, svg)
fig.savefig('3dap.pdf')