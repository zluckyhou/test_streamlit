import streamlit as st


with st.sidebar:
	st.markdown("# test sidebar layout")



st.title("This is title")

st.html("""
<script src='https://storage.ko-fi.com/cdn/scripts/overlay-widget.js'></script>
<script>
  kofiWidgetOverlay.draw('chatgpt4o', {
    'type': 'floating-chat',
    'floating-chat.donateButton.text': 'Support me',
    'floating-chat.donateButton.background-color': '#fcbf47',
    'floating-chat.donateButton.text-color': '#323842'
  });
</script>
"""
)


prompt = st.chat_input("What's up?")

if prompt:
	with st.chat_message("assistant"):
		st.warning('This is a warning', icon=":material/passkey:")
		
		st.error('This is an error', icon="🚨")
		st.markdown("After warning text")
