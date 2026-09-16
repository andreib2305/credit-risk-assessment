import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.random.seed(777)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(BASE_DIR, 'time_series_analysis.png')

def plot_graph(df: pd.DataFrame, monthly_sales: pd.DataFrame):
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))

    axes[0].plot(
        df.index, df['Sales'], color='gray', alpha=0.5, label='Дневные продажи'
    )
    axes[0].plot(
        df.index,
        df['MA7'],
        color='blue',
        linewidth=1.5,
        label='Скользящее среднее (7 дней)',
    )
    axes[0].plot(
        df.index,
        df['MA30'],
        color='red',
        linewidth=2,
        label='Скользящее среднее (30 дней)',
    )
    axes[0].set_title('Дневные продажи и скользящие средние')
    axes[0].set_ylabel('Продажи')
    axes[0].legend()
    axes[0].grid(True, linestyle='--', alpha=0.7)

    axes[1].bar(
        monthly_sales.index.strftime('%Y-%m'),
        monthly_sales.values,
        color='skyblue',
        edgecolor='black',
    )
    axes[1].set_title('Месячные суммы продаж')
    axes[1].set_xlabel('Месяц')
    axes[1].set_ylabel('Суммарные продажи')
    axes[1].tick_params(axis='x', rotation=45)
    axes[1].grid(True, linestyle='--', alpha=0.5, axis='y')

    plt.tight_layout()

def save_file():
    plt.savefig(output_path, dpi=300)
    print(f"\n8. График сохранен по пути: {output_path}")

def main():
    dates = pd.date_range(start='2022-01-01', end='2023-12-31', freq='D')
    n_days = len(dates)

    trend = np.linspace(0, 30, n_days)
    sales_data = np.random.poisson(lam=80, size=n_days) + trend

    df = pd.DataFrame({'Sales': sales_data}, index=dates)
    print('1. Первые 5 строк DataFrame:')
    print(df.head())

    monthly_sales = df['Sales'].resample('ME').sum()
    print('\n2. Первые 5 месяцев продаж:')
    print(monthly_sales.head())

    df['MA7'] = df['Sales'].rolling(window=7).mean()
    df['MA30'] = df['Sales'].rolling(window=30).mean()

    quarterly_sales = df['Sales'].resample('QE').sum().to_period('Q')
    print('\n4. Квартальные продажи:')
    print(quarterly_sales)

    df['Previous_Day'] = df['Sales'].shift(1)
    df['Daily_Change'] = df['Sales'] - df['Previous_Day']
    print("\n5-6. DataFrame со сдвигом и изменениями:")
    print(df.head())

    plot_graph(df=df, monthly_sales=monthly_sales)
    save_file()

if __name__ == "__main__":
    main()

