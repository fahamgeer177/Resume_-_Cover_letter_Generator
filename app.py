import streamlit as st
import openai
import os

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Specify the model to use
MODEL_ID = "gpt-4o-mini"

def generate_resume(position_name, job_description, polish_prompt=""):
    if polish_prompt and polish_prompt.strip():
        prompt = (
            f"Based on the following job description for the position of {position_name}: {job_description}, "
            f"generate a professional resume tailored for this role. Please follow these additional instructions: {polish_prompt}. "
            "The resume should include relevant sections such as Summary, Skills, Experience, and Education. "
            "Make the resume as strong and relevant as possible for this job."
        )
    else:
        prompt = (
            f"Based on the following job description for the position of {position_name}: {job_description}, "
            "generate a professional resume tailored for this role. "
            "The resume should include relevant sections such as Summary, Skills, Experience, and Education. "
            "Make the resume as strong and relevant as possible for this job."
        )
    messages = [
        {"role": "system", "content": "You are a professional resume writer."},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=MODEL_ID,
        messages=messages
    )
    return response['choices'][0]['message']['content']

def generate_cover_letter(position_name, job_description, additional_instructions=""):
    if additional_instructions and additional_instructions.strip():
        prompt = (
            f"Based on the following job description for the position of {position_name}: {job_description}, "
            f"generate a professional cover letter tailored for this role. Please follow these additional instructions: {additional_instructions}. "
            "The cover letter should highlight relevant qualifications, skills, and experience for this job."
        )
    else:
        prompt = (
            f"Based on the following job description for the position of {position_name}: {job_description}, "
            "generate a professional cover letter tailored for this role. "
            "The cover letter should highlight relevant qualifications, skills, and experience for this job."
        )
    messages = [
        {"role": "system", "content": "You are a professional cover letter writer."},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model=MODEL_ID,
        messages=messages
    )
    return response['choices'][0]['message']['content']

st.set_page_config(page_title="AI Career Coach", layout="centered")
st.title("AI Career Coach")

option = st.sidebar.selectbox(
    "Choose a tool",
    ("Resume Generator", "Cover Letter Generator")
)

if option == "Resume Generator":
    st.header("Resume Generator")
    position_name = st.text_input("Position Name", "")
    job_description = st.text_area("Job Description", "", height=200)
    polish_prompt = st.text_area("Additional Instructions (Optional)", "", height=68)
    if st.button("Generate Resume"):
        if position_name and job_description:
            if not openai.api_key:
                st.error("OPENAI_API_KEY is not set. Please set it before generating content.")
            else:
                with st.spinner("Generating your resume..."):
                    result = generate_resume(position_name, job_description, polish_prompt)
                st.subheader("Generated Resume")
                st.write(result)
        else:
            st.warning("Please provide both Position Name and Job Description.")

elif option == "Cover Letter Generator":
    st.header("Cover Letter Generator")
    position_name = st.text_input("Position Name", "")
    job_description = st.text_area("Job Description", "", height=200)
    additional_instructions = st.text_area("Additional Instructions (Optional)", "", height=68)
    if st.button("Generate Cover Letter"):
        if position_name and job_description:
            if not openai.api_key:
                st.error("OPENAI_API_KEY is not set. Please set it before generating content.")
            else:
                with st.spinner("Generating your cover letter..."):
                    result = generate_cover_letter(position_name, job_description, additional_instructions)
                st.subheader("Generated Cover Letter")
                st.write(result)
        else:
            st.warning("Please provide both Position Name and Job Description.")
