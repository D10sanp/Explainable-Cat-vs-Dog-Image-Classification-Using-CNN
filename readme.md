# 🐱🐶 Cat vs Dog Classifier Web App

A responsive web application built with **Streamlit** that uses a **Convolutional Neural Network (CNN)** to classify images of cats and dogs. This app is mobile-friendly, supports camera input, and includes features like **confidence display**, **downloadable prediction reports**, and (optional) **Grad-CAM visualization**.

---

## **Features**

- ✅ Upload images or capture using mobile camera 📸  
- ✅ Predict Cat or Dog with CNN  
- ✅ Display confidence as percentage  
- ✅ Color-coded confidence (High / Medium / Low)  
- ✅ Grad-CAM visualization (optional) 🖼️  
- ✅ Downloadable prediction report 📦  
- ✅ Mobile-friendly layout (responsive)  
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
git clone <your-repo-url>
cd project

pip install -r requirements.txt

## **Run the app locally**

streamlit run app.py