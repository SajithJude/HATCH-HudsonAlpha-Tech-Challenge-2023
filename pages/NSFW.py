# import streamlit as st
import openai
import os

openai.api_key =  os.getenv("APIKEY")
import streamlit as st
import streamlit.components.v1 as components

def glassmorphism_card():
    html_str = """
    <style>
        .glassmorphism {
            background: rgba(255, 255, 255, 0.5);
            backdrop-filter: blur(5px);
            border-radius: 10px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            color: #000;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 300px;
            width: 500px;
            margin: auto;
        }
        .glassmorphism input[type=text] {
            width: 80%;
            padding: 12px 20px;
            margin: 8px 0;
            box-sizing: border-box;
            border: 2px solid #ccc;
            border-radius: 4px;
            background-color: #f8f8f8;
            font-size: 16px;
        }
        .glassmorphism button[type=submit] {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 16px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;
        }
    </style>
    <div class="glassmorphism">
        <form>
            <label for="input-text">Enter Text:</label>
            <br>
            <input type="text" id="input-text" name="input-text">
            <br>
            <button type="submit">Submit</button>
        </form>
    </div>
    """
    return html_str

components.html(glassmorphism_card(), height=400)
if st.form_submit_button():
    input_text = st.text_input("Enter Text")
    st.write(f"You entered: {input_text}")
