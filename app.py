import streamlit as st


prompt = st.chat_input("What's up?")

if prompt:
	st.warning('This is a warning', icon="⚠️")
