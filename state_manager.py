import streamlit as st


def init_state():
    if "cleaned_text" not in st.session_state:
        st.session_state.cleaned_text = ""


    if "show_html" not in st.session_state:
        st.session_state.show_html = False