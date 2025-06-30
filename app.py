import os
import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()
AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_API_BASE = os.getenv("AZURE_OPENAI_API_BASE")
AZURE_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")

# Streamlit UI
st.set_page_config(page_title="Resume Ranker", layout="wide")
st.title("📄 Resume Ranker using Azure OpenAI")

# Upload Job Description
jd_file = st.file_uploader("Upload Job Description (PDF)", type=["pdf"])

# Upload multiple resumes
resume_files = st.file_uploader("Upload up to 10 Resume PDFs", type=["pdf"], accept_multiple_files=True)

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())

def get_ranking_chain(jd_text):
    llm = AzureChatOpenAI(
        deployment_name=AZURE_DEPLOYMENT_NAME,
        openai_api_key=AZURE_OPENAI_KEY,
        openai_api_base=AZURE_API_BASE,
        openai_api_version=AZURE_API_VERSION,
        model_name="gpt-4",
        temperature=0.3
    )

    prompt = PromptTemplate.from_template("""
You are an HR assistant helping screen resumes.

Given the following job description:
{jd}

And the resume content:
{resume}

Score this resume on a scale of 1 to 10 for how well it matches the job description. Return only the score and a short justification.

Example output format:
Score: 8
Reason: Matches 3 out of 4 core skills, lacks leadership experience.

Now score:
Resume:
{resume}
""")

    return LLMChain(llm=llm, prompt=prompt), jd_text

# Main logic
if jd_file and resume_files:
    jd_text = extract_text_from_pdf(jd_file)
    rank_chain, jd_context = get_ranking_chain(jd_text)

    results = []
    with st.spinner("Ranking resumes..."):
        for resume_file in resume_files:
            resume_text = extract_text_from_pdf(resume_file)
            result = rank_chain.run({"jd": jd_context, "resume": resume_text})
            name = resume_file.name.replace(".pdf", "")
            score_line = result.strip().splitlines()[0]
            score = int(score_line.replace("Score:", "").strip())
            reason = "\n".join(result.strip().splitlines()[1:])
            results.append({"Name": name, "Score": score, "Reason": reason})

    # Sort and display
    results.sort(key=lambda x: x["Score"], reverse=True)
    st.subheader("🏆 Ranked Resumes")
    for res in results:
        st.markdown(f"**{res['Name']}** — Score: {res['Score']}")
        st.text_area("Reason", res["Reason"], height=100, key=res['Name'])

