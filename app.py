import streamlit as st


with st.sidebar:
	st.markdown("# test sidebar layout")
	option = st.selectbox(
    "Select GPT model",
    ("gpt-4o", "gpt-4-0613", "Mobile phone"))



st.title("This is title")
st.write(f"Your option: {option}")

st.markdown("[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/J3J3YMOKZ)")

st.markdown("[![ko-fi](https://wbucijybungpjrszikln.supabase.co/storage/v1/object/public/chatgpt-4o-files/kofi_button_red.png)](https://ko-fi.com/J3J3YMOKZ)")

st.link_button(":red-background[Support me on ko-fi]","https://ko-fi.com/J3J3YMOKZ")

st.markdown("[![ko-fi](https://wbucijybungpjrszikln.supabase.co/storage/v1/object/public/chatgpt-4o-files/kofi_button_red_1.png)](https://ko-fi.com/J3J3YMOKZ)")

prompt = st.chat_input("What's up?")

# if prompt:
# 	with st.chat_message("assistant"):
# 		st.warning('This is a warning', icon=":material/passkey:")
		
# 		st.error('This is an error', icon="🚨")
# 		st.markdown("After warning text")
		

# video_placeholder = st.empty()

# with video_placeholder:
# 	st.markdown("test video placeholder")

# if st.button('test placeholder'):
# 	with video_placeholder:
# 		st.markdown("video placeholder changed!")


import subprocess
from st_audiorec import st_audiorec
import os
# def record_and_display():
# 	with st.container(border=True):
# 		wav_audio_data = st_audiorec()

# 		output_path = 'record_audios'
# 		# remove directory if exists 
# 		rm_user_directory = subprocess.run(["rm","-rf",output_path],check=True)
# 		mkdir_user_directory = subprocess.run(["mkdir","-p",output_path],check=True)

# 		output_file_path = os.path.join(output_path,"record_audio.mp3")
		

# 		if wav_audio_data is not None:
# 			st.markdown(f"wav_audio_data: {wav_audio_data}")

# 			st.audio(wav_audio_data, format='audio/wav')
# 			with open(output_file_path,'wb') as f:
# 				f.write(wav_audio_data)
# 			st.markdown(output_file_path)
# 			st.audio(output_file_path)

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
	st.markdown(f"wav_audio_data: {wav_audio_data}")

	st.audio(wav_audio_data, format='audio/wav')
