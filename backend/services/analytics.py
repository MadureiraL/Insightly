import pandas as pd


def generate_insights(df: pd.DataFrame) -> dict:
    insights = {}

    # Total de linhas e colunas
    insights['num_rows'] = len(df)
    insights['num_columns'] = len(df.columns)

    # Médias das colunas numéricas
    insights["medias"] = df.mean(numeric_only=True).round(2).to_dict()

    # Colunas com maior variabilidade (desvio padrão)
    stds = df.std(numeric_only=True).sort_values(ascending=False)
    insights["variabilidade"] = stds.head(3).round(2).to_dict()

    # Tendência temporais (se houver coluna de data)
    data_cols = [col for col in df.columns if 'date' in col.lower()
                                                                  or 'data' in col.lower()]
    if data_cols:
        df[data_cols[0]] = pd.to_datetime(df[data_cols[0]], errors='coerce')
        df["ano"] = df[data_cols[0]].dt.year
        insights["tendencia_anual"] = df.groupby("ano").value_counts().sort_index.to_dict()
 
    
    #Colunas com mais valores ausentes
    missing_values = df.isnull().sum()
    insights["valores_ausentes"] = missing_values[missing_values > 0].sort_values(ascending=False).to_dict()

    return insights