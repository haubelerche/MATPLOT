import matplotlib.pyplot as plt
import numpy as np  # Thêm thư viện numpy

months = ["7-23", "10-23", "1-24", "4-24", "7-24"]
cpi_values = [2.6, 2.96, 3.66, 3.59, 3.45]

plt.figure(figsize=(8, 6))
plt.plot(months, cpi_values, marker='o', linestyle='--', color='green')

z = np.polyfit(range(len(cpi_values)), cpi_values, 1)
p = np.poly1d(z)
plt.plot(months, p(range(len(cpi_values))), color='red')

for i, value in enumerate(cpi_values):
    plt.text(i, value + 0.1, f"{value:.2f}", ha='center', fontsize=10)

plt.title("Sự tăng trưởng CPI của Việt Nam giai đoạn 7/2023 đến 7/2024")
plt.xlabel("Thời gian")
plt.ylabel("CPI")

plt.ylim(2, 5)

plt.grid(True)
plt.show()
