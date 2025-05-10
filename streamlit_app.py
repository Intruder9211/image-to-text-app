import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

# Load Model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

st.title("🖼️ Image Captioning App")

# Upload Image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Process Image
    inputs = processor(image, return_tensors="pt")

    # Generate Caption with Nucleus Sampling
    output = model.generate(**inputs, do_sample=True, top_p=0.9, max_length=50)
    caption = processor.decode(output[0], skip_special_tokens=True)

    st.subheader("Generated Caption:")
    st.write(f"**{caption}**")
