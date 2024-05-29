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


import subprocess
import os

# 启动 FastAPI 应用
subprocess.Popen(["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"])

# Streamlit 应用
st.title("Ko-fi to Discord Webhook Integration")
st.write("This app is configured to receive Ko-fi webhooks and send notifications to a Discord channel.")

st.markdown("## Setup Instructions")
st.markdown("""
1. Set the Discord Webhook URL in your environment variables as `DISCORD_WEBHOOK_URL`.
2. Configure Ko-fi to send webhooks to `https://your-streamlit-app-url.streamlitapp.com/webhook`.
3. Ensure your Streamlit app is running and accessible via HTTPS.
""")
