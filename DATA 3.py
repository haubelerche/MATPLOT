import matplotlib.pyplot as plt
import numpy as np


years = ['2020', '2021', '2022', '2023', '2024F']
rates = [4, 4, 6, 4.5, 5.3]

0
colors = ['#D53302', '#FDC360', '#A0CBAD', '#8FB1BD', '#00012A']


plt.figure(figsize=(10, 6))
bars = plt.bar(years, rates, color=colors)


z = np.polyfit(range(len(years)), rates, 1)
p = np.poly1d(z)
plt.plot(years, p(range(len(years))), color='blue', linestyle='--')

plt.title('Tỷ lệ lãi suất - Refinancing Rate (%)', fontweight='bold', pad=20)  # Thêm khoảng cách
plt.xlabel('Năm')
plt.ylabel('Refinancing Rate (%)')
plt.ylim(0, 6)


for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 1), ha='center', va='bottom')

plt.show()