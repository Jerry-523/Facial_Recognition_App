from flask import Flask, request, jsonify
from keras.models import load_model
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)

# Load the trained model
model = load_model('model/model.h5')

def preprocess_image(image):
    image = image.resize((224, 224))  # Resize to the input size of the model
    image = np.array(image) / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        image = Image.open(io.BytesIO(file.read()))
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)
        predicted_class = np.argmax(predictions, axis=1)

        return jsonify({'predicted_class': int(predicted_class[0])}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)