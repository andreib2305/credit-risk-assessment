import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

class NeuralNetworkEval:

    def __init__(self, random_state: int = 42):
        self.random_state = random_state
        self.scaler = StandardScaler()
        self.model = MLPClassifier(
            hidden_layer_sizes=(16, 8),
            max_iter=500,
            random_state=self.random_state
        )

    def train_and_eval(self, df: pd.DataFrame) -> dict:
        x = df[['Age', 'Income', 'Credits', 'Late_payments']]
        y = df['Risk']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=self.random_state)

        x_train_scaled = self.scaler.fit_transform(x_train)
        x_test_scaled = self.scaler.transform(x_test)

        self.model.fit(x_train_scaled, y_train)

        y_pred = self.model.predict(x_test_scaled)

        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1_score': f1_score(y_test, y_pred)
        }

        return metrics

    def predict_client(self, client_data: dict) -> tuple[int, str]:
        client_df = pd.DataFrame([client_data])
        client_scaled = self.scaler.transform(client_df)
        pred_class = self.model.predict(client_scaled)[0]

        pred_label = "Высокий риск (1)" if pred_class == 1 else "Низкий риск (0)"

        return pred_class, pred_label