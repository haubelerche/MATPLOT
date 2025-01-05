import matplotlib.pyplot as plt

labels = ['H3PO4 85%', 'Phốt pho vàng', 'WPA 50%', 'Sản phẩm khác']
sizes = [22, 27, 38, 13]  # Tỷ lệ phần trăm
colors = ['#D53302', '#FDC360', '#A0CBAD', '#8FB1BD']  # Màu sắc cho từng phần

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

plt.axis('equal')  
plt.xlabel(labels,fontweight='bold')

plt.show()