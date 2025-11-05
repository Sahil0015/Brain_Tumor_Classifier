# 🧠 TumorNet — Brain Tumor Classifier

**TumorNet** is a deep learning project that uses a **Convolutional Neural Network (CNN)** to detect and classify brain MRI scans into four categories:  
`Glioma`, `Meningioma`, `No Tumor`, and `Pituitary`.

The model is trained on the publicly available **[Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)** from Kaggle.

---

## 🚀 Features

- 🩺 **Automatic tumor detection** from MRI scans  
- 🧠 **Multi-class classification**: Glioma, Meningioma, No Tumor, Pituitary  
- 💡 **User-friendly Streamlit app** for quick predictions  
- 🧩 **Trained model (.h5 / .keras)** for immediate inference  
- ⚙️ **End-to-end pipeline**: Training → Evaluation → Deployment  

---

## 🧱 Folder Structure

```
TumorNet/
│
├── venv/ # Virtual environment (excluded via .gitignore)
│
├── Training/ # Contains training images
├── Testing/ # Contains testing images
│
├── app.py # Streamlit web app for predictions
├── Brain_Tumor_Classifier.ipynb # Jupyter notebook for model training
│
├── Brain Tumors.h5 # Trained model (HDF5 format)
├── Brain Tumors.keras # Keras model format
│
├── requirements.txt # Project dependencies
├── .gitignore # Files/folders to ignore
└── README.md # Project documentation
```

---

## 🧩 Model Overview

- **Architecture:** Convolutional Neural Network (CNN)  
- **Framework:** TensorFlow / Keras  
- **Optimizer:** Adamax (lr=0.001)  
- **Loss Function:** Categorical Crossentropy  
- **Accuracy:** ~93% overall, with balanced class performance  

---

## 🧠 How It Works

1. The user uploads an MRI image through the Streamlit web interface.  
2. The app preprocesses the image (resizing to 224×224, normalizing).  
3. The CNN model (`Brain Tumors.h5`) predicts the tumor type.  
4. The app displays both the **predicted class** and **class probabilities**.

---

## 🖼️ Dataset Information

Dataset used:  
> **Brain Tumor MRI Dataset** — [Kaggle Link](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

- **Classes:** Glioma, Meningioma, Pituitary, No Tumor  
- **Images:** 5,500+ labeled MRI scans  
- **Format:** JPEG  
- **Split:** 80% training, 20% testing  

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Sahil0015/TumorNet.git
cd TumorNet
```

### 2️⃣ Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# source venv/bin/activate # On Mac/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app
```bash
streamlit run app.py
```

### 5️⃣ Open in browser
Once the server starts, open:
```
http://localhost:
```

Upload any MRI image and get instant predictions.

---

## 🧠 Training the Model

If you don't have the pre-trained model file (`Brain Tumors.h5` or `Brain Tumors.keras`), you can easily **train it from scratch** by following these steps:

1. **Download the dataset**  
   Get the dataset from Kaggle:  
   👉 [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)

2. **Prepare the dataset folders**  
   After downloading, extract the dataset and place the following folders inside your project directory:  
   ```
   Training/
   Testing/
   ```

3. **Train the model using the notebook**  
   Open and run all cells in the Jupyter notebook file:  
   ```
   Brain_Tumor_Classifier.ipynb
   ```
   This will automatically train the CNN model and save it as:
   ```
   Brain Tumors.h5
   ```
   or  
   ```
   Brain Tumors.keras
   ```

4. **Run the Streamlit app**  
   Once training is complete, you can launch the app and test the model using:
   ```bash
   streamlit run app.py
   ```

💡 *Tip:* Training may take several minutes depending on your hardware. For faster results, you can use a GPU runtime on **Google Colab**.

---

## 🧰 Technologies Used

| Category | Libraries / Tools |
|-----------|------------------|
| **Language** | Python |
| **Deep Learning** | TensorFlow, Keras |
| **Visualization** | Matplotlib, Seaborn |
| **Data Handling** | NumPy, Pandas |
| **Frontend** | Streamlit |
| **Model Persistence** | H5, Keras |

---

## 📜 .gitignore Notes

```
venv/
__pycache__/
*.h5
*.keras
*.zip
.DS_Store
.ipynb_checkpoints/
```

The large model files (`.h5`, `.keras`) can be excluded from Git if you plan to share your repo publicly — you can always re-upload them via release or Google Drive.

---

## 🧩 Results Summary

| Metric | Value |
|--------|--------|
| Accuracy | ~93% |
| Precision | 0.92 |
| Recall | 0.93 |
| F1-Score | 0.93 |
| Dataset Size | ~5500 images |

✅ The model demonstrates balanced performance across all tumor categories.

---

## ⚙️ Future Improvements

- 🔧 Add Grad-CAM for model explainability  
- 🌐 Deploy app using **Streamlit Cloud / Hugging Face Spaces**  
- 🧮 Experiment with EfficientNet / MobileNet architectures  
- 📱 Create a lightweight mobile-compatible version  

---

## ⚖️ Disclaimer

> This project is for **educational and research purposes only**.  
> It is **not a substitute for professional medical diagnosis or advice**.  
> Always consult a qualified radiologist or medical expert for clinical interpretation.

---

## 👨‍💻 Author

**Sahil Aggarwal**  
📂 [GitHub](https://github.com/Sahil0015)  
🔗 [LinkedIn](https://www.linkedin.com/in/sahil-codes/)  
📧 [sahilaggarwal1532003@gmail.com](mailto:sahilaggarwal1532003@gmail.com)

---

## 📝 License

This project is licensed under the **MIT License** — feel free to use, modify, and share with attribution.
