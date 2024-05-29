import streamlit as st


with st.sidebar:
	st.markdown("# test sidebar layout")
	option = st.selectbox(
    "Select GPT model",
    ("gpt-4o", "gpt-4-0613", "Mobile phone"))



st.title("This is title")
st.write(f"Your option: {option}")

st.markdown("[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/J3J3YMOKZ)")


prompt = st.chat_input("What's up?")

if prompt:
	with st.chat_message("assistant"):
		st.warning('This is a warning', icon=":material/passkey:")
		
		st.error('This is an error', icon="🚨")
		st.markdown("After warning text")
		
