import gradio as gr
import easyocr
import cv2
import numpy as np

reader = easyocr.Reader(['en'])

def image_to_text(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = reader.readtext(image)
    extracted_text = " ".join([res[1] for res in result])
    return extracted_text

interface = gr.Interface(
    fn=image_to_text,
    inputs=gr.Image(type="numpy"),
    outputs="text",
    title="Image to Text AI",
    description="Upload an image, and the AI will extract text from it."
)

interface.launch()
