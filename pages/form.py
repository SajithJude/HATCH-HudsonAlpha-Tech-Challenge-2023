import streamlit as st
from streamlit.components.v1 import html

# Define the HTML template for the glassmorphism card
html_template = """
<div style="background: rgba(255, 255, 255, 0.5);
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
            margin: auto;">
    <form>
        <label for="input-text" style="font-size: 24px;">Enter Text:</label>
        <br>
        <input type="text" id="input-text" name="input-text" style="width: 80%;
            padding: 12px 20px;
            margin: 8px 0;
            box-sizing: border-box;
            border: 2px solid #ccc;
            border-radius: 4px;
            background-color: #f8f8f8;
            font-size: 16px;">
        <br>
        <button type="submit" style="background-color: #4CAF50;
            border: none;
            color: white;
            padding: 16px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 4px;">Submit</button>
    </form>
</div>
"""

# Define the callback function for when the form is submitted
def on_submit(input_text):
    st.write(f"You entered: {input_text}")

# Render the glassmorphism card with the text input field
html_result = html_template.format()
form = html(html_result)

# Get the input field element and register a callback for when the form is submitted
input_field = form.find("#input-text")
submit_button = form.find("button")
submit_button.set_event_handler("click", lambda _: on_submit(input_field.value))

# Display the card
st.markdown("<h1 style='text-align:center'>Glassmorphism Card with Text Input Field</h1>", unsafe_allow_html=True)
st.components.v1.html(html_result)
