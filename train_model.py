import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load Dataset
df = pd.read_csv("train.csv")

# Select Features
X = df[['GrLivArea', 'BedroomAbvGr', 'FullBath']]
y = df['SalePrice']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Save Model
with open("house_price_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model Trained Successfully!")
print("house_price_model.pkl created.")