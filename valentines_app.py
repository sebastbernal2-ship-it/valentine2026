import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Get the directory where this script is located
current_dir = Path(__file__).parent

# Full path to HTML file
html_path = current_dir / "valentines.html"

# Read and display
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=800, scrolling=True)
