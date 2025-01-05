import matplotlib.pyplot as plt
import numpy as np

quarters = ['Q1 2021', 'Q2 2021', 'Q3 2021', 'Q4 2021', 
            'Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022', 
            'Q1 2023', 'Q2 2023', 'Q3 2023', 'Q1 2024', 'Q2 2024', 'Q3 2024']
DGC_values = [80000, 90000, 100000, 110000, 
              95000, 105000, 115000, 120000, 
              110000, 125000, 130000, 135000, 140000, 120000]
VN_index = [1200, 1300, 1250, 1400, 
            1350, 1450, 1400, 1500, 
            1550, 1600, 1580, 1650, 1600, 1620]


plt.figure(figsize=(10, 6))
plt.plot(quarters, DGC_values, marker='o', color='green', label='DGC')
plt.plot(quarters, VN_index, marker='o', color='gray', label='VN-index')
plt.xlabel('Quý', fontsize=14, fontweight='bold')
plt.ylabel('Giá trị', fontsize=14, fontweight='bold')

plt.legend()

plt.xticks(rotation=45)  # Xoay nhãn trục x
plt.tight_layout()  # Căn chỉnh bố cục
plt.show()