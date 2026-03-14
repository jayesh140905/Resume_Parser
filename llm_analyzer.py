from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_candidate(relevant_chunks, job_description):

    context = "\n".join(relevant_chunks)

    prompt = f"""
You are an AI recruiter.

Resume Evidence:
{context}

Job Description:
{job_description}

Tasks:
1. Estimate candidate-job match score (0-100)
2. Identify candidate strengths
3. Identify missing skills
3. Explain reasoning
4. Generate 3 interview questions
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content