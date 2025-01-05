import matplotlib.pyplot as plt

years = ['2020', '2021', '2022', '2023', '2024F']
values = [101.05, 100.27, 104.39, 101.05, 99.44]

plt.bar(years, values, color=['#CF352E', '#FFEF00', '#9DC183', '#4F7942', '#355E3B'])
plt.title('Chỉ số sản xuất sản phẩm công nghiệp PPI (%)')
plt.xlabel('Năm')
plt.ylabel('Giá trị (%)')


for i, value in enumerate(values):
    plt.text(i, value + 0.5, str(value), ha='center')

plt.ylim(0, 125)
plt.show()
