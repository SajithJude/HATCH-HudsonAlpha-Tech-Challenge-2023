import streamlit as st
import pandas as pd
import openai
import os 

st.markdown(
    """
    <style>
    body {
        background-image: linear-gradient(to bottom right, #00ffff, #ff00ff);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add your Streamlit app code here

st.markdown("# 4-1 ai chatbot gpt 3 based IT website")
st.markdown("""
    
#### Click on the arrow icon on the top left to trigger menu
#### Error Check :
    # Allows you to Paste your code and input which programming language that was used
    # If Errors Found in code, It will fix the error, if not, It will modify the code to make it efficient 
#### CS Dissertation
    # Allows you to Paste Reference URLs of Publications(around 4 atm) 
    # Will analyze the entire publication and generate a paragraph for Literature review, Novelity, Citations, ect..
#### Knowledge From Books:
    # Allows you to paste URL of any books
    # Will Reply to any questions, where the answers will be based on the information on the book 

""")
