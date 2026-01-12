import streamlit as st
import requests

API_URL = "https://resume-analyzer-fnj1.onrender.com/api/analyze"

st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.title("AI Resume Analyzer")
st.write("Upload your Resume and Job Description to get an AI-based analysis.")

resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="Paste the full job description here..."
)

if st.button("Analyze Resume"):
    if not jd.strip():
        st.warning("Please paste the job description text")
        st.stop()

    if not resume or not jd:
        st.warning("Please upload the resume and job description")
        st.stop()

    with st.spinner("Analyzing..."):
        files = {
            "resume": resume,
        }
        data = {
            "jd": jd
        }

        response = requests.post(API_URL, files=files, data=data)

    if response.status_code != 200:
        st.error("Backend error occurred")
        st.stop()

    data = response.json()

    
    if "error" in data:
        st.error("Analysis failed")
        st.text(data.get("raw_output", data["error"]))
        st.stop()

    # Output
    match_percentage = data.get("match_percentage", "N/A")
    matched_skills = data.get("matched_skills", [])
    missing_skills = data.get("missing_skills", [])
    resume_improvements = data.get("resume_improvements", [])
    final_recommendation = data.get("final_recommendation", "Not available")


    st.success("Analysis Complete")

    st.metric("Match Percentage", f"{match_percentage}%")

    st.subheader("Matched Skills")
    if matched_skills:
        for skill in matched_skills:
            st.markdown(f"- {skill}")
    else:   
        st.write("No matched skills found")

    st.subheader("Missing Skills")
    if missing_skills:  
        for skill in missing_skills:
            st.markdown(f"- {skill}")
    else:
        st.write("No missing skills identified")


    st.subheader("Resume Improvement Suggestions")
    if resume_improvements:
        for tip in resume_improvements:
            st.write(f"- {tip}")
    else:
        st.write("No suggestions generated")

    st.subheader("Final Recommendation")
    st.info(final_recommendation)
