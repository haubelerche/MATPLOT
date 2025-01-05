import matplotlib.pyplot as plt

categories = [
    'Nam Tiến Lào Cai',
    'Phốt pho vàng Việt Nam',
    'Phốt pho Việt Nam',
    'Apatit Việt Nam',
    'Phốt pho vàng Lào Cai',
    'Đồng Nam Á Lào Cai',
    'DGC'
]
values = [15000, 20000, 25000, 30000, 35000, 40000, 60000]  # Giá trị tương ứng


plt.figure(figsize=(10, 6))
bars = plt.barh(categories, values, color=['#A0CBAD'] * 6 + ['#d62728'])  # Màu cho DGC là đỏ

plt.xlabel('Giá trị', fontweight='bold')


for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, bar.get_width(), 
             va='center', ha='left')

plt.xlim(0, 70000) 
plt.show()
