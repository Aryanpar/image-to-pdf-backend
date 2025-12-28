import os
import io
from PIL import Image, ImageDraw, ImageFont
from PyPDF2 import PdfReader, PdfWriter
from app.utils.image_utils import open_image

def add_watermark(image, text, opacity=90):
    if not text:
        return image

    watermark = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(watermark)

    font = ImageFont.load_default()
    textwidth, textheight = draw.textsize(text, font)

    x = (image.width - textwidth) // 2
    y = (image.height - textheight) // 2

    draw.text((x, y), text, fill=(150,150,150,opacity), font=font)

    return Image.alpha_composite(image.convert("RGBA"), watermark).convert("RGB")


def build_pdf(image_paths, page_size=None, orientation="portrait", quality=85, watermark_text=None):
    processed_images = []

    for p in image_paths:
        img = open_image(p)

        if watermark_text:
            img = add_watermark(img, watermark_text)

        processed_images.append(img)

    pdf_bytes = io.BytesIO()
    processed_images[0].save(
        pdf_bytes,
        save_all=True,
        append_images=processed_images[1:],
        format="PDF"
    )
    pdf_bytes.seek(0)

    return pdf_bytes


def apply_password(pdf_bytes, password):
    if not password:
        return pdf_bytes

    reader = PdfReader(pdf_bytes)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    secured_pdf = io.BytesIO()
    writer.write(secured_pdf)
    secured_pdf.seek(0)

    return secured_pdf
