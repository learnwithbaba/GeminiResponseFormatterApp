import streamlit as st
from text_utils import clean_html_text




def render_left_panel():
    st.subheader("Input Panel")


    input_text = st.text_area(
    "Paste Gemini HTML Output:",
    height=300,
    placeholder="Paste Gemini HTML here..."
    )


    btn_col1, btn_col2 = st.columns(2)


    with btn_col1:
        if st.button("Clean Text") and input_text.strip():
            st.session_state.cleaned_text = clean_html_text(input_text)
            st.session_state.show_html = False


    with btn_col2:
        if st.button("Show HTML") and input_text.strip():
            st.session_state.cleaned_text = clean_html_text(input_text)
            st.session_state.show_html = True