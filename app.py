from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load Model
model = pickle.load(open("house_price_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    sqft = float(request.form["sqft"])
    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])

    data = pd.DataFrame({
        "GrLivArea": [sqft],
        "BedroomAbvGr": [bedrooms],
        "FullBath": [bathrooms]
    })

    prediction = model.predict(data)[0]

    return render_template(
        "index.html",
        prediction=f"${prediction:,.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)