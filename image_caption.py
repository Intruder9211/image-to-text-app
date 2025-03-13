import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import gradio as gr

# Load Model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Function to generate caption
def generate_caption(image):
    image = image.convert("RGB")
    inputs = processor(image, return_tensors="pt")
    with torch.no_grad():
        caption = model.generate(**inputs)
    caption_text = processor.decode(caption[0], skip_special_tokens=True)
    return caption_text

# Gradio Web App
iface = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="AI Image Captioning",
    description="Upload an image, and the AI will describe what's happening in it."
)

# Run App
iface.launch()
