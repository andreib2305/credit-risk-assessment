import matplotlib.pyplot as plt
import numpy as np
import os

output_dir = "charts"
os.makedirs(output_dir, exist_ok=True)

months = np.arange(1, 13)
product_a = [120, 135, 148, 162, 175, 190, 210, 225, 240, 260, 275, 300]
product_b = [80, 88, 95, 100, 110, 115, 130, 140, 155, 160, 170, 185]


fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(months, product_a, label='Продукт А', color='#2b5c8f', linestyle='-', marker='o', linewidth=2)
ax.plot(months, product_b, label='Продукт Б', color='#d95f02', linestyle='--', marker='s', linewidth=2)

ax.set_title('Динамика продаж продуктов А и Б по месяцам', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Месяц', fontsize=12)
ax.set_ylabel('Выручка (тыс. руб.)', fontsize=12)
ax.set_xticks(months)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=11)

plt.tight_layout()
plt.savefig(f'{output_dir}/sales_line.png', dpi=300)
plt.close()


fig, ax = plt.subplots(figsize=(12, 6))

width = 0.35

rects1 = ax.bar(months - width/2, product_a, width, label='Продукт А', color='#2b5c8f')
rects2 = ax.bar(months + width/2, product_b, width, label='Продукт Б', color='#d95f02')

ax.set_title('Сравнение продаж продуктов А и Б', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Месяц', fontsize=12)
ax.set_ylabel('Выручка (тыс. руб.)', fontsize=12)
ax.set_xticks(months)
ax.grid(True, linestyle=':', alpha=0.6, axis='y')
ax.legend(fontsize=11)

ax.bar_label(rects1, padding=3, fontsize=8, rotation=45)
ax.bar_label(rects2, padding=3, fontsize=8, rotation=45)

ax.set_ylim(0, max(product_a) * 1.15)

plt.tight_layout()
plt.savefig(f'{output_dir}/sales_bar.png', dpi=300)
plt.close()


fig, ax = plt.subplots(figsize=(10, 6))

sizes = [val / 2 for val in product_a]

scatter = ax.scatter(
    months, 
    product_a, 
    s=sizes, 
    c=months, 
    cmap='viridis', 
    alpha=0.8, 
    edgecolors='black', 
    linewidth=1.5
)

ax.set_title('Пузырьковая диаграмма продаж Продукта А', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Месяц', fontsize=12)
ax.set_ylabel('Выручка (тыс. руб.)', fontsize=12)
ax.set_xticks(months)
ax.grid(True, linestyle=':', alpha=0.6)

cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label('Номер месяца', fontsize=11)
cbar.set_ticks(months)

plt.tight_layout()
plt.savefig(f'{output_dir}/sales_scatter.png', dpi=300)
plt.close()

print("Все графики успешно построены и сохранены в файлы!")