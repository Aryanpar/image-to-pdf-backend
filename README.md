# 🖨️ Image to PDF Backend (Flask)

Backend API for converting multiple images into a single PDF — with optional watermark, password protection, and image quality control.

This backend is designed to work with a Flutter mobile app, but it can be used with any HTTP client.

---

## 🚀 Features

✔ Upload multiple images  
✔ Convert to single PDF  
✔ Optional watermark text  
✔ Optional password protection  
✔ Adjustable image quality / compression  
✔ Input validation  
✔ Automatic temp-file cleanup  
✔ Production-ready structure  
✔ REST API design  

---

## 🛠 Tech Stack

- Python
- Flask
- Pillow (Image processing)
- PyPDF2 (PDF encryption)
- Gunicorn (deployment)
- Render.com (hosting)

---

## 📂 Project Structure

app/
│
├── server.py # API entrypoint
├── init.py # flask app factory
├── config.py # constants & settings
└── utils/
├── pdf_builder.py # pdf processing logic
├── image_utils.py # image utilities
└── security.py # validation utilities

uploads/ # temporary input files
output/ # generated PDFs
requirements.txt
