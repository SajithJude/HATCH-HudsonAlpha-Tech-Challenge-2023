# import streamlit as st
import openai
import os

openai.api_key =  os.getenv("APIKEY")

import streamlit as st

style = """
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
    """
divstyle = """
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

st.markdown(style,
    unsafe_allow_html=True
)

with st.container():
    st.markdown("<h1 style='text-align:center'>Glassmorphism Card</h1>", unsafe_allow_html=True)
    form = st.markdown(divstyle,
        unsafe_allow_html=True
    )
    # submit_button = divstyle.find("#submit-button")
    # if submit_button.button.clicked:
    input_text = divstyle.find("#input-text").text_input()
    st.write(input_text)