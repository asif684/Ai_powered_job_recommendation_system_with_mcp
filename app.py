import streamlit as st
from src.helper import extract_text_from_pdf, ask_euri
from src.job_api import fetch_naukri_jobs

st.set_page_config(page_title="AI Job Recommender", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Center the main title */
    .main-title {
        text-align: center;
        color: #1f77b4;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    /* Center the description */
    .description {
        text-align: center;
        font-size: 18px;
        color: #333333;
        margin-bottom: 30px;
    }

    /* Card styling */
    .card {
        background-color: #f9f9f9; /* lighter background for readability */
        color: #000000;             /* text color */
        padding: 20px;
        margin-bottom: 15px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        font-size: 16px;            /* readable font size */
        line-height: 1.5;
    }

    .section-title {
        color: #1f77b4;
        font-weight: bold;
        font-size: 20px;
        margin-bottom: 10px;
    }

    .job-title {
        font-weight: bold;
        font-size: 16px;
        color: #0d47a1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Centered Title and Description
st.markdown('<h1 class="main-title">📄 AI Job Recommender </h1>', unsafe_allow_html=True)
st.markdown('<p class="description">Upload your resume and get AI-driven career insights along with Naukri job recommendations.</p>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("📄 Extracting text from your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("📝 Summarizing your resume..."):
        summary = ask_euri(
            f"Summarize this resume highlighting skills, education, and experience:\n\n{resume_text}",
            max_tokens=500
        )

    with st.spinner("⚡ Finding skill gaps..."):
        gaps = ask_euri(
            f"Analyze this resume and highlight missing skills, certifications, and experiences:\n\n{resume_text}",
            max_tokens=400
        )

    with st.spinner("🚀 Creating roadmap..."):
        roadmap = ask_euri(
            f"Based on this resume, suggest a roadmap to improve career prospects (skills, certifications, industry exposure):\n\n{resume_text}",
            max_tokens=400
        )

    # Display insights in columns
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("📑 Resume Summary")
        st.markdown(f"<div class='card'>{summary}</div>", unsafe_allow_html=True)
    with col2:
        st.subheader("🛠 Skill Gaps")
        st.markdown(f"<div class='card'>{gaps}</div>", unsafe_allow_html=True)
    with col3:
        st.subheader("🚀 Career Roadmap")
        st.markdown(f"<div class='card'>{roadmap}</div>", unsafe_allow_html=True)

    st.success("✅ Analysis Completed!")

    # Job Recommendations
    if st.button("🔎 Get Naukri Job Recommendations"):
        with st.spinner("💡 Generating job keywords..."):
            keywords = ask_euri(
                f"Based on this resume summary, suggest the best job titles and keywords (comma-separated):\n\n{summary}",
                max_tokens=100
            )
            search_keywords_clean = keywords.replace("\n", "").strip()

        st.success(f"Extracted Job Keywords: {search_keywords_clean}")

        with st.spinner("🔍 Fetching jobs from Naukri..."):
            naukri_jobs = fetch_naukri_jobs(search_keywords_clean, rows=60)

        st.markdown("---")
        st.header("💼 Top Naukri Jobs")

        if naukri_jobs:
            for i, job in enumerate(naukri_jobs, start=1):
                with st.expander(f"{i}. {job.get('title')} at {job.get('companyName')}"):
                    st.markdown(f"<div class='card'>"
                                f"📍 Location: {job.get('location')}  \n"
                                f"🔗 [View Job]({job.get('url')})"
                                f"</div>", unsafe_allow_html=True)
        else:
            st.warning("No Naukri jobs found.")
