import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

st.title("🖼️ Image to Text Captioning")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.markdown("⏳ **Generating caption...**")

    # Preprocess and generate
    inputs = processor(images=image, return_tensors="pt").to(model.device)
    output = model.generate(**inputs)

    caption = processor.decode(output[0], skip_special_tokens=True)
    
    st.subheader("📝 Caption:")
    st.success(caption)

