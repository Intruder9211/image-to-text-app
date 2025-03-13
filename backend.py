from flask import Flask, request, jsonify
import easyocr
from PIL import Image
import io

app = Flask(__name__)
reader = easyocr.Reader(['en'])

@app.route('/image-to-text', methods=['POST'])
def image_to_text():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']
    img = Image.open(io.BytesIO(image.read()))
    
    result = reader.readtext(img)
    extracted_text = " ".join([text[1] for text in result])
    
    return jsonify({"text": extracted_text})

if __name__ == '__main__':
    app.run(debug=True)
