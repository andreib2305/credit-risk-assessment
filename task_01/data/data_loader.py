import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generate_dataset(data_count: int = 500, random_state: int = 42) -> pd.DataFrame:
    np.random.seed(random_state)

    age = np.random.randint(18, 70, size=data_count)
    income = np.random.randint(30000, 200000, size=data_count)
    credit_count = np.random.randint(0, 6, size=data_count)
    late_payments = np.random.randint(0, 8, size=data_count)

    risk_score = (
            (income < 60000).astype(int) + (credit_count >= 4).astype(int) +
            (late_payments >= 3).astype(int)
    )
    risk = (risk_score >= 2).astype(int)

    df = pd.DataFrame({
        'Age': age,
        'Income': income,
        'Credits': credit_count,
        'Late_payments': late_payments,
        'Risk': risk
    })

    return df

def plot_risk_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        df['Income'],
        df['Late_payments'],
        c=df['Risk'],
        cmap='coolwarm',
        alpha=0.7,
        edgecolors='k'
    )

    plt.title('Зависимость кредитного риска от Дохода и Количества просрочек')
    plt.xlabel('Доход (руб.)')
    plt.ylabel('Количество просрочек')
    plt.colorbar(scatter, label='Риск (0 = Низкий, 1 = Высокий)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
