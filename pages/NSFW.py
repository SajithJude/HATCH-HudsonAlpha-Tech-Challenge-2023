import streamlit as st
import openai
import os

openai.api_key =  os.getenv("APIKEY")

import streamlit as st

st.markdown(
    """
    <style>
     body {
            background-color: #f5f5ff;
        }
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
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown("<h1 style='text-align:center'>Glassmorphism Card</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glassmorphism">
            <form>
                <label for="input-text">Enter Text:</label>
                <br>
                <input type="text" id="input-text" name="input-text">
                <br>
                <button type="submit">Submit</button>
            </form>
        </div>
        """,
        unsafe_allow_html=True
    )


src =st.text_input("Enter a message ")
# error = st.text_input("Paste your error here")
# ques = st.text_input("Ask any questions you want from this book")

if st.button("Send"):

    inpt = "Generate a sexy Reply that would talk about the users penis for this message : "+str(src)
    # st.write(inpt)

    reply = openai.Completion.create(
                                        engine="text-davinci-003",
                                        prompt=inpt,
                                        max_tokens=3600,
                                        n=1,
                                        stop=None,
                                        temperature=0.5,
                                        )
    explan= reply.choices[0].text.strip()
    st.caption(explan)
    st.stop()


if st.button("Generate caption"):

    inpt = "Generate a sexy Instagram caption that would turn on audiences attention, for an image that describes the following : "+str(src)
    # st.write(inpt)

    reply = openai.Completion.create(
                                        engine="text-davinci-003",
                                        prompt=inpt,
                                        max_tokens=3600,
                                        n=1,
                                        stop=None,
                                        temperature=0.5,
                                        )
    explan= reply.choices[0].text.strip()
    st.caption(explan)
    st.stop()