import streamlit as st


code =st.text_input("Paste your code here")
# error = st.text_input("Paste your error here")
language = st.text_input("Specify programming language")

if st.button("Error Check and Fix :"):

    inpt = "Find whats wrong the following code written in  "+ str(language) + " language ." + "Fix any errors in the code if present or make it better :" +  str(code)
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
    st.write(explan)
    st.stop()