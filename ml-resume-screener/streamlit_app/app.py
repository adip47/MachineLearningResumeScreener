
import streamlit as st
import requests

st.title("ML Resume Screener")

jd = st.text_area("Paste Job Description")
uploaded_resumes = st.file_uploader("Upload Resumes", type=["txt"], accept_multiple_files=True)

if st.button("Match"):
    files = {"jd": ("jd.txt", jd)}
    for i, file in enumerate(uploaded_resumes):
        files[f"resumes"] = (file.name, file.read())
    response = requests.post("http://localhost:8000/match/", files=files)
    st.json(response.json())
