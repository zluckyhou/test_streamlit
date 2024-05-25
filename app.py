import json
import os
from urllib.parse import quote_plus, urlencode

import streamlit as st
from authlib.integrations.base_client import RemoteApp
from authlib.integrations.requests_client import OAuth2Session
from dotenv import load_dotenv

load_dotenv()

# AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
# AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
# AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
# AUTH0_REDIRECT_URI = os.getenv("AUTH0_REDIRECT_URI")
# AUTH0_LOGOUT_REDIRECT_URI = os.getenv("AUTH0_LOGOUT_REDIRECT_URI")

AUTH0_CLIENT_ID = st.secrets["client_id"]  # Google Client ID
AUTH0_CLIENT_SECRET = st.secrets["client_secret"]  # Google Client Secret
AUTHORIZE_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
# TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
# REVOKE_ENDPOINT = "https://oauth2.googleapis.com/revoke"
AUTH0_DOMAIN = st.secrets['auth_domain']
AUTH0_REDIRECT_URI = st.secrets["redirect_url"]
AUTH0_LOGOUT_REDIRECT_URI = st.secrets["redirect_url"]

# Initialize Auth0 app
auth0 = RemoteApp(
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    api_base_url=f"https://{AUTH0_DOMAIN}",
    authorize_url=f"https://{AUTH0_DOMAIN}/authorize",
    authorize_params=None,
    access_token_url=f"https://{AUTH0_DOMAIN}/oauth/token",
    access_token_params=None,
    refresh_token_url=None,
    redirect_uri=AUTH0_REDIRECT_URI,
    client_kwargs={"scope": "openid profile email"},
)

# Streamlit app
st.title("Auth0 Login Example")

# Login button
login_button = st.button("Login")

if login_button:
    redirect_uri = auth0.authorize_redirect(redirect_uri=AUTH0_REDIRECT_URI)
    st.write(f'<a href="{redirect_uri}" target="_self">Redirect to Auth0 Login</a>', unsafe_allow_html=True)

# Fetch the token and user info
query_params = st.experimental_get_query_params()
code = query_params.get("code", [None])[0]

if code:
    token = auth0.authorize_access_token(code=code, redirect_uri=AUTH0_REDIRECT_URI)
    user_info = auth0.get("userinfo", token=token).json()
    st.write("User Info:", json.dumps(user_info, indent=4))

    # Logout button
    logout_button = st.button("Logout")
    if logout_button:
        params = {
            "returnTo": AUTH0_LOGOUT_REDIRECT_URI,
            "client_id": AUTH0_CLIENT_ID,
        }
        logout_url = f"https://{AUTH0_DOMAIN}/v2/logout?" + urlencode(params, quote_via=quote_plus)
        st.write(f'<a href="{logout_url}" target="_self">Logout</a>', unsafe_allow_html=True)
