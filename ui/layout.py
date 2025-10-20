import streamlit as st

def render_header():
    col1, col2 = st.columns([1, 13])
    with col1:
        st.image("Images/logoo.png", width=80)
    with col2:
        st.markdown("""
            <h2 style='margin-top: -10px;'>KARTS  Stock Analysis</h2>
        """, unsafe_allow_html=True)

def apply_dark_theme():
    st.markdown("""
        <style>
            body { background-color: #0e1117; color: #ffffff; }
            .stApp { background-color: #0e1117; }
            h2, h3, .markdown-text-container { color: #ffffff !important; }
        </style>
    """, unsafe_allow_html=True)
