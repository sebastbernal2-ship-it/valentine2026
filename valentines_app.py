import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Will You Be My Valentine? 💕",
    page_icon="💖",
    layout="centered"
)

current_dir = Path(__file__).parent
html_path = current_dir / "valentines.html"

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=800, scrolling=False)
