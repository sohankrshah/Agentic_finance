import streamlit as st

def render_sidebar():
    st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            background-color: rgb(14, 17, 23) !important;
        }
        input[type="text"] {
            background-color: #1e272e !important;
            color: white !important;
            border: 1px solid #00ff00 !important;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.header("🔍 Search Stock")

    sidebar_data = {
        "company_name": st.sidebar.text_input("Enter Company Name", ""),
        "show_fundamental": st.sidebar.checkbox("📊 Fundamental Data"),
        "show_technical": st.sidebar.checkbox("📈 Technical Graph"),
        "show_sentiment": st.sidebar.checkbox("💬 Sentiment Analysis"),
        "show_risks": st.sidebar.checkbox("⚠️ Risk Assessments"),
        "show_recommendation": st.sidebar.checkbox("🤖 AI Recommendations")
    }

    return sidebar_data
