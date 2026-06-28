import streamlit as st

st.set_page_config(
    page_title="ATS Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 ATS Resume Analyzer")

st.write("""
Welcome!

Use the sidebar.

📄 Resume Analyzer

🏆 Resume Ranking
""")

st.sidebar.title("About")
st.sidebar.info(
    """🚀 AI-Powered ATS Resume Analyzer & Smart Candidate Ranking System

📄 Analyze • 🎯 Score • 📊 Rank • ⚡ Hire Smarter
🧠 Built with Machine Learning & Python
👨‍💻 Developed with ❤️ By ~ DIWAKAR KUSHWAHA"""
    
)