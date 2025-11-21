import streamlit as st
from left_ui import render_left_panel
from right_ui import render_right_panel
from state_manager import init_state


st.set_page_config(page_title="Gemini HTML Cleaner", layout="wide")
st.title("Gemini HTML Viewer & Cleaner")


init_state()


split_ratio = st.slider("Adjust Panel Size", 1, 5, 2)
left_col, right_col = st.columns([split_ratio, 5 - split_ratio])


with left_col:
    render_left_panel()


with right_col:
    render_right_panel()