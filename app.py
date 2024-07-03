from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import PyPDF2  

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input, pdf_content, prompt])  # pdf_content is now text, not a list
    return response.text

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfFileReader(uploaded_file)
    text = ''
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        resume_text = extract_text_from_pdf(uploaded_file)

        pdf_parts = resume_text 
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


st.set_page_config(page_title="SkillSync")


st.header("SkillSync ATS 🤖")

input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

st.markdown('<div class="flex-container">', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    submit1 = st.button("About the Resume")
with col2:
    submit3 = st.button("Percentage match")
with col3:
    submit4 = st.button("Recommendations")
with col4:
    submit5 = st.button("Interview Questions")

st.markdown('</div>', unsafe_allow_html=True)

input_prompt1 = """
You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an experienced ATS (Applicant Tracking System) scanner with a deep understanding of ATS functionality. Your task is to evaluate a resume against the provided job description. First, provide the percentage match indicating how well the resume aligns with the job description. Next, list keywords that are present in the job description but missing in the resume. Finally, share your overall assessment and any additional thoughts.
"""

input_prompt4 = """
You are a career coach. Based on the provided resume and job description, give detailed recommendations to improve the resume to better align with the job requirements. Highlight specific areas to enhance.
"""

input_prompt5 = """
You are an experienced interviewer with a deep understanding of technical and behavioral assessment techniques. Based on the provided job description and resume, generate a comprehensive list of potential interview questions 7-8 in each section. These questions should include:
1. Technical questions related to the candidate's skills and experience as outlined in the resume.
2. Questions to assess the candidate's problem-solving abilities and proficiency in relevant technologies.
3. Behavioral questions to evaluate the candidate's fit for the company culture and their ability to work effectively in a team.
4. Questions to gauge the candidate's understanding of the industry.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4, pdf_content, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit5:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt5, pdf_content, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.write("Please upload the resume")
