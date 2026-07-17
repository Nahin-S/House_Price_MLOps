from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


housing = fetch_california_housing(as_frame = True)

X = housing.data
y = housing.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

model = RandomForestRegressor()

model.fit(X_train, y_train)
score = model.score(X_test,y_test)

print(f'R2 score : {score :.4f}')