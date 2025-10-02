from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from io import BytesIO
from services.analytics import generate_insights
from services.visuals import generate_graphs

app = FastAPI(
    title="Insightly API",
    description="API para processar arquivos Excel e gerar insights e gráficos.",
    version="1.0.0"
)

# Configuração do CORS(permite acesso do frontend react)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens (ajuste conforme necessário)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
