#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt

grades = np.array([62, 87, 81, 69, 87, 62, 45, 95, 76, 76, 62, 71, 65, 67, 72, 80, 40, 77, 87, 58, 84, 73, 93, 64, 89])

bins = [40, 50, 60, 70, 80, 90, 100]

hist, bins = np.histogram(grades, bins=bins)

plt.figure(figsize=(10, 5))  
plt.bar(range(len(hist)), hist, width=0.8, align='center', color='skyblue', edgecolor='black')


plt.xticks(range(len(hist)), ['40-50', '50-60', '60-70', '70-80', '80-90', '90-100'])

plt.xlabel('Grade Intervals')
plt.ylabel('Frequency')
plt.title('Bar Chart of Grades')

plt.grid(True)
plt.show()


# In[ ]:




