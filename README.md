# 🧠 AI Resume Analyzer (GenAI + RAG)

An AI-powered Resume Analyzer that compares a candidate’s resume against a job description and provides **match percentage, skill alignment, missing skills, and actionable improvement suggestions** using Large Language Models (LLMs).

This project is designed to simulate a **real-world recruiter screening workflow**, combining **FastAPI, Streamlit, and Generative AI** into a production-style application.

---

## 🔍 What This Project Does

Recruiters often spend a lot of time manually reviewing resumes against job descriptions. This application automates that process by:

* Parsing resumes (PDF format)
* Understanding job descriptions semantically
* Using AI to evaluate skill overlap and gaps
* Providing structured, human-readable feedback

The goal is **not just scoring**, but offering **meaningful insights** that help candidates improve their resumes.

---

## 🧩 Key Features

* 📄 **PDF Resume Parsing** using `pypdf`
* 🧠 **LLM-based Analysis** with structured JSON output
* 📊 **Match Percentage Scoring**
* ✅ **Matched Skills & Missing Skills Identification**
* ✍️ **Actionable Resume Improvement Suggestions**
* 🌐 **FastAPI Backend** for scalable API access
* 🎨 **Streamlit Frontend** for a clean, interactive UI
* 🔐 Secure API key handling via environment variables

---

## 🏗️ Project Architecture

```
Resume-Analyzer/
│
├── api/
│   ├── main.py            # FastAPI app entry point
│   ├── routes.py          # /api/analyze endpoint
│   └── rag/
│       └── llm.py         # LLM configuration
│
├── frontend/
│   └── app.py             # Streamlit frontend
│
├── requirements.txt
├── README.md
└── .env.example           # Environment variable template
```

---

## ⚙️ Tech Stack

* **Backend**: FastAPI, Uvicorn
* **Frontend**: Streamlit
* **AI / NLP**: LangChain, OpenAI API
* **PDF Processing**: PyPDF
* **Deployment**: Render (backend), Streamlit Cloud (frontend)
* **Version Control**: Git & GitHub

---

## 🚀 How It Works (High Level)

1. User uploads a **PDF resume** and pastes a **job description**
2. Resume text is extracted from the PDF
3. A carefully crafted prompt is sent to the LLM
4. The LLM analyzes:

   * Skill overlap
   * Missing requirements
   * Resume quality
5. The model returns **structured JSON**
6. Streamlit displays the results in a clean, point-wise format

---

## 🧪 Local Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Soumya-Choudhury/Resume-Analyzer.git
cd Resume-Analyzer
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

### 5️⃣ Run backend

```bash
uvicorn api.main:app --reload --port 8001
```

### 6️⃣ Run frontend

```bash
streamlit run frontend/app.py
```

---

## 🧠 Challenges Faced

This project came with several real-world challenges:

* **LLM output inconsistency**
  The model sometimes returned non-JSON text. This was handled by enforcing strict output format and adding robust JSON extraction logic.

* **PDF text extraction issues**
  Some resumes had formatting issues or empty pages, requiring fallback handling.

* **Environment variable security**
  Accidentally committing `.env` caused GitHub push protection to block commits, reinforcing proper secret management practices.

* **Deployment complexity**
  Deploying backend and frontend separately required careful API URL handling and debugging network-level issues.

* **Long-running API calls**
  LLM latency caused the frontend to appear “stuck,” which was resolved by better loading indicators and timeout awareness.

These challenges closely mirror problems faced in **real production AI systems**, making the project a strong learning experience.

---

## 🔮 Future Improvements

This project can be further enhanced in several ways:

* 🔍 **True RAG with Vector Search**
  Use FAISS or Pinecone to store resumes and job descriptions for multi-document comparison.

* 📈 **Skill Weighting System**
  Assign higher importance to core skills vs nice-to-have skills.

* 👤 **User Accounts & History**
  Allow users to track previous analyses and improvements over time.

* 📄 **Multi-format Resume Support**
  Support DOCX and image-based resumes using OCR.

* 🧪 **Evaluation Metrics**
  Add confidence scores and explainability for each decision.

* 🌍 **Cloud-native Scaling**
  Use background tasks, async processing, and caching for higher throughput.

---

## 🎯 Why This Project Matters

This project demonstrates:

* Real-world **GenAI application design**
* Backend–frontend integration
* Clean API architecture
* Secure handling of secrets
* Production deployment challenges
* Thoughtful UX for AI outputs

It reflects how AI systems are actually built and deployed—not just trained.

---

## 👤 Author

**Soumya Choudhury**
Software Development & AI Enthusiast

* GitHub: [https://github.com/Soumya-Choudhury](https://github.com/Soumya-Choudhury)
* LinkedIn: [https://linkedin.com/in/soumya-choudhury27](https://linkedin.com/in/soumya-choudhury27)

---

⭐ If you found this project interesting, feel free to star the repository and connect with me!
