
# 🖼️ Image to Text Generator  

This is a Flask-based web application that allows users to upload an image and generate text descriptions using AI. It utilizes **Google Generative AI** to analyze and extract meaningful text from images. The project is designed to be simple, efficient, and easy to use.  

## 🚀 Project Overview  

The **Image to Text Generator** aims to bridge the gap between image processing and AI-driven text generation. Whether it's recognizing objects, or scenes  this project provides an automated solution.  

### 🌟 Key Features  
✅ Upload an image and extract text descriptions  
✅ Uses **Google Generative AI** for text processing  
✅ Flask-based backend for handling image uploads and processing  
✅ User-friendly web interface built with **HTML, CSS, and JavaScript**  
✅ Supports multiple image formats  
✅ Fast and accurate AI-powered text generation  

---

## 🛠️ Tech Stack  
- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **AI Model:** Google Generative AI  
- **Image Processing:** Pillow (PIL)  
- **Deployment:** Docker (optional)  

---

## 📥 Installation  

Follow these steps to set up and run the project locally:  

### 1️⃣ Clone the repository:  
```sh
git clone https://github.com/sarath2230/Image-to-Text-Generator.git
```  
   
### 2️⃣ Navigate to the project folder:  
```sh
cd Image-to-Text-Generator
```  
   
### 3️⃣ Create a virtual environment (optional but recommended):  
```sh
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
```  
   
### 4️⃣ Install dependencies:  
```sh
pip install -r requirements.txt
```  
   
### 5️⃣ Run the Flask application:  
```sh
python app.py
```  
   
### 6️⃣ Open the application in your browser:  
```
http://127.0.0.1:5000/
```  

---

## 🎯 How It Works  
1️⃣ Upload an image using the web interface.  
2️⃣ The backend processes the image and sends it to Google Generative AI.  
3️⃣ The AI model analyzes the image and generates text-based descriptions.  
4️⃣ The extracted text is displayed on the web interface.  

---

