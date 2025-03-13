import easyocr
import gradio as gr
from PIL import Image

# OCR Reader
reader = easyocr.Reader(['en'])

# Function to extract text from image
def extract_text(image):
    result = reader.readtext(image)
    extracted_text = "\n".join([text[1] for text in result])
    return extracted_text

# Create Gradio UI
iface = gr.Interface(
    fn=extract_text,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Image to Text Converter",
    description="Upload an image and extract text using OCR."
)

# Run the WebApp
iface.launch()
