from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from io import BytesIO
from services.analytics import generate_insights
from services.visuals import generate_graphs

router = APIRouter()

@router.post("/upload")
async def upload_excel(file: UploadFile = File(...)):
    if not file.filename.endswith(('.xls', '.xlsx')):
        raise HTTPException(status_code=400, detail="Arquivo deve ser .xlsx ou .xls")
    
    contents = await file.read()
    try:
        df = pd.read_excel(BytesIO(contents))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading Excel file: {str(e)}")
    
    insights = generate_insights(df)
    graphs = generate_graphs(df)
    
    return {
        "filename": file.filename,
        "insights": insights,
        "graphs": graphs
    }