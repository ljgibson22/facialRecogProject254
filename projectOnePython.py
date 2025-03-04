import cv2
import numpy as np
import tensorflow as tf
import serial
import time

# Initialize serial communication with Arduino
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # Give Arduino time to get ready

# Load the google teachable machine model
model_path = "C:/Users/ljgib/Downloads/completeConverted_keras/keras_model.h5"
model = tf.keras.models.load_model(model_path, compile=False)

# Load and edit OpenCV video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 10)  # Reduce FPS for faster processing

def preprocess_frame(frame):
    img = cv2.resize(frame, (224, 224))  # Resize
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = img.astype(np.float32) / 255.0  # Normalize pixel values
    return img

prev_class = None  # Store the previous class
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, (320, 240))  # Reduce resolution for faster processing
    processed_frame = preprocess_frame(frame)
    predictions = model.predict(processed_frame)

    class_index = np.argmax(predictions)
    confidence = np.max(predictions)

    if class_index == 0 or confidence < 0.7:
        if prev_class != "R":
            print(f"Unrecognized! Class: {class_index} Confidence: {confidence:.2f}")
            if arduino and arduino.is_open:
                arduino.write(b'R')  # Send "R" for red buzzer
    else:
        if prev_class != "B":
            print(f"Recognized! Class: {class_index} Confidence: {confidence:.2f}")
            if arduino and arduino.is_open:
                arduino.write(b'B')  # Send "B" for blue buzzer


    # Display video capture
    cv2.imshow("Face Recognition", frame)
    
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
arduino.close()