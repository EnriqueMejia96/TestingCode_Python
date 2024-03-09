from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class MLSystem:
    def __init__(self):
        pass

    def load_data(self):
        # Simula la carga de un dataset
        data = load_iris()
        return data.data, data.target

    def preprocess_data(self, X):
        # Simula el preprocesamiento de los datos
        scaler = StandardScaler().fit(X)
        return scaler, scaler.transform(X)

    def train_model(self, X, y):
        # Simula el entrenamiento de un modelo
        model = LogisticRegression(random_state=42)
        model.fit(X, y)
        return model
    
    def evaluate_model(self, model, X, y):
        # Simula la evaluación de un modelo
        predictions = model.predict(X)
        return accuracy_score(y, predictions)

    def run_entire_workflow(self, input_data_path):
        try:
            X, y = self.load_data()
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            scaler, X_train_scaled = self.preprocess_data(X_train)
            model = self.train_model(X_train_scaled, y_train)
            X_test_scaled = scaler.transform(X_test)
            accuracy = self.evaluate_model(model, X_test_scaled, y_test)
            return {'success': True, 'accuracy': accuracy}
        except Exception as e:
            return {'success': False, 'message': str(e)}
