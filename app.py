from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load dataset
df = pd.read_csv("data/house_price.csv")

X = df.drop("Price", axis=1)
y = df["Price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        area = float(request.form["Area"])
        bedrooms = float(request.form["Bedrooms"])
        bathrooms = float(request.form["Bathrooms"])
        stories = float(request.form["Stories"])
        parking = float(request.form["Parking"])
        age = float(request.form["Age"])
        location = float(request.form["Location"])

        # Prepare input for model
        arr = np.array([[area, bedrooms, bathrooms, stories, parking, age, location]])

        prediction = model.predict(arr)[0]

        return render_template(
            "index.html",
            prediction_text=f"Predicted House Price: Rs. {int(prediction):,}"
        )

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")



if __name__ == "__main__":
    app.run(debug=True)
