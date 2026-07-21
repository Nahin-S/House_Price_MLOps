import mlflow
import pandas as pd

# Load the latest version of the registered model
model = mlflow.pyfunc.load_model(
    "models:/RandomForestHousePrice/latest"
)


# Sample input (same features as California Housing dataset)
sample = pd.DataFrame({
    "MedInc": [8.3252],
    "HouseAge": [41],
    "AveRooms": [6.9841],
    "AveBedrms": [1.0238],
    "Population": [322],
    "AveOccup": [2.5556],
    "Latitude": [37.88],
    "Longitude": [-122.23]
})

prediction = model.predict(sample)

print("Predicted House Price:", prediction)





