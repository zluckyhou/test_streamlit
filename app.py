import json
import os
from urllib.parse import quote_plus, urlencode

import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# 设置Auth0的客户端ID和秘密、域以及会话秘钥
AUTH0_CLIENT_ID = st.secrets["client_id"]  # Google Client ID
AUTH0_CLIENT_SECRET = st.secrets["client_secret"]  # Google Client Secret
AUTH0_DOMAIN = st.secrets['auth_domain']
AUTH0_REDIRECT_URI = st.secrets['redirect_url']
# SESSION_SECRET_KEY = os.getenv("APP_SECRET_KEY")

# Initialize OAuth session
oauth = OAuth2Session(
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    scope="openid profile email",
    redirect_uri=AUTH0_REDIRECT_URI
)

auth0_metadata_url = f'https://{AUTH0_DOMAIN}/.well-known/openid-configuration'
oauth.load_server_metadata(auth0_metadata_url)

# Streamlit app
st.title("Auth0 Login with Streamlit")

if "user" not in st.session_state:
    st.session_state["user"] = None

def login():
    authorization_url, state = oauth.create_authorization_url(
        f'https://{AUTH0_DOMAIN}/authorize'
    )
    st.session_state["oauth_state"] = state
    st.write(f"### [Login with Auth0]({authorization_url})")

def logout():
    st.session_state["user"] = None
    st.write("You have been logged out.")

def callback():
    if "code" in st.experimental_get_query_params():
        token = oauth.fetch_token(
            f'https://{AUTH0_DOMAIN}/oauth/token',
            authorization_response=st.experimental_get_query_params()["code"],
            code=st.experimental_get_query_params()["code"]
        )
        userinfo = oauth.get(f'https://{AUTH0_DOMAIN}/userinfo').json()
        st.session_state["user"] = userinfo

if st.session_state["user"]:
    st.write(f"Hello, {st.session_state['user']['name']}!")
    st.button("Logout", on_click=logout)
else:
    login()

if "code" in st.experimental_get_query_params():
    callback()
