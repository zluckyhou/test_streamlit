import streamlit as st


with st.sidebar:
	st.markdown("# test sidebar layout")



st.title("This is title")

st.markdown("[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/J3J3YMOKZ)")


prompt = st.chat_input("What's up?")

if prompt:
	with st.chat_message("assistant"):
		st.warning('This is a warning', icon=":material/passkey:")
		
		st.error('This is an error', icon="🚨")
		st.markdown("After warning text")
