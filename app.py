import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
import os

# Google OAuth 配置
CLIENT_ID = st.secrets["client_id"]  # Google Client ID
CLIENT_SECRET = st.secrets["client_secret"]  # Google Client Secret
AUTHORIZE_URL = 'https://accounts.google.com/o/oauth2/auth'
TOKEN_URL = 'https://oauth2.googleapis.com/token'
REDIRECT_URI = st.secrets["redirect_url"]  # 确保这与你在Google Cloud Platform中设置的相匹配

# 创建OAuth2会话对象
def create_oauth_session(state=None):
    return OAuth2Session(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        authorization_endpoint=AUTHORIZE_URL,
        token_endpoint=TOKEN_URL,
        redirect_uri=REDIRECT_URI,
        scope='openid email profile',
        state=state
    )



# 处理OAuth回调
def auth_callback():
    if 'code' in st.query_params():
        oauth_session = create_oauth_session(state=st.session_state['oauth_state'])
        code = st.query_params()['code'][0]
        token = oauth_session.fetch_token(TOKEN_URL, code=code, include_client_id=True)
        st.session_state['auth_token'] = token


if 'code' in st.query_params():
    auth_callback()


st.title('Google 登录示例')

if 'auth_token' not in st.session_state:
    # 创建OAuth会话并生成授权URL
    oauth_session = create_oauth_session()
    authorize_url, state = oauth_session.create_authorization_url(AUTHORIZE_URL)
    st.session_state['oauth_state'] = state
    st.markdown(f'<a href="{authorize_url}" target="_self">使用Google登录</a>', unsafe_allow_html=True)
else:
    # 使用OAuth令牌获取用户信息
    oauth_session = create_oauth_session(state=st.session_state['oauth_state'])
    oauth_session.token = st.session_state['auth_token']
    resp = oauth_session.get('https://www.googleapis.com/oauth2/v1/userinfo')
    user_info = resp.json()
    st.write(f'Hi {user_info["name"]}!')

    if st.button('Logout'):
        st.session_state.pop('auth_token', None)


