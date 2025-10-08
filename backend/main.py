from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import upload

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
