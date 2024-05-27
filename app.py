import streamlit as st


with st.sidebar:
	st.markdown("# test sidebar layout")



st.title("This is title")


prompt = st.chat_input("What's up?")

if prompt:
	st.warning('This is a warning', icon="⚠️")
	st.error('This is an error', icon="🚨")
	st.markdown("After warning text")
