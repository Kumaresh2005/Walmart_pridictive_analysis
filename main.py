# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("Walmart_Sales.csv")

# Show first 5 rows
print("First 5 Rows:")
print(data.head())

# Select input features
X = data[['Temperature', 'Fuel_Price', 'CPI', 'Unemployment', 'Holiday_Flag']]

# Target column
y = data['Weekly_Sales']

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict sales
predictions = model.predict(X_test)

# Show some predictions
print("\nPredicted Sales:")
print(predictions[:5])

# Model accuracy
r2 = r2_score(y_test, predictions)
print("\nModel Accuracy (R2 Score):", r2)

# Error
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", mae)

# Graph
plt.figure(figsize=(10,5))

# Actual values
plt.plot(y_test.values[:50], label='Actual Sales')

# Predicted values
plt.plot(predictions[:50], label='Predicted Sales')

plt.title("Actual vs Predicted Weekly Sales")
plt.xlabel("Data Points")
plt.ylabel("Sales")

plt.legend()

plt.show()