import PyPDF2
import re

def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text.lower()

def calculate_ats_score(resume_text, job_skills):
    if not job_skills:
        return 0.0

    # Clean and split job skills
    skills_list = [skill.strip().lower() for skill in job_skills.split(',')]
    
    if not skills_list:
        return 0.0

    match_count = 0
    for skill in skills_list:
        # Use regex to find whole word matches for the skill
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, resume_text):
            match_count += 1

    # Calculate percentage
    score = (match_count / len(skills_list)) * 100
    return round(score, 2)
