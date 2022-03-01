from flask import Flask, request
import pickle
from numpy import array2string

model_path = "data/models/RandomForestClassifier_base.pkl"

with open(model_path, "rb") as file:
    unpickled_rf = pickle.load(file)

app = Flask(__name__)

@app.route("/score", methods=["GET"])
def predict_species():
    features = ["petal_length", "petal_width","sepal_length","sepal_width"]
    flower = [ request.args.get(feat) for feat in features]
    return array2string(unpickled_rf.predict([flower]))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5001)