import re

def has_char(text):
   # Returns True if any English letters are found, False otherwise (removes need to translate numbers)
   return bool(re.search(r'[a-zA-Z]', text))


def parse_docx(doc, text_map):
   # Collect Paragraph info
   for idx, para in enumerate(doc.paragraphs):
      if para.text.strip():
         text_map.append({
            "type": "paragraph",
            "index": idx,
            "text": para.text
         })

   # Collect table info
   for table_idx, table in enumerate(doc.tables):
      for row_idx, row in enumerate(table.rows):
         for col_idx, cell in enumerate(row.cells):
            for para_idx, para in enumerate(cell.paragraphs):
               if para.text.strip() and has_char(para.text):
                  text_map.append({
                     "type": "table_cell",
                     "table_idx": table_idx,
                     "row": row_idx,
                     "col": col_idx,
                     "para_idx": para_idx,
                     "text": para.text
                  })
   
   return text_map