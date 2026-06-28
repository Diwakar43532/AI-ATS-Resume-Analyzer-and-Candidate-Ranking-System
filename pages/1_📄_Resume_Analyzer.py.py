import streamlit as st
import json
import tempfile

import requests
import os

st.set_page_config(
    page_title="ATS Resume Analyzer",
    page_icon="📄",
    layout="wide"
)



st.title("📄 ATS Resume Analyzer")
st.caption("Upload your resume and compare it with the Job Description.")
st.divider()

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=180
)

if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.error("Please upload a resume.")
        st.stop()
    
    if job_description.strip() == "":
        st.error("Please paste a Job Description.")
        st.stop()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix="." + uploaded_file.name.split(".")[-1]
    ) as tmp:

        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    url = "http://127.0.0.1:8000/resume/match"

    with open(temp_path, "rb") as f:
        mime = (
            "application/pdf"
            if uploaded_file.name.endswith(".pdf")
            else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

        response = requests.post(
            url,
            files={
                "file": (uploaded_file.name, f, mime)
            },
            data={"job_description": job_description},
        )

    if os.path.exists(temp_path):
        os.remove(temp_path)

    if response.status_code == 200:
        result = response.json()
        
    else:
        st.error(f"API Error: {response.text}")
        st.stop()

    

    st.session_state["result"] = result
    st.success("Resume Parsed Successfully!")

# ===========================
# Display Parsed Resume
# ===========================

if "result" in st.session_state:

    result = st.session_state["result"]

    st.divider()
    st.header("📋 Resume Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"👤 Name\n\n{result.get('name', 'Not Found')}")
        st.info(f"📧 Email\n\n{result.get('email', 'Not Found')}")

    with col2:
        st.info(f"📞 Phone\n\n{result.get('phone', 'Not Found')}")

    # ===========================
    # Education
    # ===========================

    st.subheader("🎓 Education")

    education = result.get("education", [])

    if education:

        ignore = [
            "Qualification",
            "Institute / Board",
            "Marks / CGPA",
            "Year"
        ]

        for edu in education:

            degree = edu.get("degree", "")

            if degree in ignore:
                continue

            college = edu.get("college", "")
            year = edu.get("year", "")
            cgpa = edu.get("cgpa", "")
            percentage = edu.get("percentage", "")

            line = degree

            if college:
                line += f" | {college}"

            if year:
                line += f" | {year}"

            if cgpa:
                line += f" | CGPA: {cgpa}"

            if percentage:
                line += f" | {percentage}%"

            st.write("•", line)

    else:
        st.info("No education found.")

    # ===========================
    # Skills
    # ===========================

    st.divider()
    st.subheader("💻 Skills")

    skills = result.get("skills", [])

    if skills:
        st.write(", ".join(skills))
    else:
        st.warning("No skills found.")

    # ===========================
    # Experience
    # ===========================

    st.divider()
    st.subheader("💼 Experience")

    experience = result.get("experience", [])

    if experience:
        for exp in experience:
            role = exp.get("role", "")
            company = exp.get("company", "")
            duration = exp.get("duration", "")
            description = exp.get("description", [])

            if role:
                st.markdown(f"**👨‍💻 Role:** {role}")

            if company:
                st.markdown(f"**🏢 Company:** {company}")

            if duration:
                st.markdown(f"**📅 Duration:** {duration}")

            if description:

                st.markdown("**Responsibilities:**")

                for item in description:
                    st.write(f"• {item}")

            st.divider()

    else:
        st.info("No experience found.")
    # ===========================
    # Projects
    # ===========================

    st.divider()
    st.subheader("🚀 Projects")

    projects = result.get("projects", [])

    if projects:
        for project in projects:
            st.write("•", project)
    else:
        st.info("No projects found.")

    #============================
    # ATS Score
    #============================
    score = result.get("ats_score", 0)

    st.subheader("🎯 ATS Match Score")

    col1, col2 = st.columns([4, 1])

    with col1:
        st.progress(score / 100)

    with col2:
        st.metric("Score", f"{score}%")

    # Color Message
    if score >= 90:
        st.success("✅ Excellent Match")
    elif score >= 75:
        st.info("👍 Good Match")
    elif score >= 60:
        st.warning("⚠ Moderate Match")
    else:
        st.error("❌ Poor Match")

    st.write("### ✅ Matched Skills")

    matched = result.get("matched_skills", [])

    if matched:
        st.success(", ".join(matched))
    else:
        st.warning("No matching skills found.")

    # ===========================
    # JSON View
    # ===========================

    st.divider()

    with st.expander("📄 View Complete JSON"):
        st.json(result)

    # ===========================
    # Download Buttons
    # ===========================

    json_data = json.dumps(result, indent=4)

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label="⬇ Download JSON",
            data=json_data,
            file_name="resume_result.json",
            mime="application/json"
        )

    with col2:
        with open("output/resume.csv", "rb") as f:
            st.download_button(
                label="⬇ Download CSV",
                data=f,
                file_name="resume.csv",
                mime="text/csv"
            )