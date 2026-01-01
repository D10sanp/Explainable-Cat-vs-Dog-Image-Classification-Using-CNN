import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, UnidentifiedImageError

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Cat vs Dog Classifier",
    page_icon="🐱",
    layout="wide"
)

# ================= LOAD MODEL =================
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("cat_dog_cnn.h5")

try:
    model = load_model()
except Exception:
    st.error("❌ Model could not be loaded.")
    st.stop()

# ================= CLASS LABELS =================
class_labels = {0: "Cat 🐱", 1: "Dog 🐶"}

# ================= TITLE =================
st.title("🐱 Cat vs 🐶 Dog Classifier")
st.write("Upload or capture an image, then click **Check Image**.")

# ================= LAYOUT =================
left_col, right_col = st.columns(2)

# ================= LEFT COLUMN =================
with left_col:
    st.subheader("📤 Image Input")
    input_method = st.radio(
        "Choose input method:",
        ["Upload Image", "Use Camera 📸"]
    )

    image = None
    if input_method == "Upload Image":
        uploaded_file = st.file_uploader(
            "Upload an image",
            type=["jpg", "jpeg", "png"]
        )
        if uploaded_file:
            try:
                image = Image.open(uploaded_file).convert("RGB")
            except UnidentifiedImageError:
                st.error("❌ Invalid image file.")
    else:
        camera_image = st.camera_input("Take a picture")
        if camera_image:
            try:
                image = Image.open(camera_image).convert("RGB")
            except UnidentifiedImageError:
                st.error("❌ Camera image not readable.")

    if image:
        st.image(image, caption="Input Image", use_container_width=True)

# ================= RIGHT COLUMN =================
with right_col:
    st.subheader("📊 Prediction Result")

    if image and st.button("🔍 Check Image"):
        try:
            with st.spinner("🔄 Analyzing image..."):
                # ===== PREPROCESS IMAGE =====
                img = image.resize((64, 64))
                img = np.array(img) / 255.0
                img = np.expand_dims(img, axis=0)

                # ===== PREDICTION =====
                prediction = model.predict(img, verbose=0)
                prob_dog = float(prediction[0][0])
                prob_cat = 1 - prob_dog
                predicted_class = 1 if prob_dog > 0.5 else 0

                # ===== CONFIDENCE =====
                confidence = int(abs(prob_dog - 0.5) * 200)
                if confidence >= 80:
                    confidence_label = "🟢 High Confidence"
                elif confidence >= 60:
                    confidence_label = "🟠 Medium Confidence"
                else:
                    confidence_label = "🔴 Low Confidence"

                # ===== DISPLAY RESULTS =====
                st.success(f"**{class_labels[predicted_class]}**")
                st.write(confidence_label)
                st.write("### Confidence")
                st.progress(confidence / 100)
                st.write(f"🐱 Cat: **{int(prob_cat*100)}%**  \n🐶 Dog: **{int(prob_dog*100)}%**")

                # ===== DOWNLOAD REPORT =====
                report = f"""
Cat vs Dog Prediction Report
----------------------------
Prediction: {class_labels[predicted_class]}
Cat Confidence: {int(prob_cat*100)}%
Dog Confidence: {int(prob_dog*100)}%
Overall Confidence: {confidence}%
"""
                st.download_button(
                    label="📦 Download Prediction Report",
                    data=report,
                    file_name="prediction_report.txt",
                    mime="text/plain"
                )

        except Exception as e:
            st.error("❌ Error during prediction.")
            st.exception(e)
    else:
        st.info("Upload or capture an image to start.")
