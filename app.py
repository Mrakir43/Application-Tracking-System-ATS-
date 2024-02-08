from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
import PyPdf2 as pdf
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_text(upload_file):
    reader=pdf.PdfReader(upload_file)
    text=""
    for page in reader(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text
    