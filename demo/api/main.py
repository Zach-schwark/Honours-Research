import sys
sys.path.insert(0,"../../research")
from pgmpy.readwrite import XMLBIFReader
from Models import BICBayesianNetwork
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

## Set up logging
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)
#
# Enable CORS
#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=["*"],
#    allow_credentials=False,
#    allow_methods=["*"],
#    allow_headers=["*"],
#)


def load_model():
    reader = XMLBIFReader("public/BIC_saved_model.xml")
    model = reader.get_model()

    BIC_BN = BICBayesianNetwork(model = model)
    
    return BIC_BN

class PredictionInput(BaseModel):
    # define your input schema here
    variables: dict = {'term': '_36_months', 'installment': '_5_898_435_665_', 'loan_amnt': '_961_0_10750_0_', 'int_rate': '_5_284_11_73_'}

@app.post("/predict")
async def predict(input_data: PredictionInput):
    BIC_BN = load_model()
    try:
        print("in backend predict endpoint")
        prediction = BIC_BN.inference("assignment", mode="single", evidence=input_data.variables)
        print(prediction[0])
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
#    
@app.get("/")
async def root():
    return {"message": "Backend is working"}   
    
    
@app.get("/test")
async def test():
    return {"message": "Backend is working!"}
