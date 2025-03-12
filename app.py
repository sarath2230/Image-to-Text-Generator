from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import google.generativeai as genai
from PIL import Image
# Configure Google API key
os.environ["GOOGLE_API_KEY"] = "Your api key"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def generate_text_from_image(image_path):
    
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    with open(image_path, "rb") as image_file:
        image = Image.open(image_file)
        response = model.generate_content(image)
    return response.text

@app.route('/', methods=['GET', 'POST'])
def index():
    filename = None
    caption = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file:
            # Save the file to the upload folder
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Generate caption using the provided code
            caption = generate_text_from_image(filepath)

    return render_template('index.html', filename=filename, caption=caption)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
