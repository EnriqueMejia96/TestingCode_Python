from sklearn.datasets import load_iris
import pandas as pd

def process_iris_data():
    # Cargar los datos de Iris
    iris = load_iris()
    data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    data['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
   
    # Calcular la media de cada característica por especie
    mean_values = data.groupby('species').mean()
    return mean_values