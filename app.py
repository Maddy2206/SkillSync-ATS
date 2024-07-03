from dotenv import load_dotenv
import base64
import streamlit as st
import os
import io
from PIL import Image 
import pdf2image
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file, poppler_path):
    if uploaded_file is not None:
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read(), poppler_path=poppler_path)

        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit App Configuration
st.set_page_config(page_title="SkillSync")

# Apply dark theme from config.toml

st.header("SkillSync ATS 🤖")

input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

st.markdown('<div class="flex-container">', unsafe_allow_html=True)

# Add additional buttons for new features
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
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
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

# Specify the path to the poppler bin directory
poppler_path = r'C:\Users\rawat\Downloads\Release-24.02.0-0\poppler-24.02.0\Library\bin'

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file, poppler_path)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file, poppler_path)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file, poppler_path)
        response = get_gemini_response(input_prompt4, pdf_content, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit5:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file, poppler_path)
        response = get_gemini_response(input_prompt5, pdf_content, input_text)
        st.subheader("Response")
        st.write(response)
    else:
        st.write("Please upload the resume")
