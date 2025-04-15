import streamlit as st
from model_helper import predict


st.title("🚗 vehicle Damage Detection")

uploaded_file = st.file_uploader("Upload the file", type=["jpg", "png"])

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        prediction = predict(image_path)
        st.image(uploaded_file, caption="Uploaded File", width=500)
        st.info(f"Predicted Class: {prediction}")