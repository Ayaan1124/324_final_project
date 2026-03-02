import fitz  # PyMuPDF
import os
from tqdm import tqdm

# ================================
# CONFIGURATION
# ================================

pdf_path = "pdf_data/BJP_2014.pdf"
txt_output = "data/BJP_2014.txt"

# ================================
# EXTRACTION
# ================================

# Open PDF
doc = fitz.open(pdf_path)
print(f"Loaded PDF: {pdf_path} ({doc.page_count} pages)")

# Extract text
full_text = ""

for page_num in tqdm(range(doc.page_count), desc="Extracting text"):
    page = doc[page_num]
    text = page.get_text("text")  # pure text mode
    full_text += text + "\n\n"

# Save to TXT
with open(txt_output, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"Saved text to: {txt_output}")