import streamlit as st


st.title("This is title")


prompt = st.chat_input("What's up?")

if prompt:
	st.warning('This is a warning', icon="⚠️")
