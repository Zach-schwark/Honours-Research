import sys
import pandas as pd
sys.path.insert(0,"../../research")
from pgmpy.readwrite import XMLBIFReader
from Models import BICBayesianNetwork
from data_preprocessing.DataPreprocessing import DataPreprocessing

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # SvelteKit dev server
        "https://honours-research-ebk6.vercel.app",  # Production URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


reader = XMLBIFReader("models/BIC_saved_model.xml")
model = reader.get_model()

BIC_BN = BICBayesianNetwork(model = model)

class PredictionInput(BaseModel):
    # define your input schema here
    variables: dict = {'term': '_36_months', 'installment': '_5_898_435_665_', 'loan_amnt': '_961_0_10750_0_', 'int_rate': '_5_284_11_73_'}


@app.post("/predict",  strict_slashes=False)
async def predict(input_data: PredictionInput):
    try:
        prediction = BIC_BN.inference("assignment", mode="single", evidence=input_data.variables)
        print(prediction[0])
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
# Health check endpoint
@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}