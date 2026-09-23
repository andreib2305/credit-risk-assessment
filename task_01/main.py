from data.data_loader import generate_dataset, plot_risk_distribution
from models.fuzzy_model import FuzzyRiskEval
from models.nn_model import NeuralNetworkEval

def main():

    print("1. Генерация датасета и построение графика.")
    df = generate_dataset(data_count=500, random_state=40)

    print(f"Датасет сформирован! Всего клиентов: {len(df)}")
    print("\nПервые 5 записей датасета:")
    print(df.head())

    # Построение графика
    plot_risk_distribution(df)

    print("\n2. Инициализация модели нечеткой логики.")
    fuzzy_evaluator = FuzzyRiskEval()

    print("\n3. Обучение нейронной сети.")
    nn_evaluator = NeuralNetworkEval(random_state=42)
    metrics = nn_evaluator.train_and_eval(df)

    print("\nРезультаты качества нейронной сети на тестовой выборке:")
    print(f" - Accuracy: {metrics['accuracy']:.2f}")
    print(f" - Precision: {metrics['precision']:.2f}")
    print(f" - Recall: {metrics['recall']:.2f}")
    print(f" - F1-score: {metrics['f1_score']:.2f}")

    print("\n4. Тестирование на новом клиенте.")
    new_client = {
        'Age': 35,
        'Income': 45000,
        'Credits': 2,
        'Late_payments': 4
    }
    print("Параметры клиента:")
    for key, value in new_client.items():
        print(f" - {key}: {value}")

    fuzzy_score, fuzzy_class = fuzzy_evaluator.eval(
        income_val=new_client['Income'],
        late_payments_val=new_client['Late_payments']
    )
    fuzzy_label = "Высокий риск (1)" if fuzzy_class == 1 else "Низкий риск (0)"

    nn_class, nn_label = nn_evaluator.predict_client(new_client)

    print("\nРезультаты оценки:")
    print(f" [Нечеткая логика]: Степень риска = {fuzzy_score:.1f}% | Класс: {fuzzy_label}")
    print(f" [Нейронная сеть]:  Класс: {nn_label}\n")

if __name__ == "__main__":
    main()