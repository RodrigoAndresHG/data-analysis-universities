import pandas as pd
import os

def clean_data():
    # Ruta absoluta
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '../Global_Education.csv')  # Ruta actualizada
    
    # Verificar la ruta actual y la existencia del archivo
    print("Current working directory:", os.getcwd())
    print("Using file path:", file_path)
    print("File exists:", os.path.isfile(file_path))
    
    # Cargar datos
    data = pd.read_csv(file_path, encoding='latin1')
    
    # Manejo de valores nulos
    data.fillna(0, inplace=True)
    
    # Crear variable de ROI (simplificada para el ejemplo)
    data['ROI'] = (data['Youth_15_24_Literacy_Rate_Male'] + data['Youth_15_24_Literacy_Rate_Female']) / 2
    
    # Guardar datos procesados
    processed_path = os.path.join(current_dir, '../data/processed/processed_global_education.csv')
    data.to_csv(processed_path, index=False)
    
if __name__ == "__main__":
    clean_data()
