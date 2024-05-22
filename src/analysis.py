import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_data():
    # Ruta absoluta
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '../processed_global_education.csv')
    
    # Verificar la ruta actual y la existencia del archivo
    print("Current working directory:", os.getcwd())
    print("Using file path:", file_path)
    print("File exists:", os.path.isfile(file_path))
    
    # Cargar datos procesados
    data = pd.read_csv(file_path)
    
    # Seleccionar solo columnas numéricas para el cálculo de la matriz de correlación
    numeric_data = data.select_dtypes(include=[float, int])
    
    # Correlaciones
    corr_matrix = numeric_data.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Matriz de Correlación')
    plt.show()
    
    # Comparar ROI con otras variables
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Gross_Tertiary_Education_Enrollment', y='ROI', data=data)
    plt.title('ROI vs Matriculación Terciaria Bruta')
    plt.xlabel('Matriculación Terciaria Bruta (%)')
    plt.ylabel('ROI')
    plt.show()
    
    # Guardar el resumen del análisis
    summary = data.describe()
    summary_path = os.path.join(current_dir, '../results/summary.csv')
    summary.to_csv(summary_path)
    
if __name__ == "__main__":
    analyze_data()
