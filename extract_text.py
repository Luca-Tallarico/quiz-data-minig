import os
from pypdf import PdfReader

def extract_text_from_pdfs():
    pdf_files = [
        "APPUNTI LEZIONE_mining copia.pdf",
        "Lecture_01.5_Handouts_SQL_queries.pdf",
        "Lecture_01_Data_Mining_Introduction_2025_2026.pdf",
        "Lecture_02_Clustering_Techniques.pdf",
        "Lecture_03_Perceptron_and_Learning_Process.pdf",
        "Lecture_04. Text Mining_1.pdf",
        "Lecture_05 Text_Mining_2.pdf",
        "Lecture_06 Text Classification.pdf"
    ]
    
    output_file = "course_notes.md"
    
    with open(output_file, "w", encoding="utf-8") as f:
        for pdf_file in pdf_files:
            if not os.path.exists(pdf_file):
                print(f"File not found: {pdf_file}")
                continue
                
            print(f"Processing {pdf_file}...")
            f.write(f"# Document: {pdf_file}\n\n")
            
            try:
                reader = PdfReader(pdf_file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                f.write(text)
                f.write("\n\n---\n\n")
            except Exception as e:
                print(f"Error reading {pdf_file}: {e}")
                f.write(f"Error extracting text from {pdf_file}: {e}\n\n")

if __name__ == "__main__":
    extract_text_from_pdfs()
