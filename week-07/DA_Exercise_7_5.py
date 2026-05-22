# Import pandas for working with tables and datasets
import pandas as pd

# Import numpy for numerical operations
import numpy as np

# Import matplotlib for charts and graphs
import matplotlib.pyplot as plt

# Import train_test_split to divide data into training and testing sets
from sklearn.model_selection import train_test_split

# Import the Linear Regression model
from sklearn.linear_model import LinearRegression

# Import metrics for evaluating the model
from sklearn import metrics


# Load the housing.csv dataset into a DataFrame named boston
boston = pd.read_csv('housing.csv')

# Display the first 5 rows of the dataset
print(boston.head())

# Display the number of rows and columns
print(boston.shape)

# Display the data types of each column
print(boston.dtypes)

# Check for missing values in each column
print(boston.isnull().sum())


# Remove the MEDV column from the dataset and store remaining columns in X
# X contains the input features used for prediction
X = boston.drop('MEDV', axis=1)

# Store the MEDV column in y
# y is the target variable we want to predict
y = boston['MEDV']


# Split the data into training and testing sets
# 80% is used for training
# 20% is used for testing
# random_state=42 keeps the split consistent each time
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create a Linear Regression model
model = LinearRegression()


# Train the model using the training data
# The model learns patterns between X and y
model.fit(X_train, y_train)


# Print the intercept value of the regression model
print("Intercept:", model.intercept_)

# Print the coefficients for each feature
print("Coefficients:", model.coef_)


# Use the trained model to make predictions on the test data
y_pred = model.predict(X_test)


# Display the actual values from the test set
print("Actual values:")
print(list(y_test))

# Display the predicted values from the model
print("Predicted values:")
print(list(y_pred.round(2)))


# Calculate the R² score using the model
# This shows how well the model fits the data
r2_score = model.score(X_test, y_test)

# Print the R² score
print("R² Score:", round(r2_score, 4))


# Calculate Mean Absolute Error
# Shows the average prediction error
mae = metrics.mean_absolute_error(y_test, y_pred)

# Calculate Mean Squared Error
# Larger errors are penalized more heavily
mse = metrics.mean_squared_error(y_test, y_pred)

# Calculate R² again using sklearn metrics
r2 = metrics.r2_score(y_test, y_pred)


# Print evaluation metrics
print("MAE:", round(mae, 4))
print("MSE:", round(mse, 4))
print("R²:", round(r2, 4))


# Create a scatter plot of actual test values vs predicted values
plt.scatter(
    y_test,
    y_pred,
    color='steelblue',
    alpha=0.7
)

# Create a red diagonal line for perfect predictions
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r-',
    lw=2
)

# Label the x-axis
plt.xlabel('Actual Prices ($1,000s)')

# Label the y-axis
plt.ylabel('Predicted Prices ($1,000s)')

# Add a title to the graph
plt.title('Boston Housing — Actual vs Predicted Prices')

# Display the chart
plt.show()