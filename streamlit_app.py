import streamlit as st
import easyocr
import numpy as np
from PIL import Image

# Load OCR Model
reader = easyocr.Reader(['en'])

st.title("🖼 Image to Text Converter")

# File Upload
uploaded_file = st.file_uploader("Upload an Image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert image file to PIL Image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert PIL Image to NumPy array
    image_np = np.array(image)

    # Extract text from image
    text = reader.readtext(image_np, detail=0)
    
    # Display extracted text
    st.subheader("Extracted Text:")
    st.write(" ".join(text))

