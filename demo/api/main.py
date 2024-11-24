import sys
sys.path.insert(0,"../../research")
from pgmpy.readwrite import XMLBIFReader
from Models import BICBayesianNetwork
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

## Set up logging
#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)
#
# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


def load_model():
    reader = XMLBIFReader("public/BIC_saved_model.xml")
    model = reader.get_model()

    BIC_BN = BICBayesianNetwork(model = model)
    
    return BIC_BN


##@app.post("/predict")
##async def predict(input_data: PredictionInput):
##    BIC_BN = load_model()
##    logger.info("Received prediction request")
##    logger.info(f"Input data: {input_data}")
##    try:
##        print("in backend predict endpoint")
##        prediction = BIC_BN.inference("assignment", mode="single", evidence=input_data.variables)
##        logger.info(f"Prediction result: {prediction}")
##        print(prediction[0])
##        return {"prediction": prediction[0]}
##    except Exception as e:
##        logger.error(f"Error during prediction: {str(e)}")
##        raise HTTPException(status_code=500, detail=str(e))
#    
@app.get("/")
async def root():
    return {"message": "Backend is working"}   
    
    
@app.get("/test")
async def test():
    return {"message": "Backend is working!"}


#from fastapi import FastAPI
#
#app = FastAPI()
#
#@app.get("/")
#async def root():
#    return {"message": "It works!"}