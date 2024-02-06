# Streamline Interviewer Prep with Streamlit and Gemini

⚡ Timesaving approach for taking interviews ⚡

## Project Description:

This project helps recruiters save time and effort by automating resume analysis and question generation using Streamlit and the powerful Gemini text-to-text model. It offers a user-friendly web interface for seamless interaction with the functionalities.

## Key Features:

- **Streamlit UI**: Intuitive and interactive interface for easy file uploads and results visualization.
- **Gemini Integration**: Leverages Gemini's text understanding and question answering capabilities for accurate analysis and context-aware responses.
- **Resume Analysis**: Extracts key skills, experiences, and qualifications from uploaded resumes.
- **Dynamic Question Generation**: Tailors interview questions based on the extracted resume information.
- **Context-Aware Answers**: Provides answers to generated questions within the context of the resume.

## Usage:

1. Enter your Gemini API key.
2. Upload a PDF resume.
3. The app will display:
    - A summary of the resume's key points
    - A list of generated interview questions
    - Answers to the questions based on the resume context

## Quick Setup

```bash
git clone https://github.com/ankurkumar95/interviewer_assistant.git
cd interviewer-assistant
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run run.py
```

