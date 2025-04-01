import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

grades = np.array([62, 87, 81, 69, 87, 62, 45, 95, 76, 76, 62, 71, 65, 67, 72, 80, 40, 77, 87, 58,
                   84, 73, 93, 64, 89])
class_limits = np.array([40, 50, 60, 70, 80, 90, 100])

freq_table, _ = np.histogram(grades, bins=class_limits)
midpoints = (class_limits[:-1] + class_limits[1:]) / 2
cum_freq = np.cumsum(freq_table)

plt.plot(midpoints, cum_freq, marker='o', linestyle='-')

plt.fill_between(midpoints, cum_freq, color='skyblue', alpha=0.3)

plt.xlabel('Grades')
plt.ylabel('Cumulative Frequency')
plt.title('Ogive')

plt.grid(True)
plt.show()





