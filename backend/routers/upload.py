from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO
from services.analytics import generate_insights
from services.visuals import generate_graphs
from utils.excel_reader import validate_extension, validate_size, validate_dataframe

router = APIRouter()

@router.post("/upload")
async def validate_extension(file: UploadFile = File(...)):

    try:
        validate_extension(file.filename)
        validate_size(file)

        contents = await file.read()
        df = pd.read_excel(BytesIO(contents))
        validate_dataframe(df)

        insights = generate_insights(df)
        graphs = generate_graphs(df)

        return {
            "filename": file.filename,
            "insights": insights,
            "graphs": graphs
        }

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erro ao processar o arquivo: {str(e)}")
