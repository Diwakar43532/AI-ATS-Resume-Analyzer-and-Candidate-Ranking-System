import streamlit as st
import tempfile
import pandas as pd
import json

import requests
import os






st.set_page_config(layout="wide")

st.title("🏆 Resume Ranking System")

st.write("Upload multiple resumes and rank them based on Job Description.")

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf","docx"],
    accept_multiple_files=True
)

job_description = st.text_area(
    "Paste Job Description"
)

if st.button("Rank Resumes"):

    if not uploaded_files:

        st.error("Upload resumes first.")

    elif job_description == "":

        st.error("Paste Job Description.")

    else:

        st.success(f"{len(uploaded_files)} resumes uploaded.")
    
        with st.spinner("Ranking resumes..."):

            files = []

            temp_files = []

            for uploaded_file in uploaded_files:

                suffix = "." + uploaded_file.name.split(".")[-1]

                tmp = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix
                )

                tmp.write(uploaded_file.read())
                tmp.close()

                temp_files.append(tmp.name)

                mime = (
                    "application/pdf"
                    if uploaded_file.name.endswith(".pdf")
                    else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

                files.append(

                    (
                        "files",
                        (
                            uploaded_file.name,
                            open(tmp.name, "rb"),
                            mime
                        )

                    )

                )

            BASE_URL = "https://ai-ats-resume-analyzer-and-candidate.onrender.com"

            response = requests.post(

                f"{BASE_URL}/batch/parse",

                files=files,

                data={
                    "job_description": job_description
                }

            )

            # Close file handles
            for _, file_tuple in files:
                file_tuple[1].close()

            # Delete temp files
            for path in temp_files:

                if os.path.exists(path):
                    os.remove(path)

            if response.status_code == 200:

                api_data = response.json()

                results = []

                for item in api_data["results"]:

                    resume = item["data"]

                    resume["file_name"] = item["filename"]

                    resume["rank"] = item["rank"]

                    results.append(resume)

                st.session_state["results"] = results

                st.success("Ranking Completed!")

            else:

                st.error(response.text)
            

# ==========================================
# Show Ranking Results
# ==========================================

if "results" in st.session_state:

    results = st.session_state["results"]

    # Sort by ATS Score
    results.sort(
        key=lambda x: x.get("ats_score", 0),
        reverse=True
   )

    # ---------------------------------------
    # Dashboard
    # ---------------------------------------

    highest = max(r["ats_score"] for r in results)
    average = round(
        sum(r["ats_score"] for r in results) / len(results),
        2
    )

    if results:
        top_candidate = results[0].get(
            "name",
            results[0]["file_name"]
        )
    else:
        top_candidate = "No Candidate"
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📄 Total Resumes", len(results))
    col2.metric("🏆 Highest Score", f"{highest}%")
    col3.metric("📊 Average Score", f"{average}%")
    col4.metric("⭐ Top Candidate", top_candidate)

    st.divider()

    # ---------------------------------------
    # Ranking Table
    # ---------------------------------------

    table = []

    for rank, candidate in enumerate(results, start=1):

        score = candidate["ats_score"]

        if score >= 90:
            recommendation = "Strong Match"

        elif score >= 75:
            recommendation = "Good Match"

        elif score >= 60:
            recommendation = "Moderate"

        else:
            recommendation = "Needs Improvement"

        candidate["Recommendation"] = recommendation

        # Medal Icons

        if rank == 1:
            rank_display = "🥇"

        elif rank == 2:
            rank_display = "🥈"

        elif rank == 3:
            rank_display = "🥉"

        else:
            rank_display = str(rank)



        table.append({

            "Rank": rank_display,

            "Candidate": candidate.get("name", "Unknown"),
            
            "Resume":candidate["file_name"],

            "ATS Score": score,

            "Matched Skills": ", ".join(candidate["matched_skills"]),

            "Recommendation": recommendation

        })

    df = pd.DataFrame(table)

    st.subheader("🏆 Resume Ranking")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
    st.divider()

    st.subheader("📥 Download Ranking")

    col1, col2 = st.columns(2)


    # -----------------------------
    # Download CSV
    # -----------------------------

    csv = df.to_csv(index=False)

    with col1:

        st.download_button(

            label="⬇ Download Ranking CSV",

            data=csv,

            file_name="resume_ranking.csv",

            mime="text/csv"

        )

    # -----------------------------
    # Download JSON
    # -----------------------------

    json_data = json.dumps(results, indent=4)

    with col2:

        st.download_button(

            label="⬇ Download Ranking JSON",

            data=json_data,

            file_name="resume_ranking.json",

            mime="application/json"

        )

    st.divider()


    # ---------------------------------------
    # Candidate Details
    # ---------------------------------------

    st.subheader("👤 Candidate Details")

    for candidate in results:

        with st.expander(
            f"{candidate.get('name','Unknown')} ({candidate['ats_score']}%)"
        ):
            score = candidate["ats_score"]

            if score >= 90:
                st.success(f"🎯 ATS Score : {score}%")

            elif score >= 75:
                st.info(f"🎯 ATS Score : {score}%")

            elif score >= 60:
                st.warning(f"🎯 ATS Score : {score}%")

            else:
                st.error(f"🎯 ATS Score : {score}%")

            st.write("**Recommendation:**", candidate["Recommendation"])

            st.write("**Matched Skills:**", candidate["matched_skills"])

            st.divider()

            
            
            

            st.write("### 📧 Contact")

            col1, col2 = st.columns(2)

            with col1:
                st.write("📧", candidate.get("email", "Not Found"))

            with col2:
                st.write("📞", candidate.get("phone", "Not Found"))

            
            st.write("### 💻 Skills")

            skills = candidate.get("matched_skills", [])

            if skills:
                st.write(", ".join(skills))
            else:
                st.write("No skills found.")

            st.write("### 🚀 Projects")

            projects = candidate.get("projects", [])

            if projects:

                for project in projects:

                    if isinstance(project, dict):

                        title = project.get("title", "")

                        description = project.get("description", "")

                        st.markdown(f"**{title}**")

                        if description:
                            st.write(description)

                    else:

                        st.write(f"• {project}")

            else:

                st.info("No projects found.")

            st.write("### 💼 Experience")

            experience = candidate.get("experience", [])

            if experience:

                for exp in experience:

                    if isinstance(exp, dict):

                        role = exp.get("role", "")

                        company = exp.get("company", "")

                        duration = exp.get("duration", "")

                        description = exp.get("description", [])

                        if role:
                            st.markdown(f"**Role:** {role}")

                        if company:
                            st.write(f"🏢 {company}")

                        if duration:
                            st.write(f"📅 {duration}")

                        if description:

                            for point in description:
                                st.write(f"• {point}")

                        st.divider()

                    else:

                        st.write(f"• {exp}")

            else:

                st.info("No experience found.")
    # ---------------------------------------
    # Raw JSON
    # ---------------------------------------
    st.divider()
    with st.expander("📄 View Raw JSON"):
        st.json(results)