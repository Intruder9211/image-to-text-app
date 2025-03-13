import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import easyocr

# OCR Reader
reader = easyocr.Reader(['en'])

# Function to extract text from image
def extract_text():
    file_path = filedialog.askopenfilename()  # Open file dialog
    if not file_path:
        return

    image = Image.open(file_path)
    image.thumbnail((400, 400))  # Resize for display
    img = ImageTk.PhotoImage(image)

    image_label.config(image=img)
    image_label.image = img

    result = reader.readtext(file_path)
    extracted_text = "\n".join([text[1] for text in result])

    text_display.config(state=tk.NORMAL)
    text_display.delete('1.0', tk.END)
    text_display.insert(tk.END, extracted_text)
    text_display.config(state=tk.DISABLED)

# Create GUI window
root = tk.Tk()
root.title("Image to Text Converter")
root.geometry("500x600")

# Upload button
upload_btn = tk.Button(root, text="Upload Image", command=extract_text)
upload_btn.pack(pady=10)

# Image display label
image_label = tk.Label(root)
image_label.pack()

# Text display area
text_display = tk.Text(root, height=10, width=50, wrap="word")
text_display.pack(pady=10)
text_display.config(state=tk.DISABLED)

root.mainloop()
