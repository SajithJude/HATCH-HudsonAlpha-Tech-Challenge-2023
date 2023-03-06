import streamlit as st
from streamlit.components.v1 import html

# Define the HTML for the top navigation menu
top_menu = """
<div style="background: linear-gradient(to right, #9C27B0, #E040FB); padding: 10px;">
    <span style="color: white; font-size: 30px;">Glassmorphism Page</span>
</div>
"""

# Define the HTML for the sidebar
sidebar = """
<div style="background: linear-gradient(to bottom, #9C27B0, #E040FB); padding: 10px;">
    <span style="color: white; font-size: 20px;">Sidebar</span>
</div>
"""

# Define the HTML for the glassmorphism card
card = """
<div style="background: linear-gradient(to bottom right, #9C27B0, #E040FB); border-radius: 20px; padding: 20px;">
    <div style="display: flex; flex-direction: row; justify-content: space-between; margin-bottom: 20px;">
        <div style="background: linear-gradient(to bottom, #FF6B6B, #FFC107); border-radius: 20px; padding: 20px; margin-right: 10px;">
            <span style="color: white; font-size: 20px;">Column 1</span>
        </div>
        <div style="background: linear-gradient(to bottom, #64B5F6, #00E676); border-radius: 20px; padding: 20px; margin-left: 10px;">
            <span style="color: white; font-size: 20px;">Column 2</span>
        </div>
    </div>
    <div style="background: rgba(255, 255, 255, 0.5); backdrop-filter: blur(5px); border-radius: 10px; padding: 20px; color: #000;">
        <h2 style="text-align: center;">Main Tab Card</h2>
        <p>Content goes here</p>
    </div>
</div>
"""

# Define the HTML for the main tab
main_tab = """
<div style="padding: 20px;">
    <span style="font-size: 20px;">Main Tab Content</span>
    <br><br>
    <div style="display: flex; flex-direction: row;">
        <div style="flex: 1; margin-right: 10px;">""" + card + """</div>
        <div style="flex: 1;">""" + card + """</div>
    </div>
</div>
"""

# Define the HTML for the entire page
page = """
<div>
    """ + top_menu + """
    <div style="display: flex; flex-direction: row;">
        <div style="flex: 1;">""" + sidebar + """</div>
        <div style="flex: 4;">""" + main_tab + """</div>
    </div>
</div>
"""

# Render the HTML using the components API
html_component = html(page)
st.components.v1.html(html_component)
