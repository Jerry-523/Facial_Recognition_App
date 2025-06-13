# Facial Recognition App

This project is a facial recognition application that utilizes a convolutional neural network (CNN) to identify individuals based on images. The application consists of a backend built with Flask and a frontend that allows users to upload images for recognition.

## Project Structure

```
facial-recognition-app
├── dataset
│   ├── raw              # Original images of students and other individuals
│   └── augmented        # Images that have undergone data augmentation
├── model
│   ├── train.py         # Code to define and train the CNN
│   ├── model.h5         # Saved model after training
│   └── utils.py         # Utility functions for model training
├── backend
│   ├── app.py           # Main entry point for the Flask backend
│   ├── requirements.txt  # Dependencies for the backend application
│   └── utils.py         # Utility functions for the backend
├── frontend
│   ├── index.html       # Main HTML file for the frontend
│   ├── app.js           # JavaScript code for handling image uploads
│   └── styles.css       # CSS styles for the frontend
└── README.md            # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd facial-recognition-app
   ```

2. **Install backend dependencies**:
   Navigate to the `backend` directory and install the required packages:
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. **Prepare the dataset**:
   Place the original images in the `dataset/raw` directory. The data augmentation process will generate images in the `dataset/augmented` directory.

4. **Train the model**:
   Run the training script to train the CNN and save the model:
   ```
   cd ../model
   python train.py
   ```

5. **Run the backend**:
   Start the Flask application:
   ```
   cd ../backend
   python app.py
   ```

6. **Access the frontend**:
   Open `frontend/index.html` in a web browser to use the application.

## Usage

- Upload an image using the form in the frontend.
- The image will be sent to the backend for processing.
- The backend will normalize the image, make a prediction using the trained model, and return the results to the frontend for display.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License.