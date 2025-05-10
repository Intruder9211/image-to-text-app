import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

st.set_page_config(page_title="Image to Caption", layout="centered")

@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()
device = torch.device("cpu")  # force CPU to avoid GPU transfer error
model.to(device)

st.title("🖼️ Image to Text Generator using BLIP")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button("Generate Caption"):
        with st.spinner("Generating..."):
            inputs = processor(images=image, return_tensors="pt").to(device)
            output = model.generate(**inputs, do_sample=True, top_p=0.9, max_length=50)
            caption = processor.tokenizer.decode(output[0], skip_special_tokens=True)

            st.success("Caption Generated!")
            st.markdown(f"**📝 Detected Caption:** `{caption}`")
