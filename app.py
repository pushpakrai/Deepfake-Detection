from flask import Flask, request, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import base64
from utils.face_detection import extract_faces
from utils.prediction import predict_multiple_frames
from utils.visualization import visualize_predictions, image_to_base64
import cv2

# Initialize Flask App
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database for user management
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Endpoint for User Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username already exists
        if User.query.filter_by(username=username).first():
            return "Username already exists. Please choose a different one."

        # Hash the password using the default method
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# Endpoint for User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('upload_and_detect'))
        return "Invalid credentials"
    return render_template('login.html')

# Function to extract frames from the video
def extract_frames(video_path, frame_skip=5):
    """Extract frames from the video at specified intervals."""
    frames = []
    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_skip == 0:
            frames.append(frame)
        frame_count += 1

    cap.release()
    return frames

# Endpoint to Handle File Upload
@app.route('/upload', methods=['GET', 'POST'])
def upload_and_detect():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        file = request.files['video']
        if file.filename == '':
            return "No selected file."

        # Save Uploaded Video
        video_path = os.path.join("uploads", file.filename)
        file.save(video_path)

        # Extract Faces
        faces = extract_faces(video_path, frame_skip=5)
        if not faces:
            return "No faces detected in the video."

        face_images_base64 = [image_to_base64(face) for face in faces]

        # Extract Frames
        frames = extract_frames(video_path, frame_skip=5)
        frame_images_base64 = [image_to_base64(frame) for frame in frames]

        # Predict Consistency and Accuracy
        consistency, avg_confidence, confidences = predict_multiple_frames(faces)

        # Visualize Predictions
        plot_path = visualize_predictions(confidences)
        with open(plot_path, "rb") as f:
            plot_base64 = base64.b64encode(f.read()).decode('utf-8')

        return render_template('result.html',
                               faces=face_images_base64,
                               frames=frame_images_base64,  # Pass the frames to the template
                               result=consistency,
                               accuracy=f"{avg_confidence * 100:.2f}",
                               avg_confidence=f"{avg_confidence:.2f}",
                               plot=plot_base64)

    return render_template('upload.html')

# Endpoint for User Logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)