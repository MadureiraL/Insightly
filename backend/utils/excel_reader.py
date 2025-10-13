from routers import upload
import pandas as pd

# Verifica se o arquivo é Excel


def validate_extension(file: str):
    if not file.filename.endswith(('.xls', '.xlsx')):
        raise ValueError(
            status_code=400, detail="Arquivo deve ser .xlsx ou .xls")

# Verifica o tamanho do arquivo (limite de 5MB)


def validate_size(size: int, max_mb: int = 5):
    if size > max_mb * 1024 * 1024:
        raise ValueError(
            status_code=400, detail="Arquivo muito grande. Limite de 5MB.")

def validate_dataframe(df: pd.DataFrame):
    if df.empty:
        raise ValueError(
            status_code=400, detail="O arquivo Excel está vazio.")
    if df.shape[0] < 2:
        raise ValueError(
            status_code=400, detail="O arquivo Excel deve ter pelo menos 2 linhas de dados.")
    if df.shape[1] < 2:
        raise ValueError(
            status_code=400, detail="O arquivo Excel deve ter pelo menos 2 colunas de dados.") 
       