# import fitz  # PyMuPDF
# import pdfplumber

# def write_clean_pdf_with_images(original_pdf, parsed_blocks_per_page, output_path):
#     original_doc = fitz.open(original_pdf)
#     new_doc = fitz.open()

#     for page_index, original_page in enumerate(original_doc):
#         # Create new blank page with same dimensions
#         new_page = new_doc.new_page(width=original_page.rect.width, height=original_page.rect.height)

#         # Add images from original page
#         image_list = original_page.get_images(full=True)
#         for img in image_list:
#             xref = img[0]
#             base_image = original_doc.extract_image(xref)
#             pix = fitz.Pixmap(original_doc, xref)
#             rects = original_page.get_image_rects(xref)
#             for rect in rects:
#                 new_page.insert_image(rect, pixmap=pix)

#         # Add parsed text
#         parsed_blocks = parsed_blocks_per_page[page_index]
#         for block in parsed_blocks:
#             x0, y0, x1, y1 = block["bbox"]
#             text = block["text"]
#             rect = fitz.Rect(x0, y0, x1, y1)
#             new_page.insert_textbox(
#                 rect,
#                 text,
#                 fontsize=8,
#                 fontname="helv",
#                 color=(0, 0, 0),
#                 align=0  # left-aligned
#             )

#     new_doc.save(output_path)
#     print(f"✅ Clean PDF with images saved: {output_path}")
