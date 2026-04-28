from fpdf import FPDF
import os

docs = ["compliance_manual", "audit_guidelines", "reporting_guidelines"]

for doc in docs:
    txt_path = f"dataset/internal_docs/{doc}.txt"
    pdf_path = f"dataset/internal_docs/{doc}.pdf"
    
    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()
        
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    
    for line in text.split("\n"):
        pdf.multi_cell(0, 5, txt=line.encode('latin-1', 'replace').decode('latin-1'))
        
    pdf.output(pdf_path)
print("PDFs generated successfully.")
