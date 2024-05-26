import streamlit as st
from authlib.integrations.requests_client import OAuth2Session
import os

# Google OAuth 配置
CLIENT_ID = st.secrets["client_id"]  # Google Client ID
CLIENT_SECRET = st.secrets["client_secret"]  # Google Client Secret
AUTHORIZE_URL = 'https://accounts.google.com/o/oauth2/auth'
TOKEN_URL = 'https://oauth2.googleapis.com/token'
REDIRECT_URI = st.secrets["redirect_url"]  # 确保这与你在Google Cloud Platform中设置的相匹配

import streamlit as st
from authlib.integrations.requests_client import OAuth2Session

# 使用Streamlit的秘密管理获取配置
AUTH0_CLIENT_ID = st.secrets["client_id"]
AUTH0_CLIENT_SECRET = st.secrets["client_secret"]
AUTH0_DOMAIN = st.secrets["auth_domain"]
AUTH0_BASE_URL = f'https://{AUTH0_DOMAIN}'
AUTH0_CALLBACK_URL = st.secrets["redirect_url"]

# 创建OAuth会话
oauth = OAuth2Session(client_id=AUTH0_CLIENT_ID, client_secret=AUTH0_CLIENT_SECRET, scope='openid profile email', redirect_uri=AUTH0_CALLBACK_URL)

# 定义获取token的函数
def get_token():
    return st.session_state.get("token", {})

# 定义保存token的函数
def set_token(token):
    st.session_state["token"] = token

# 定义清除session的函数
def clear_session():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# 登录页面
def login():
    auth_url, state = oauth.create_authorization_url(AUTH0_BASE_URL + '/authorize')
    set_token({"state": state})
    st.session_state['auth_url'] = auth_url
    st.markdown(f'请点击此链接进行登录: [Auth0登录]({auth_url})')

# 处理回调
def callback():
    code = st.query_params.get('code')
    if code:
        code = code[0]
        try:
            token = oauth.fetch_token(AUTH0_BASE_URL + '/oauth/token', authorization_response=f"{AUTH0_CALLBACK_URL}?code={code}", state=get_token()['state'])
            set_token(token)
            st.query_params.clear()  # 清除URL中的参数
            st.success('登录成功!')
        except Exception as e:
            st.error('认证失败: ' + str(e))

# 主界面
if 'auth_url' in st.query_params:
    callback()

if 'token' in st.session_state:
    st.write("你已经登录!")
    st.button("登出", on_click=clear_session)
else:
    login()

