from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import json
import os

app = Flask(__name__)
CORS(app)

# ---------- Paths ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "plant_disease_prediction_model.h5")
CLASS_INDEX_PATH = os.path.join(BASE_DIR, "model", "class_indices.json")

# ---------- Load model ----------
model = tf.keras.models.load_model(MODEL_PATH)

# ---------- Load class indices ----------
with open(CLASS_INDEX_PATH, "r") as f:
    class_indices = json.load(f)

# ✅ FIXED mapping (key → int index, value → class name)
index_to_class = {int(k): v for k, v in class_indices.items()}

IMG_SIZE = 224

def preprocess_image(image):
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Plant Disease Prediction API running"})

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    try:
        file = request.files["file"]
        image = Image.open(file).convert("RGB")

        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)

        class_index = int(np.argmax(prediction))
        confidence = float(np.max(prediction))

        disease = index_to_class[class_index]

        return jsonify({
            "disease": disease
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
