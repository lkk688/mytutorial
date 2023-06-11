import numpy as np
import pandas as pd
import matplotlib.pyplot as plt#pip install matplotlib
#plt.style.use('seaborn-whitegrid')
import seaborn as sns

# Set the default text font size
plt.rc('font', size=16)
# Set the axes title font size
plt.rc('axes', titlesize=16)
# Set the axes labels font size
plt.rc('axes', labelsize=16)
# Set the font size for x tick labels
plt.rc('xtick', labelsize=14)
# Set the font size for y tick labels
plt.rc('ytick', labelsize=14)
# Set the legend font size
plt.rc('legend', fontsize=14)
# Set the font size of the figure title
plt.rc('figure', titlesize=20)

#Grouped Bar Chart
labels = ['Car@0.7 Hard', 'Car@0.7 Moderate', 'Car@0.7 Easy', 'Ped@0.5 Hard', 'Ped@0.5 Moderate', 'Ped@0.5 Easy', 'Cyclist@0.5 Hard', 'Cyclist@0.5 Moderate', 'Cyclist@0.5 Easy']
group1 = [38.54, 48, 48.8, 43.5, 39.1, 38.8, 46.6, 52.8, 51.6]
group2 = [80.9, 77.7, 76.1, 51.4, 41.9, 41.4, 72.4, 69.6, 68.3]

x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

#plt.figure(figsize=(10,6))
fig, ax = plt.subplots(figsize=(10,7))
rects1 = ax.bar(x - width/2, group1, width, label='Vehicle Lidar Only')
rects2 = ax.bar(x + width/2, group2, width, label='Fusion with Infrastructure')

# # Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Cases')
ax.set_title('BEV AP')
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.xticks(rotation=30)
# for tick in ax.get_xticklabels():
#     tick.set_rotation(45)
spacing = 0.2
fig.subplots_adjust(bottom=spacing)
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

fig, ax = plt.subplots(figsize=(10,7))
rects1 = ax.bar(x - width/2, group1, width, label='Vehicle Lidar Only')
rects2 = ax.bar(x + width/2, group2, width, label='Fusion with Infrastructure')

# # Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Cases')
ax.set_title('3D AP')
ax.set_xticks(x)
ax.set_xticklabels(labels)
plt.xticks(rotation=30)
spacing = 0.2
fig.subplots_adjust(bottom=spacing)
ax.legend()

plt.show()

#save figure as vector-format images (.pdf, eps, svg)
fig.savefig('3dap.pdf')