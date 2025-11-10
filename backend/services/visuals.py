import pandas as pd
import plotly.express as px
import plotly.io as pio
import os
from config import EXPORT_DIR # precisa consertar 

def generate_graphs(df: pd.DataFrame) -> dict:
    graphs = {}

    # 🔹 1. Gráfico de barras das médias
    numeric_cols = df.select_dtypes(include="number").columns
    if len(numeric_cols) > 0:
        mean_values = df[numeric_cols].mean()
        fig_bar = px.bar(
            x=mean_values.index,
            y=mean_values.values,
            title="Médias das colunas numéricas"
        )
        graphs["bar_means"] = fig_bar.to_json()

    # 🔹 2. Gráfico de linha (se houver coluna de data)
    date_cols = [col for col in df.columns if "data" in col.lower()]
    if date_cols:
        df[date_cols[0]] = pd.to_datetime(df[date_cols[0]], errors="coerce")
        df_sorted = df.sort_values(by=date_cols[0])
        fig_line = px.line(
            df_sorted,
            x=date_cols[0],
            y=numeric_cols[0] if len(numeric_cols) > 0 else None,
            title=f"Tendência temporal ({numeric_cols[0]})"
        )
        graphs["line_trend"] = fig_line.to_json()

    # 🔹 3. Gráfico de pizza (categorias)
    cat_cols = df.select_dtypes(include="object").columns
    if len(cat_cols) > 0:
        top_cat = cat_cols[0]
        fig_pie = px.pie(
            df,
            names=top_cat,
            title=f"Distribuição por {top_cat}"
        )
        graphs["pie_distribution"] = fig_pie.to_json()

    return graphs

def save_image(fig, filename: str) -> str:
    filepath = os.path.join(EXPORT_DIR, filename)
    pio.write_image(fig, filepath, format='png', scale=2)
    return filepath