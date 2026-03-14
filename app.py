import streamlit as st

from resume_parser import extract_resume_text
from utils import chunk_text
from vector_store import build_vector_store
from retriever import retrieve_sections
from llm_analyzer import analyze_candidate

st.title("LLM Resume Intelligence System")

resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if resume is None:
    st.info("Please upload a resume.")

if job_description == "":
    st.info("Please paste a job description.")

if resume and job_description:

    with st.spinner("Analyzing resume..."):

        text = extract_resume_text(resume)

        chunks = chunk_text(text)

        index, embeddings = build_vector_store(chunks)

        relevant_chunks = retrieve_sections(
            "candidate skills experience projects", chunks, index
        )

        result = analyze_candidate(relevant_chunks, job_description)

    st.subheader("Analysis Result")
    st.write(result)