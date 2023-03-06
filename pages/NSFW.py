import streamlit as st
import openai
import os

openai.api_key =  os.getenv("APIKEY")


src =st.text_input("Enter a message ")
# error = st.text_input("Paste your error here")
# ques = st.text_input("Ask any questions you want from this book")

if st.button("Send"):

    inpt = "Generate a sexy Reply that would trigger the user for this message : "+str(src)
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