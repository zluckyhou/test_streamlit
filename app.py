import json
import os
from urllib.parse import quote_plus, urlencode

import streamlit as st
from streamlit_oauth import OAuth2Component
import base64




# create an OAuth2Component instance
CLIENT_ID = st.secrets["client_id"]  # Google Client ID
CLIENT_SECRET = st.secrets["client_secret"]  # Google Client Secret
AUTHORIZE_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
REVOKE_ENDPOINT = "https://oauth2.googleapis.com/revoke"
REDIRECT_URL = st.secrets["redirect_url"]

with st.sidebar:
	st.markdown("# Test login")
	# login module
	if "auth" not in st.session_state:
		# create a button to start the OAuth2 flow
		oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_ENDPOINT, TOKEN_ENDPOINT, TOKEN_ENDPOINT, REVOKE_ENDPOINT)
		result = oauth2.authorize_button(
			name="Continue with Google",
			icon="https://www.google.com.tw/favicon.ico",
			redirect_uri=REDIRECT_URL,
			scope="openid email profile",
			key="google",
			extras_params={"prompt": "consent", "access_type": "offline"},
			use_container_width=True,
			pkce='S256',
		)
	
		
		if result:
			# Customize the button using the injected CSS class
			# CSS for Google login button
			logger.info(f"oauth result: {result}")
			google_button_css = """
				background-color: #4285f4;
				color: white;
				border: none;
				border-radius: 4px;
				padding: 8px 20px;
				font-family: Roboto, sans-serif;
				font-size: 14px;
				box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
				cursor: pointer;
				display: flex;
				align-items: center;
				text-decoration: none;
			""".replace("\n", " ") 
			
			st.markdown(f"""
				<a href="{result}" style="{google_button_css}">
					<img src="https://www.google.com.tw/favicon.ico" style="margin-right: 8px; width:20px; height:20px">
					Continue with Google
				</a>
			""", unsafe_allow_html=True)
			# st.write(result)
	
			# decode the id_token jwt and get the user's email address
			id_token = result["token"]["id_token"]
			# verify the signature is an optional step for security
			payload = id_token.split(".")[1]
			# add padding to the payload if needed
			payload += "=" * (-len(payload) % 4)
			payload = json.loads(base64.b64decode(payload))
			name = payload["name"]
			email = payload["email"]
			st.session_state["user_profile"] = payload
			logger.info(f"user profile: {payload}")
			st.session_state["name"] = name
			st.session_state["auth"] = email
			st.session_state["token"] = result["token"]
			st.rerun()									
	else:
		st.write(f"Welcome {st.session_state['name']}")
		# st.write(st.session_state["auth"])
		# st.write(st.session_state["token"])
		if st.button("Logout"):
			del st.session_state["auth"]
			del st.session_state["token"]

