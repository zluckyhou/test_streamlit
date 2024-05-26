import streamlit as st
from authlib.integrations.starlette_client import OAuth
import os



CLIENT_ID = st.secrets["client_id"]  # Google Client ID
CLIENT_SECRET = st.secrets["client_secret"]  # Google Client Secret
AUTHORIZE_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
REVOKE_ENDPOINT = "https://oauth2.googleapis.com/revoke"
REDIRECT_URL = st.secrets["redirect_url"]



# 初始化OAuth 2客户端
oauth = OAuth()
oauth.register(
    name='google',
    client_id=st.secrets["client_id"],  # 替换为你的Google客户端ID
    client_secret=st.secrets["client_secret"],  # 替换为你的Google客户端密钥
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid profile email'},
)

# Streamlit页面布局
def main():
    st.title('Google 登录示例')

    # 显示登录按钮
    if 'auth_token' not in st.session_state:
        authorize_url, state = oauth.google.authorize_redirect(
            redirect_uri='http://localhost:8501'
        )
        st.session_state['oauth_state'] = state
        st.markdown(f'<a href="{authorize_url}" target="_self">使用Google登录</a>', unsafe_allow_html=True)
    else:
        # 访问受保护的资源
        resp = oauth.google.get('userinfo', token=st.session_state['auth_token'])
        user_info = resp.json()
        st.write(f'Hi {user_info["name"]}!')

        if st.button('Logout'):
            st.session_state.pop('auth_token', None)

# 处理OAuth回调
def auth_callback():
    token = oauth.google.authorize_access_token()
    st.session_state['auth_token'] = token

# 设置Streamlit页面配置
if __name__ == "__main__":
    if 'oauth_state' in st.experimental_get_query_params():
        auth_callback()
    main()
