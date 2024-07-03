# SkillSync ATS Streamlit App

SkillSync ATS is an Applicant Tracking System implemented as a Streamlit web application. It matches resumes with job descriptions, provides recommendations, and generates interview questions based on candidate resumes.

## Description

SkillSync ATS simplifies the hiring process by analyzing resumes and job descriptions. It offers insights into candidate skills, recommends job matches, and generates tailored interview questions.

## Demo Video

(https://youtu.be/P66KUkNcgg0)

## Tech Stack Used

- **Frontend:**
  - Streamlit: Python-based web framework for creating interactive web applications.

- **Libraries and APIs:**
  - dotenv: Python library for loading environment variables from a .env file.
  - base64: Python library for encoding binary data to base64 format.
  - PIL (Python Imaging Library) / Pillow: Python imaging library for working with images, used for image processing.
  - pdf2image: Python library for converting PDF files to images.
  - google.generativeai: Custom API integration for accessing Google's generative AI models, utilizing an API key stored in environment variables.

## Installation

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the application using `streamlit run app.py`.

## Usage

1. **Upload Resume:**
   - Navigate to the application and upload a candidate's resume using the provided interface.
   - The system will parse the resume, extracting key information such as skills, experience, and education.

2. **Match Percentage:**
   - After uploading a job description, SkillSync ATS calculates a match percentage indicating how well the candidate's skills and experience align with the job requirements.

3. **Recommendations:**
   - Receive job recommendations based on the match percentage. SkillSync ATS suggests positions that best fit the candidate's qualifications and experience.

4. **Interview Questions:**
   - Generate interview questions tailored to different aspects of the candidate's profile:
     - **Resume Skills:** Questions related to technical skills and expertise listed in the resume.
     - **Behavioural Skills:** Questions focused on assessing soft skills, such as teamwork, communication, and problem-solving abilities.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request with your enhancements.


