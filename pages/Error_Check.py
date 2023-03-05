import streamlit as st
import openai
import os

openai.api_key =  os.getenv("APIKEY")

use =st.text_input("What Was this code Supposed to do ?")
code =st.text_input("Paste your code here")
error = st.text_input("Paste your error here")
language = st.text_input("Specify programming language")

if st.button("Error Check and Fix :"):

    inpt = "Fix the issue with the following code written in  "+ str(language) + " language ." + "The purpose of the code is to :" + str(use)+ " ."+ "The error that showed was :"+ str(error)
    st.write(inpt)

    outpt = openai.Completion.create(
                                        engine="text-davinci-003",
                                        prompt=inpt,
                                        max_tokens=3600,
                                        n=1,
                                        stop=None,
                                        temperature=0.5,
                                        )
    explan= outpt.choices[0].text.strip()
    st.code(explan)
    st.stop()