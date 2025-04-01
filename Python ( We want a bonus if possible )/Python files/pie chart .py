
import numpy as np
import matplotlib.pyplot as plt

grades = np.array([62, 87, 81, 69, 87, 62, 45, 95, 76, 76, 62, 71, 65, 67, 72, 80, 40, 77, 87, 58,
                   84, 73, 93, 64, 89])

bins = [40, 50, 60, 70, 80, 90, 100]

hist, bins = np.histogram(grades, bins=bins)

labels = ['40-50', '50-60', '60-70', '70-80', '80-90', '90-100']

plt.figure(figsize=(8, 8))  
plt.pie(hist, labels=labels, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)

plt.title('Pie Chart of Grades Distribution')
plt.show()




