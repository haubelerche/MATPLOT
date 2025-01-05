import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022', '2023', '2024F']
vietnam = [20, 25, 20, 10, 59, 60, 61]
china = [40, 42, 40, 41, 9, 9, 9]
kazakhstan = [28, 28, 25, 29, 22, 20, 20]  # Không có dữ liệu cho Kazakhstan trong năm này

bar_width = 0.25
x = np.arange(len(years))

plt.bar(x - bar_width, vietnam, width=bar_width, color=['#F06038'], label='Việt Nam')
plt.bar(x, china, width=bar_width, color=['#FCC560'], label='Trung Quốc')
plt.bar(x + bar_width, kazakhstan, width=bar_width, color=['#B9C94C'], label='Kazakhstan')

plt.title('Thị phần xuất khẩu phốt pho (%)')
plt.xlabel('Năm')
plt.ylabel('Thị phần (%)')
plt.xticks(x, years)

for i in range(len(years)):
    plt.text(i - bar_width, vietnam[i] + 1, str(vietnam[i]), ha='center')
    plt.text(i, china[i] + 1, str(china[i]), ha='center')
    plt.text(i + bar_width, kazakhstan[i] + 1, str(kazakhstan[i]), ha='center')

plt.legend()

plt.ylim(0, 70)
plt.show()
