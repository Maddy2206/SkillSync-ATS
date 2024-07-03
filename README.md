# SkillSync ATS

SkillSync ATS is a specialized Applicant Tracking System implemented as a Streamlit web application. Its primary focus is to assist candidates in preparing for job applications by refining their resumes. By analyzing resumes and job descriptions, SkillSync ATS provides personalized recommendations to enhance candidate profiles, ensuring alignment with employer expectations. Additionally, it generates targeted interview questions based on the content of candidate resumes, empowering individuals to effectively showcase their qualifications and skills in the competitive job market.

![image](https://github.com/Maddy2206/SkillSync-ATS/assets/143317316/a35167a5-dcaf-4e6f-bf0d-a9b76bf42913)

## Demo Video

(https://youtu.be/P66KUkNcgg0)

## Tech Stack Used

- **Frontend:**
  - **Streamlit**: Python-based web framework for creating interactive web applications.

- **Libraries and APIs:**
  - **dotenv**: Python library for loading environment variables from a .env file.
  - **base64**: Python library for encoding binary data to base64 format.
  - **PIL (Python Imaging Library) / Pillow**: Python imaging library for working with images, used for image processing.
  - **pdf2image**: Python library for converting PDF files to images.
  - **google.generativeai**: Custom API integration for accessing Google's generative AI models, utilizing an API key stored in environment variables.

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

![image](https://github.com/Maddy2206/SkillSync-ATS/assets/143317316/305da84d-1619-4692-829c-b6d8aaa70258)



3. **Recommendations:**
   - Receive job recommendations based on the match percentage. SkillSync ATS suggests positions that best fit the candidate's qualifications and experience.

![image](https://github.com/Maddy2206/SkillSync-ATS/assets/143317316/66933cae-475e-439f-ba39-8ee65aa98481)



4. **Interview Questions:**
   - Generate interview questions tailored to different aspects of the candidate's profile:
     - **Resume Skills:** Questions related to technical skills and expertise listed in the resume.
     - **Behavioural Skills:** Questions focused on assessing soft skills, such as teamwork, communication, and problem-solving abilities.
    
![image](https://github.com/Maddy2206/SkillSync-ATS/assets/143317316/de4838bf-a2a2-4b34-b043-7911439ea345)

## Motivation to build this

SkillSync ATS is a dedicated Applicant Tracking System implemented as a Streamlit web application. It is designed to empower job seekers by optimizing their resume preparation process. Motivated by the desire to bridge the gap between candidate skills and employer expectations, SkillSync ATS meticulously analyzes resumes and job descriptions. It provides tailored recommendations to enhance resume content, ensuring candidates present themselves effectively to prospective employers. Additionally, the system generates targeted interview questions derived from resume insights, equipping candidates with the tools they need to confidently pursue career opportunities and stand out in competitive job markets.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request with your enhancements.


