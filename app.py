import streamlit as st
import numpy as np
import random
import time
from PIL import Image
import os
import mimetypes
from supabase import create_client, Client, StorageException
from io import StringIO, BytesIO
from tempfile import NamedTemporaryFile
import json
import requests


# check if image
def is_image(file_path):
	try:
		Image.open(file_path)
		return True
	except IOError:
		return False

def get_supabase_client():
	url = st.secrets['supabase_url']
	key = st.secrets['supabase_key']
	supabase = create_client(url, key)
	return supabase

# insert data to database
def supabase_insert_message(user_message,response_content,messages,content_type,service_channel):
    supabase = get_supabase_client()
    data, count = supabase.table('messages').insert({"user_message": user_message, "response_content": response_content,"messages":messages,"content_type":content_type,"service_channel":service_channel}).execute()

def supabase_insert_user(name,user_name,profile,picture,oauth_token):
    supabase = get_supabase_client()
    data, count = supabase.table('users').insert({"name":name,"user_name":user_name,"profile":profile,"picture":picture,"oauth_token":oauth_token}).execute()


def supabase_fetch_user(user_name):
    supabase = get_supabase_client()
    data,count = supabase.table('users').select("*").eq('user_name',user_name).execute()
    return data
        

# check if file already exists
def check_supabase_file_exists(file_path):
	supabase = get_supabase_client()
	bucket_name = st.secrets["bucket_name"]
	supabase_storage_ls = supabase.storage.from_(bucket_name).list()
	
	if any(file["name"] == os.path.basename(file_path) for file in supabase_storage_ls):
		return True
	else:
		return False


def upload_file_to_supabase_storage(file_obj):
	base_name = os.path.basename(file_obj.name)
	path_on_supastorage = os.path.splitext(base_name)[0] + '_' + str(round(time.time())//6000)  + os.path.splitext(base_name)[1]
	mime_type, _ = mimetypes.guess_type(file_obj.name)
	
	supabase = get_supabase_client()
	bucket_name = st.secrets["bucket_name"]
	
	bytes_data = file_obj.getvalue()
	with NamedTemporaryFile(delete=False) as temp_file:
		temp_file.write(bytes_data)
		temp_file_path = temp_file.name
	
	try:
		with open(temp_file_path, "rb") as f:
			if check_supabase_file_exists(path_on_supastorage):
				public_url = supabase.storage.from_(bucket_name).get_public_url(path_on_supastorage)
			else:
				supabase.storage.from_(bucket_name).upload(file=temp_file_path, path=path_on_supastorage, file_options={"content-type": mime_type})
				public_url = supabase.storage.from_(bucket_name).get_public_url(path_on_supastorage)
	except StorageException as e:
		print("StorageException:", e)
		raise
	finally:
		os.remove(temp_file_path)  # Ensure the temporary file is removed
	
	return public_url





# Initialize file uploader
if 'uploaded_file' not in st.session_state:
	st.session_state.uploaded_file = None

# upload file
with st.sidebar:
	about = """
	# ChatGPT-4o
	
	This is GPT-4o, **totally free** for now!
	
	You can use the text and image capabilities now. More capabilities like audio and video will be rolled out iteratively in the future. Stay tuned.
	"""
	st.markdown(about)

	st.divider()

	st.markdown("**Buy me a coffee:rose::rose::rose:**")
	st.image(["https://wbucijybungpjrszikln.supabase.co/storage/v1/object/public/chatgpt-4o/Buy%20Me%20a%20Coffe-qrcode_2860875.png","https://wbucijybungpjrszikln.supabase.co/storage/v1/object/public/chatgpt-4o/_____20240524133837_1.png"],caption=["Paypal","Wechat"])
	st.divider()

	# file uploader
	st.markdown("**Upload image to your chat.**")
	file_uploader_key = str(st.session_state.get('file_uploader_key', ''))
	uploaded_file = st.file_uploader("Upload File", key=file_uploader_key)
	if uploaded_file is not None:
		# display filename
		# st.write("Filename:", uploaded_file.name)
		st.session_state.uploaded_file = uploaded_file
		if uploaded_file.type.startswith("image/"):
			st.image(uploaded_file)
		st.session_state['file_uploader_key'] = st.session_state.get('file_uploader_key', '') + 'new'


prompt = st.chat_input("What is up?")

# React to user input
if prompt:
	# Display user message in chat message container
	with st.chat_message("user"):
		st.markdown(prompt)
	# if uploaded image, display in message list and remove from sidebar
	if st.session_state.uploaded_file and st.session_state.uploaded_file.type.startswith("image/"):
		public_url = upload_file_to_supabase_storage(st.session_state.uploaded_file)
		st.image(public_url)
		st.session_state.uploaded_file = None


