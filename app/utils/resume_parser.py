import spacy
from PyPDF2 import PdfReader

def parse_resume(file_path):
    nlp = spacy.load("en_core_web_sm")
    text = extract_text_from_pdf(file_path)
    doc = nlp(text)

    skills = [ent.text for ent in doc.ents if ent.label_ == "SKILL"]
    return {"skills": skills}

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text
 
