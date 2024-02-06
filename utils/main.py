import google.generativeai as genai
import os
from pdf2image import convert_from_path

class InterviewerAssistant:
    def __init__(self, api_key):
        self.client = genai.configure(api_key=api_key)
        self.model_nlp = genai.GenerativeModel('gemini-pro')
        self.model_vision = genai.GenerativeModel('gemini-pro-vision')

    def analyze_resume(self, resume_text):
        """Analyzes a resume and provides a summary of the candidate's work."""
        prompt = f"Analyze the following resume and provide a short summary of the candidate's work:\n{resume_text}"
        response = self.model_nlp.generate_content(prompt)
        return response.text

    def generate_questions(self, resume_text):
        """Generates interview questions based on the resume."""
        prompt = f"Generate 5 interview questions that directly assess the candidate's work mentioned in the following resume:\n{resume_text}\nAlso, create one domain-specific coding question and one behavioral question."
        response = self.model_nlp.generate_content(prompt)
        questions = response.text.split("\n")
        return questions

    def answer_question(self, question, context=""):
        """Answers a specific interview question, optionally using context from previous responses."""
        prompt = f"{context}\nQuestion: {question}\nAnswer: "
        response = self.model_nlp.generate_content(prompt)
        return response.text
    
    def pdf_to_text(self, pdf_path, output_dir="out_png"):
        """Converts a PDF file to plain text."""
        if not os.path.exists(pdf_path):
            raise ValueError(f"PDF file not found: {pdf_path}")
        pages = convert_from_path(pdf_path, 500)
        response = list()
        for page_num in range(len(pages)):
            response.append(self.model_vision.generate_content(pages[page_num]).text)
        return response
