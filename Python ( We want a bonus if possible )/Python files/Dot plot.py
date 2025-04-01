#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import matplotlib.pyplot as plt

grades = np.array([62, 87, 81, 69, 87, 62, 45, 95, 76, 76, 62, 71, 65, 67, 72, 80, 40, 77, 87, 58,
                   84, 73, 93, 64, 89])

indices = np.arange(len(grades))

plt.figure(figsize=(10, 5)) 
plt.plot(indices, grades, marker='o', linestyle='none', color='skyblue', markersize=8)

plt.xlabel('Student')
plt.ylabel('Grade')
plt.title('Dot Plot of Grades')

plt.grid(True)
plt.show()


# In[ ]:




