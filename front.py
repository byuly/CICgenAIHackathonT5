import streamlit as st

st.set_page_config(page_title="Streamlit Demo") #HTML title
st.title("T5ChatBot") #page title

color_text = st.text_input("Question:") #display a text box
go_button = st.button("Go", type="primary") #display a primary buttonv

if go_button: #code in this if block will be run when the button is clicked

    st.write(f"jun also asked{color_text} too!") #display the response content

st.image("cat.png")