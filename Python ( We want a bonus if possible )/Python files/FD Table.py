#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import pandas as pd

grades = np.array([62, 87, 81, 69, 87, 62, 45, 95, 76, 76, 62, 71, 65, 67, 72, 80, 40, 77, 87, 58,
                   84, 73, 93, 64, 89])
class_limits = np.array([40, 50, 60, 70, 80, 90, 100])

freq_table, _ = np.histogram(grades, bins=class_limits)
midpoints = (class_limits[:-1] + class_limits[1:]) / 2
rel_freq = freq_table / len(grades)
cum_freq = np.cumsum(freq_table)

result_table = pd.DataFrame({
    'Class_limit': [f"[{class_limits[i]}-{class_limits[i+1]})" for i in range(len(class_limits)-1)],
    'Frequency': freq_table,
    'Relative_Frequency': rel_freq,
    'Cumulative_Frequency': cum_freq,
    'Midpoints': midpoints
})

print("Table:")
print(result_table)


# In[ ]:




