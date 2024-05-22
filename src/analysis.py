import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_data():
    # Cargar datos procesados
    data = pd.read_csv('../data/processed/processed_global_education.csv')
    
    # Correlaciones
    corr_matrix = data.corr()
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
    summary.to_csv('../results/summary.csv')
    
if __name__ == "__main__":
    analyze_data()

