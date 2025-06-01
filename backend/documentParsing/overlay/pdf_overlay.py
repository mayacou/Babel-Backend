# import fitz  # PyMuPDF

# def overlay_translated_text(input_pdf, translated_blocks_per_page, output_pdf):
#     doc = fitz.open(input_pdf)

#     for page_index, page in enumerate(doc):
#         translated_blocks = translated_blocks_per_page[page_index]
#         for block in translated_blocks:
#             x0, y0, x1, y1 = block["bbox"]
#             text = block["text"]

#             # ⬇️ Shrink bounding box by 10% vertically, 5% horizontally
#             width = x1 - x0
#             height = y1 - y0
#             shrink_h = height * 0.03
#             shrink_w = width * 0.005

#             rect = fitz.Rect(
#                 x0 + shrink_w,
#                 y0 + shrink_h / 2,
#                 x1 - shrink_w,
#                 y1 - shrink_h / 2
#             )

#             # 1. Draw white background
#             page.draw_rect(rect, fill=(1, 1, 1), color=(1,0,0), fill_opacity=0.9)

#             # 2. Try inserting text
#             font_size = 9  # fixed for now, adjust later if you want dynamic sizing
#             try:
#                 inserted = page.insert_textbox(
#                     rect,
#                     text,
#                     fontsize=font_size,
#                     fontname="helv",
#                     align=3,
#                     color=(0, 0, 0)
#                 )

#                 if inserted == 0:
#                     print(f"[WARN] Text didn't fit: '{text[:30]}...' @ {rect}")

#             except Exception as e:
#                 print(f"[ERROR] Failed to insert: {e}")
#                 page.insert_text((x0, y0), text, fontsize=font_size, color=(1, 0, 0))

#     doc.save(output_pdf)
#     print(f"✅ Overlay saved to: {output_pdf}")
