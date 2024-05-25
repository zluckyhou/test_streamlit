import os
import streamlit as st
from authlib.integrations.requests_client import OAuth2Session



# 设置Auth0的客户端ID和秘密、域以及会话秘钥
AUTH0_CLIENT_ID = st.secrets["client_id"]  # Google Client ID
AUTH0_CLIENT_SECRET = st.secrets["client_secret"]  # Google Client Secret
AUTH0_DOMAIN = st.secrets['auth_domain']
# SESSION_SECRET_KEY = os.getenv("APP_SECRET_KEY")

# 创建OAuth 2会话
oauth2_session = OAuth2Session(
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    redirect_uri=st.secrets["redirect_url"]
)

def login():
    # 生成Auth0授权URL和session state
    uri, state = oauth2_session.create_authorization_url(
        f'https://{AUTH0_DOMAIN}/authorize',
        scope="openid profile email"
    )
    st.session_state['oauth_state'] = state
    # 重定向用户到Auth0
    st.write('Please login at', uri)

def logout():
    # 清除会话状态
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    # 重定向用户到Auth0注销URL
    st.write('You have been logged out.')

if 'oauth_state' in st.session_state:
    # 处理从Auth0回调后的交换令牌
    token = oauth2_session.fetch_token(
        f'https://{AUTH0_DOMAIN}/oauth/token',
        authorization_response=st.experimental_get_query_params()['code'],
        client_secret=AUTH0_CLIENT_SECRET
    )
    st.session_state['oauth_token'] = token
   
    # 这里获取用户信息，只是一个示例
    user_info = oauth2_session.get(f'https://{AUTH0_DOMAIN}/userinfo').json()
    st.session_state['user_info'] = user_info

    # 这里应当重定向到应用程序的主页或其他页面

if 'user_info' not in st.session_state:
    st.button('Login with Auth0', on_click=login)
else:
    st.write(st.session_state['user_info'])

    st.button('Logout', on_click=logout)

# 应用程序其他的主体代码...
