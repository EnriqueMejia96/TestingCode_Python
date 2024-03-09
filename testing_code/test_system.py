import unittest
from system import MLSystem

class TestMLSystem(unittest.TestCase):
    def test_entire_workflow(self):
        # Inicializa el sistema de ML
        system = MLSystem()
        # Ejecuta el flujo de trabajo completo y obtiene el resultado
        result = system.run_entire_workflow(None)  

        # Verifica que el flujo de trabajo se haya completado con éxito
        self.assertTrue(result['success'], "The ML system workflow should have completed successfully.")

        # Verifica que la precisión del modelo sea razonable
        # Nota: el umbral específico depende del caso de uso y expectativas
        self.assertGreater(result['accuracy'], 0.7, "The model accuracy should be above 0.7.")

if __name__ == '__main__':
    unittest.main()