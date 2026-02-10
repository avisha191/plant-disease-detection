# 🌿 Plant Disease Detection System

A full-stack machine learning web application that detects plant diseases from leaf images using a trained Convolutional Neural Network (CNN).

This project allows users to upload an image of a plant leaf and receive the predicted disease through a clean web interface.

---

## 🚀 Features

- Image-based plant disease detection
- CNN model trained on the PlantVillage dataset
- Flask REST API backend
- Clean, modern frontend (HTML, CSS, JavaScript)
- Modular and scalable project structure
- Model hosted externally (industry best practice)

---

## 🛠️ Tech Stack

### Machine Learning
- TensorFlow / Keras
- Convolutional Neural Network (CNN)

### Backend
- Python
- Flask
- Flask-CORS
- NumPy
- Pillow

### Frontend
- HTML
- CSS
- JavaScript

---

## 📁 Project Structure

```text
plant_disease_app/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── model/
│       └── class_indices.json
│
├── frontend/
│   ├── index.html
│   ├── about.html
│   ├── how-it-works.html
│   ├── future.html
│   ├── css/
│   └── js/
│
├── .gitignore
└── README.md

⚠️ The trained model file is intentionally **not included** in this repository due to GitHub size limits.

---

## 🧠 How the System Works

1. User uploads a leaf image via the frontend
2. The image is sent to the Flask backend
3. The backend preprocesses the image
4. The CNN model performs prediction
5. The predicted disease label is returned and displayed

---

## ⬇️ Model Download (IMPORTANT)

The trained CNN model file is **hosted externally** due to GitHub’s file size limitations.

### 🔗 Download the model from Google Drive:
👉 https://drive.google.com/file/d/1c9X4EXQTxCCeNRp7N2pCqqgzfUvztWCM/view?usp=sharing

After downloading, place the model file here:

backend/model/plant_disease_prediction_model.h5


> ⚠️ The application will not run without this file.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/avisha191/plant-disease-detection.git
cd plant-disease-detection
2️⃣ Set up the backend
cd backend
pip install -r requirements.txt
python app.py
You should see:

Running on http://127.0.0.1:5000
3️⃣ Run the frontend
Open this file in your browser:

frontend/index.html
Upload a leaf image and click Predict Disease.

🧪 Notes
Confidence scores are intentionally hidden to avoid misleading interpretations

Predictions may vary due to inter-crop visual similarities

This project demonstrates a single-head multi-class CNN

🔮 Future Enhancements
Crop-specific disease models

Treatment and remedy suggestions

Mobile application

Deployment on cloud (Render / AWS)

📌 Why the Model Is Not in GitHub
GitHub has a 100 MB per-file limit.
In real-world ML systems, trained models are treated as artifacts, not source code.

Hosting models externally and documenting download steps is an industry standard practice.

