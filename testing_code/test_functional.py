import unittest
from iris_processor import process_iris_data
class TestIrisDataProcessor(unittest.TestCase):
    def test_process_iris_data(self):
        # Ejecutar la función de procesamiento
        result = process_iris_data()
        # Verificar las columnas y filas esperadas
        self.assertEqual(list(result.columns), ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
        self.assertEqual(len(result), 3)  # Debe haber 3 filas       
        # Verificar que los valores medios no sean nulos
        for column in result.columns:
            self.assertFalse(result[column].isnull().any())

if __name__ == '__main__':
    unittest.main()