# 📄 Resume Ranker using Azure OpenAI

This project is a Streamlit-based web application that ranks multiple resumes against a given job description using **Azure OpenAI's GPT-4 model**. It provides a score and a justification for each resume based on how well it matches the job description.

## 🚀 Features

- Upload a **Job Description (PDF)**.
- Upload **up to 10 Resumes (PDFs)**.
- Uses **Azure OpenAI (GPT-4)** to analyze and score each resume.
- Outputs:
  - A numerical **score (1-10)**.
  - A **justification** explaining the score.
  - **Sorted ranking** of all resumes for easy comparison.

## 🧠 Tech Stack

- [Streamlit](https://streamlit.io/) – for building the interactive UI.
- [LangChain](https://www.langchain.com/) – for chaining prompts and interacting with Azure OpenAI.
- [Azure OpenAI (GPT-4)](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/) – for semantic analysis and scoring.
- [PyPDF2](https://pypi.org/project/PyPDF2/) – for extracting text from PDFs.
- [Python-dotenv](https://pypi.org/project/python-dotenv/) – for managing environment variables securely.

## 🖼️ UI Preview

![App Screenshot](https://via.placeholder.com/900x400?text=Resume+Ranker+Streamlit+App)

> Replace the screenshot URL with your deployed app screenshot or a local image path.

## 📂 Folder Structure

resume-ranker/
│
├── resume_ranker.py # Main Streamlit app
├── .env # Environment variable file (not included in Git)
├── requirements.txt # Python dependencies
└── README.md # Project readme


## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-ranker.git
cd resume-ranker

pip install -r requirements.txt

streamlit run resume_ranker.py
```
## 🌐 Connect with Me

- 🔗 Portfolio: [shreel.framer.ai](https://shreel.framer.ai)
- 💼 LinkedIn: [linkedin.com/in/shreelfaldu](https://linkedin.com/in/shreelfaldu)
- 📷 Instagram: [@shreel.faldu](https://instagram.com/shreel.faldu)
- 📧 Email: shreel.faldu121124@marwadiuniversity.ac.in
