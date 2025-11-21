import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Gemini HTML Cleaner", layout="wide")

st.title("Gemini HTML Viewer & Cleaner")

# Slider to control window split (movable boundary)
split_ratio = st.slider("Adjust Panel Size", 1, 5, 2)

left_col, right_col = st.columns([split_ratio, 5 - split_ratio])

# Session state to store outputs
if "cleaned_text" not in st.session_state:
    st.session_state.cleaned_text = ""

if "show_html" not in st.session_state:
    st.session_state.show_html = False

# ---------- LEFT PANEL ----------
with left_col:
    st.subheader("Input Panel")

    input_text = st.text_area(
        "Paste Gemini HTML Output:",
        height=300,
        placeholder="Paste Gemini HTML here..."
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Clean Text"):
            if input_text.strip():
                text = input_text.replace("\\n", "")
                text = text.replace('\\"', '"')
                st.session_state.cleaned_text = text
                st.session_state.show_html = False

    with col2:
        if st.button("Show HTML"):
            if input_text.strip():
                text = input_text.replace("\\n", "")
                text = text.replace('\\"', '"""')
                st.session_state.cleaned_text = text
                st.session_state.show_html = True


# ---------- RIGHT PANEL ----------
with right_col:
    st.subheader("Output Panel")

    # Show cleaned text with copy button
    if st.session_state.cleaned_text and not st.session_state.show_html:
        st.success("Cleaned Output (Copy Enabled)")
        st.code(st.session_state.cleaned_text, language="html")

    # Render HTML preview
    if st.session_state.show_html and st.session_state.cleaned_text:
        st.success("Rendered HTML Preview")
        components.html(
            st.session_state.cleaned_text,
            height=600,
            scrolling=True
        )
