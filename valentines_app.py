import streamlit as st
import streamlit.components.v1 as components

# Read the HTML file
with open('valentines.html', 'r') as f:
    html_content = f.read()

# Display the HTML
components.html(html_content, height=800, scrolling=True)
