from flask import Flask, request, jsonify
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

app = Flask(__name__)

# Create a dummy model for demonstration purposes
def create_model():
    model = Sequential([
        Dense(10, activation='relu', input_shape=(10000,)),  # Adjust the input shape based on your actual data
        Dense(10, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy')
    return model

model = create_model()

def prepare_image(file):
    # Convert the image file to an array, then resize and flatten it
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (100, 100))  # Resize to 100x100 as an example
    return image.flatten().reshape(1, -1)  # Flatten and add batch dimension

def compare_signatures(image1, image2):
    # Prepare images
    img1 = prepare_image(image1)
    img2 = prepare_image(image2)
    # Stack images or concatenate features depending on your model's design
    combined_features = np.hstack((img1, img2))
    # Predict similarity
    similarity = model.predict(combined_features)[0]
    return similarity[0]

@app.route('/sign/match', methods=['POST'])
def match_signatures():
    file1 = request.files['image1']
    file2 = request.files['image2']
    if not file1 or not file2:
        return jsonify({'error': 'Missing images'}), 400
    similarity = compare_signatures(file1, file2)
    return jsonify({'similarity': float(similarity)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)