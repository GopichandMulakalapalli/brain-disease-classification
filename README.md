# MRI-Based Brain Disease Classification

A deep learning project that classifies uploaded brain images into three model output categories: **Haemorrhagic**, **Ischemic**, and **Normal**. The application uses a trained TensorFlow/Keras model and provides a simple interface for uploading an image and viewing the predicted category.

> **Important medical disclaimer:** This project is for educational and demonstration purposes only. It is not a medical diagnostic tool. Do not use its predictions to make healthcare decisions.

## Features

- Upload an image from your local computer.
- Preprocess the image before prediction.
- Display the model's predicted category.
- Show informational text about the predicted category.
- Includes a Jupyter notebook for model development/experimentation.

## Technology

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Streamlit
- Jupyter Notebook

## Repository files

- `predictions.py` — Streamlit application.
- `Brain_tumor_detection.ipynb` — notebook for model development.
- `model.h5` — trained model file (provide separately if it is not included in this repository).
- `requirements.txt` — Python dependencies.
- `screenshots/` — screenshots of the application (optional).

## How it works

1. The user uploads a JPG, JPEG, or PNG image.
2. The app resizes the image to 200 × 200 pixels.
3. The trained model generates output scores.
4. The app selects the class with the highest score from `Haemorrhagic`, `Ischemic`, and `Normal`.
5. The predicted category is shown in the interface.

## Setup

Use Python 3.11 if that matches your model's environment.

### 1. Clone the repository

```bash
git clone https://github.com/GopichandMulakalapalli/brain-disease-classification.git
cd brain-disease-classification
```

### 2. Create and activate a virtual environment (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Add the trained model

The application loads `model.h5` from the same directory as `predictions.py`. Place the model file there before running the application.

GitHub blocks ordinary Git files larger than 100 MB. If your model file is larger than this, use Git LFS or host the model elsewhere and document how to download it. Do not commit a large model through the normal web uploader.

### 5. Run the app

```powershell
python -m streamlit run predictions.py
```

Open the local URL printed in the terminal.

## Screenshots

Add screenshots of the upload screen and prediction results to a folder named `screenshots`, then link them here. For example:

```markdown
![Upload screen](screenshots/upload-screen.png)
![Haemorrhagic result](screenshots/haemorrhagic-result.png)
![Ischemic result](screenshots/ischemic-result.png)
```

## Limitations

- The prediction is only as reliable as the training data and model evaluation.
- The current app chooses the class with the highest model output; it does not display a calibrated probability.
- The app's output should not be interpreted as a confirmed diagnosis.
- Confirm the model architecture and evaluation metrics from the notebook before describing them as ResNet50 or reporting performance figures.

## Author

Gopichand Mulakalapalli

GitHub: https://github.com/GopichandMulakalapalli
