import streamlit as st
import streamlit.components.v1 as components




def render_right_panel():
    st.subheader("Output Panel")


    if st.session_state.cleaned_text and not st.session_state.show_html:
        st.success("Cleaned Output (Copy Enabled)")
        st.code(st.session_state.cleaned_text, language="html")


    if st.session_state.show_html and st.session_state.cleaned_text:
        st.success("Rendered HTML Preview")
        components.html(
        st.session_state.cleaned_text,
        height=600,
        scrolling=True
    )