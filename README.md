📄 AI ATS Resume Analyzer & Candidate Ranking System

An AI-powered Applicant Tracking System (ATS) that parses resumes, evaluates candidates against job descriptions, calculates ATS scores, and ranks multiple applicants using Machine Learning and NLP.

📌 Project Overview

Recruiters often receive hundreds of resumes for a single job opening. Manually screening them is time-consuming and inconsistent.

This project automates the recruitment process by:

Parsing resumes (PDF/DOCX)
Extracting candidate information
Matching resumes with Job Descriptions
Calculating ATS Match Scores
Ranking multiple candidates
Exporting results as JSON and CSV
✨ Features
Resume Parsing
PDF Resume Support
DOCX Resume Support
Automatic Text Extraction
Resume Cleaning
Information Extraction
Name
Email
Phone Number
LinkedIn
GitHub
Portfolio
Skills
Education
Experience
Projects
Certifications
Languages
ATS Scoring
Job Description Matching
Skill Matching
ATS Percentage Score
Missing Skill Detection
Candidate Ranking
Upload Multiple Resumes
Automatic Ranking
Highest Score Detection
Candidate Recommendation
Export Options
JSON Export
CSV Export
User Interface
Streamlit Dashboard
FastAPI Backend
Interactive Progress Bar
Download Reports
🏗️ Project Architecture
                User
                  │
                  ▼
        Streamlit Frontend
                  │
        REST API (HTTP Requests)
                  │
                  ▼
           FastAPI Backend
                  │
      Resume Parsing Pipeline
                  │
 ┌───────────────┼───────────────┐
 │               │               │
 ▼               ▼               ▼
Text        Information      ATS Score
Extraction   Extraction      Calculation
 │               │               │
 └───────────────┼───────────────┘
                 ▼
          Candidate Ranking
                 ▼
          JSON / CSV Export
📂 Folder Structure
AI-ATS-Resume-Analyzer-and-Candidate-Ranking-System
│
├── backend/
│   ├── main.py
│   ├── routes.py
│   └── routers/
│
├── parser/
│   ├── extractor.py
│   ├── cleaner.py
│   ├── regex_extractor.py
│   ├── section_parser.py
│   ├── skill_extractor.py
│   ├── ner_extractor.py
│   ├── ats_scorer.py
│   ├── validator.py
│   ├── exporter.py
│   ├── jd_matcher.py
│   └── parser.py
│
├── pages/
│   ├── Resume_Analyzer.py
│   └── Resume_Ranking.py
│
├── data/
│
├── output/
│
├── Home.py
├── requirements.txt
├── runtime.txt
└── README.md
⚙️ Tech Stack
Programming Language
Python
Backend
FastAPI
Uvicorn
Frontend
Streamlit
Machine Learning
Scikit-learn
Joblib
NLP
spaCy
Regex
Data Processing
Pandas
NumPy
Resume Parsing
PDFMiner
python-docx
Visualization
Plotly
Deployment
GitHub
Render
Streamlit Community Cloud

🌐 Live Demo
Frontend (Streamlit)
https://ai-ats-resume-analyzer-and-candidate-ranking-system-5csafpcr4p.streamlit.app/
Backend API (Render)
Paste Your Render URL Here
GitHub Repository
Paste Your GitHub Repository URL Here
📸 Screenshots

Add screenshots for:

🏠 Home Page
📄 Resume Analyzer
🎯 ATS Score
🏆 Resume Ranking
📊 Dashboard
📥 JSON Export
📄 CSV Export

Example:

screenshots/
│
├── home.png
├── analyzer.png
├── ranking.png
├── ats_score.png
└── dashboard.png
📈 Workflow
Upload Resume
      │
      ▼
Extract Text
      │
      ▼
Clean Resume
      │
      ▼
Extract Information
      │
      ▼
Extract Skills
      │
      ▼
Compare with JD
      │
      ▼
Calculate ATS Score
      │
      ▼
Rank Candidates
      │
      ▼
Export Results
🔮 Future Improvements
AI-powered resume improvement suggestions
LLM-based semantic matching
Authentication (JWT)
Database integration (SQLite/PostgreSQL)
Recruiter dashboard
Interview scheduling
Email notifications
Docker support
GitHub Actions (CI/CD)
Advanced analytics and reports
👨‍💻 Author

Diwakar Kushwaha

🎓 Computer Science Student
💻 AI/ML & Python Developer
🚀 Passionate about Machine Learning, NLP, and Full-Stack Development
📄 License

This project is licensed under the MIT License.

⭐ Support

If you found this project helpful, consider starring ⭐ the repository and sharing it with others. Contributions, suggestions, and feedback are always welcome!
