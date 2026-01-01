# 🐱🐶 Cat vs Dog Classifier Web App

A responsive web application built with **Streamlit** that uses a **Convolutional Neural Network (CNN)** to classify images of cats and dogs. The app supports both image upload and camera input, displays prediction confidence, and allows downloading a prediction report.

---

## **Features**

- ✅ Upload images or capture using a camera 📸  
- ✅ Predict Cat or Dog with a CNN  
- ✅ Display confidence as percentage  
- ✅ Color-coded confidence levels (High/Medium/Low)  
- ✅ Downloadable prediction report 📦  
- ✅ Mobile-friendly and responsive layout  
- ✅ Loading spinner during prediction  
- ✅ Error handling for invalid inputs  

---

## **Project Structure**

project/
│── app.py # Main Streamlit app
│── cat_dog_cnn.h5 # Trained CNN model
│── requirements.txt # Python dependencies
│── README.md # This file


---

## **Installation**

1. Clone the repository:

```bash
git clone git@github.com:D10sanp/Explainable-Cat-vs-Dog-Image-Classification-Using-CNN.git
cd Explainable-Cat-vs-Dog-Image-Classification-Using-CNN

pip install -r requirements.txt

Running the App Locally
streamlit run app.py
