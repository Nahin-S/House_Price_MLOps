from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import mlflow
import mlflow.sklearn 
housing = fetch_california_housing(as_frame = True)
mlflow.sklearn.autolog()

X = housing.data
y = housing.target
estimators = 30
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)
with mlflow.start_run():
    model = RandomForestRegressor(
        n_estimators = estimators,
        max_depth = 20
    )

    model.fit(X_train, y_train)
    score = model.score(X_test,y_test)
    
    print(f'R2 score : {score :.4f}')