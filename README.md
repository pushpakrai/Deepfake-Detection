
# Deepfake Detection System

A production-ready **Deepfake Detection Web Application** built using **Flask** and **Deep Learning** techniques.  
The system analyzes uploaded media and predicts whether the content is **Real** or **Deepfake** using a trained neural network model.

This project demonstrates the practical application of **computer vision**, **machine learning**, and **web development** to address the growing challenge of digital media manipulation.

---

## 📌 Key Features

- Flask-based web application
- Deep learning model for deepfake detection
- Image preprocessing using OpenCV and Pillow
- Model inference using TensorFlow
- Clean and modular project structure
- Result visualization
- Database integration using Flask-SQLAlchemy
- Scalable and extensible design

---

## 🏗️ System Architecture

1. User uploads image/video via web interface  
2. Media preprocessing and feature extraction  
3. Deep learning model inference  
4. Prediction result displayed on UI  

---

## 🗂️ Project Structure

```

Deepfake-Detection/
│
├── app.py                     # Flask application entry point
├── convert.py                 # Media preprocessing utilities
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── LICENSE
│
├── static/                    # CSS, JS, uploaded media
├── templates/                 # HTML templates
├── utils/                     # ML model & helper functions
├── instance/                  # Configuration files
└── .git/                      # Git version control

````

---

## 🛠️ Technologies & Tools

| Category | Technologies |
|--------|-------------|
| Language | Python |
| Backend | Flask |
| ML Framework | TensorFlow |
| Image Processing | OpenCV, Pillow |
| Data Science | NumPy, SciPy, Scikit-learn |
| Visualization | Matplotlib |
| Database | Flask-SQLAlchemy |

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/pushpakrai/Deepfake-Detection.git
cd Deepfake-Detection
````

---

### Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Run the Application

```bash
python app.py
```

---

### Step 5: Access the Application

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

---

## 🧠 Model Overview

* Trained using real and manipulated media samples
* Deep neural network implemented in TensorFlow
* Input preprocessing includes resizing, normalization, and feature extraction
* Binary classification: **Real vs Deepfake**

---

## 🚀 Future Enhancements

* Support for video deepfake detection
* Improved model accuracy and robustness
* REST API integration
* Cloud deployment (AWS / GCP / Azure)
* Authentication and user management
* Performance optimization for large files

---

## 🧪 Use Cases

* Media verification platforms
* Social media content moderation
* Digital forensics
* Academic research and learning
* Cybersecurity applications

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Pushpak Rai**
GitHub: [https://github.com/pushpakrai](https://github.com/pushpakrai)

---

## ⭐ Acknowledgements

* OpenCV community
* TensorFlow team
* Flask framework contributors

````

---

# ✅ `requirements.txt`

```txt
Flask
Werkzeug
numpy
tensorflow
opencv-python
Pillow
matplotlib
scikit-learn
scipy
Flask-SQLAlchemy
```` 
