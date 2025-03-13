import streamlit as st
import easyocr
from PIL import Image

reader = easyocr.Reader(['en'])

st.title("Image to Text Converter")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    text = reader.readtext(uploaded_file, detail=0)
    st.write("Extracted Text:", " ".join(text))
