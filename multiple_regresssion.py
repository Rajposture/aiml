
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# 1. Load the dataset
data = fetch_california_housing(as_frame=True).frame

print("First five rows:")
print(data.head())

print("\nMissing values:", data.isnull().sum().sum())

# 2. Separate input and output
X = data.drop("MedHouseVal", axis=1)
y = data["MedHouseVal"]

# 3. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))

# 4. Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# 5. Predict house prices
y_pred = model.predict(X_test)

# 6. Evaluate the model
print("\nR2 Score:", round(r2_score(y_test, y_pred), 3))
print("MAE:", round(mean_absolute_error(y_test, y_pred), 3))
print("MSE:", round(mean_squared_error(y_test, y_pred), 3))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, y_pred)), 3))

# 7. Compare 10 actual and predicted prices
result = pd.DataFrame({
    "Actual Price": y_test.values[:10] * 100000,
    "Predicted Price": y_pred[:10] * 100000
})

print("\nActual vs Predicted Prices:")
print(result.round(2))

# 8. Draw a simple line graph
plt.plot(y_test.values[:10] * 100000, marker="o", label="Actual")
plt.plot(y_pred[:10] * 100000, marker="o", label="Predicted")

plt.xlabel("House Number")
plt.ylabel("Price in Dollars")
plt.title("Actual vs Predicted House Prices")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 9. Predict the price of a new house
new_house = pd.DataFrame(
    [[5.0, 20, 6.0, 1.0, 1500, 3.0, 34.0, -118.3]],
    columns=X.columns
)

price = model.predict(new_house)

print("\nPredicted price of new house:")
print("$", round(price[0] * 100000, 2))
