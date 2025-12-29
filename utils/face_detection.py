import cv2

# Load Haar Cascade for Face Detection
FACE_CASCADE = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def extract_faces(video_path, frame_skip=5):
    cap = cv2.VideoCapture(video_path)
    faces = []
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_skip == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detected_faces = FACE_CASCADE.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in detected_faces:
                cropped_face = frame[y:y + h, x:x + w]
                cropped_face_resized = cv2.resize(cropped_face, (224, 224))
                faces.append(cropped_face_resized)

        frame_count += 1
    cap.release()
    return faces
