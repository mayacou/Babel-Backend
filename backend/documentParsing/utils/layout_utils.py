# from PIL import Image
# import pytesseract
# import io
# import fitz


# def ocr_image_bytes(image_bytes):
#    img = Image.open(io.BytesIO(image_bytes))
#    return pytesseract.image_to_string(img)

# def ocr_images_on_page(page_images):
#    ocr_blocks = []
#    for img in page_images:
#       text = ocr_image_bytes(img["image_bytes"])
#       if text.strip():
#          # You may need to estimate position or group it at top of page
#          ocr_blocks.append({"text": text.strip(), "bbox": (50, 50, 300, 100)})  # placeholder coords
#    return ocr_blocks

# def extract_text_and_images(pdf_path):
#    doc = fitz.open(pdf_path)
#    full_result = []

#    for page in doc:
#       page_text = page.get_text("text").strip()
#       image_blocks = page.get_images(full=True)

#       page_data = {
#          "text": page_text if page_text else None,
#          "images": [],
#       }

#       for img_index, img_info in enumerate(image_blocks):
#          xref = img_info[0]
#          base_image = doc.extract_image(xref)
#          image_bytes = base_image["image"]
#          page_data["images"].append({
#             "image_bytes": image_bytes,
#             "xref": xref
#          })

#       full_result.append(page_data)

#    return full_result

