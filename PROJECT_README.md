# HireHub ATS (Applicant Tracking System)

## Project Overview
HireHub ATS is a modern, web-based Applicant Tracking System built using Django. It is designed to act as a bridge between Company Administrators posting jobs and Candidates (Students) looking for opportunities. 

The standout feature of this platform is the built-in **ATS Match Scorer**, which uses Python's `PyPDF2` library to physically read the text inside a candidate's uploaded PDF resume, compare the extracted words against the required skills of the job they are applying for, and instantly calculate an ATS Match Score percentage.

## Technologies Used
- **Backend**: Python 3, Django 6.0.3 Web Framework
- **Database**: MySQL (accessed via `PyMySQL`)
- **Frontend Structures**: HTML5, Django Templates
- **Styling**: Vanilla CSS, Bootstrap 5 Framework, Bootstrap Icons
- **Resume Parsing**: `PyPDF2` (Python library for extracting text from PDF files)
- **Asynchronous Execution**: JavaScript `Fetch()` API for AJAX form handling.

## Key Features & Code Explanation

### 1. Custom User Models (`accounts\models.py`)
To keep the application highly secure and organized, the default Django user model was extended into a `CustomUser`. This custom model introduced boolean flags: `is_student` and `is_admin_user`. This allows the application to cleanly separate candidates from recruiters using built-in Django route protections.

### 2. The ATS Scoring Engine (`ats_scorer\utils.py`)
This file is the brain of the application. It contains two vital functions:
*   `extract_text_from_pdf(pdf_file)`: Safely consumes the binary PDF data from the frontend upload and iterates over its pages to extract raw text variables.
*   `calculate_ats_score(resume_text, job_skills)`: A custom algorithm that compares the words found in the resume against a list of required job skills, calculating the percentage of required skills that the candidate actually possesses. 

### 3. Dynamic Email Dispatching (`ats_scorer\views.py`)
When a student applies for a role, the application utilizes Django's `send_mail` functionality to fire off an automated email to the student summarizing their application status. This email is dynamically generated into one of three formats (Shortlisted, Under Review, or Rejected) based entirely on if the candidate's ATS score surpassed thresholds of 70% or 40%.

### 4. Seamless AJAX Form Submissions (`templates\ats_scorer\apply.html`)
To prevent the web browser from undergoing a jarring page reload every time an application is submitted, the frontend was equipped with an asynchronous JavaScript fetch API event listener. 
It intercepts the "Submit" click, morphs the button into an interactive loading spinner, and transmits the PDF to the backend silently. Once `views.py` processes the file and responds with a `JsonResponse`, the Javascript automatically updates the DOM to display the matching ATS score to the user instantly.

### 5. Glassmorphism UI & Pure CSS Backgrounds (`templates\base\base.html`)
Instead of a stationary, boring background, the application features an infinitely animated background composed of drifting, rotating geometric polygons. 
Furthermore, elements like the top Navbar and dropdown menus employ an advanced CSS technique known as **Glassmorphism**. They utilize semi-transparent `rgba` backgrounds paired with `-webkit-backdrop-filter: blur(15px);` to create a stunning "frosted glass" effect that beautifully blurs the floating geometric shapes moving beneath it.
