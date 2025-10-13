import pandas as pd
import plotly.express as px

def generate_insights(df: pd.DataFrame) -> dict:
    insights = {}
    
    # Exemplo de insight: Estatísticas descritivas
    insights['summary_statistics'] = df.describe().to_dict()
    
    # Exemplo de insight: Contagem de valores nulos
    insights['null_values'] = df.isnull().sum().to_dict()
    
    return insights
