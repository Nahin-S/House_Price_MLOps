from fastapi import FastAPI
from pydantic import BaseModel
import joblib


app = FastAPI()


# Load trained model
model = joblib.load("model.joblib")


class HouseData(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


@app.get("/")
def home():
    return {"message": "House Price API is running"}


@app.post("/predict")
def predict(data: HouseData):

    input_data = [[
        data.MedInc,
        data.HouseAge,
        data.AveRooms,
        data.AveBedrms,
        data.Population,
        data.AveOccup,
        data.Latitude,
        data.Longitude
    ]]

    prediction = model.predict(input_data)

    return {
        "predicted_price": prediction[0]
    }