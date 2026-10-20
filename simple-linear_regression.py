import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create dataset
data = {
    'Experience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary': [25000, 28000, 32000, 36000, 40000,
               45000, 50000, 55000, 60000, 65000]
}

df = pd.DataFrame(data)

# Independent and dependent variables
X = df[['Experience']]
y = df['Salary']

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict salary
y_pred = model.predict(X)

# Display slope and intercept
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict salary for 7 years of experience
experience = [[7]]
predicted_salary = model.predict(experience)

print("Predicted salary for 7 years of experience:",
      predicted_salary[0])

# Display actual and predicted values
print("\nActual Salary:")
print(y.values)

print("\nPredicted Salary:")
print(y_pred)

# Plot regression line
plt.scatter(X, y)
plt.plot(X, y_pred)

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Simple Linear Regression")

plt.show()