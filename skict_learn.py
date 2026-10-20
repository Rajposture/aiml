
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Create sample data
X = [[1], [2], [3], [4], [5], [6]]
y = [10, 20, 30, 40, 50, 60]

# 2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=1
)

# 3. Create the model
model = LinearRegression()

# 4. Train the model
model.fit(X_train, y_train)

# 5. Predict the output
y_pred = model.predict(X_test)
print("Predicted values:", y_pred)

# 6. Calculate evaluation measures
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# 7. Predict for a new input
print("Prediction for 7:", model.predict([[7]])[0])
