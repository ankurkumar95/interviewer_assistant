from utils.main import InterviewerAssistant
import streamlit as st
 
def main():
    st.title("Interviewer Assistant")
    gemini_key = st.text_input("Enter your Gemini API key")
    assistant = InterviewerAssistant(api_key=gemini_key)
    uploaded_pdf = st.file_uploader("Upload your document")
    if uploaded_pdf:
        doc_path = f'{uploaded_pdf.name}'
        with open(doc_path, "wb") as f:
            f.write(uploaded_pdf.getvalue())
        resume_text = assistant.pdf_to_text(doc_path)
        summary = assistant.analyze_resume("\n".join(resume_text))
        questions = assistant.generate_questions(resume_text)
        answer = assistant.answer_question(questions, context=summary)
        st.write("Summary:\n {}".format(summary))
        st.write("Questions:\n {}".format("\n".join(questions)))
        st.write("Answer:\n {}".format(answer))
 
 
if __name__ == "__main__":
    main()