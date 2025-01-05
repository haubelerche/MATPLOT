import matplotlib.pyplot as plt
import numpy as np


years = np.array([2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])
electric_vehicle = np.array([50, 100, 200, 300, 450, 600, 800, 1000, 1200])  # Dữ liệu cho xe điện
energy_storage = np.array([30, 60, 120, 240, 400, 600, 800, 1000, 1200])  # Dữ liệu cho lưu trữ năng lượng


plt.figure(figsize=(10, 6))


plt.bar(years, electric_vehicle, color='#D53302', label='Pin cho xe điện (GWh)')
plt.bar(years, energy_storage, bottom=electric_vehicle, color='#A0CBAD', label='Pin lưu cho trữ năng lượng và thiết bị điện tử (GWh)')


plt.xlabel('Năm', fontsize=14,  fontweight='bold')
plt.ylabel('Giá trị (GWh)', fontsize=14,  fontweight='bold')

plt.xticks(years) 


plt.legend()

plt.show()