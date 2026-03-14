# Llama-3 Resume Intelligence System

An AI-powered application that analyzes resumes against job descriptions using **semantic embeddings, FAISS vector search, and Llama-3 reasoning**.
The system performs **skill gap analysis, candidate evaluation, and interview question generation** to assist recruiters in screening candidates.

---

## Features

* **Resume Parsing**

  * Extracts text from PDF resumes.

* **Semantic Resume Understanding**

  * Uses sentence embeddings to understand resume content.

* **Vector Search (FAISS)**

  * Retrieves relevant resume sections using similarity search.

* **LLM Reasoning**

  * Uses **Llama-3 via Groq API** to evaluate candidate-job fit.

* **Skill Gap Analysis**

  * Identifies missing skills compared to job description.

* **Interview Question Generation**

  * Automatically generates technical interview questions.

* **Interactive Web Interface**

  * Built with **Streamlit** for easy testing and demonstration.

---

## Tech Stack

* **Python**
* **Llama-3 (Groq API)**
* **Sentence Transformers**
* **FAISS Vector Database**
* **Streamlit**
* **PyMuPDF**

---

## System Architecture

```
Resume (PDF)
      │
      ▼
Resume Text Extraction
      │
      ▼
Text Chunking
      │
      ▼
Sentence Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
Relevant Resume Retrieval
      │
      ▼
Llama-3 Analysis
      │
      ▼
Candidate Match Score + Skill Gap + Interview Questions
```

---

## Project Structure

```
resume-intelligence-system
│
app.py
llm_analyzer.py
resume_parser.py
retriever.py
utils.py
vector_store.py
requirements.txt
README.md
.gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/resume-intelligence-system.git
cd resume-intelligence-system
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_api_key_here
```

Your API key will remain hidden from GitHub using `.gitignore`.

---

## Run the Application

```bash
python -m streamlit run app.py
```

Open your browser:

```
http://localhost:8501
```

---

## Usage

1. Upload a **PDF resume**
2. Paste a **job description**
3. The system will generate:

   * Candidate **match score**
   * **Strengths**
   * **Missing skills**
   * **Interview questions**

---

## Example Output

```
Match Score: 82%

Strengths:
Python, Machine Learning, NLP, Transformers

Missing Skills:
Docker, Kubernetes

Interview Questions:
1. Explain containerization in ML pipelines.
2. How would you deploy an NLP model in production?
3. What are the challenges in scaling ML systems?
```

---

## Future Improvements

* Resume skill extraction
* ATS-style resume scoring
* Multi-resume ranking system
* Recruiter dashboard
* Deployment with Docker

---

