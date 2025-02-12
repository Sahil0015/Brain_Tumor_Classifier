import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
MODEL_PATH = "Brain Tumors.h5"
model = tf.keras.models.load_model(MODEL_PATH, compile=False)
model.compile(optimizer=tf.keras.optimizers.Adamax(learning_rate=0.001), 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Define class labels
class_labels = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

# Streamlit UI
st.title("Brain Tumor Classification Web-Page")
st.write("Upload an MRI image to classify the type of brain tumor.")

# Upload file
uploaded_file = st.file_uploader("Choose an image...")

if uploaded_file is not None:
    # Load and preprocess the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    img = image.resize((224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Make prediction
    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions)
    predicted_class = class_labels[predicted_index]
    
    # Display prediction
    st.subheader(f"Predicted Class: {predicted_class}")
    st.write("Prediction Probabilities:")
    for i, label in enumerate(class_labels):
        st.write(f"{label}: {predictions[0][i]:.4f}")