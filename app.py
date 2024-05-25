import streamlit as st
import logging

# 配置日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 清除现有的处理器，避免重复添加
if logger.hasHandlers():
    logger.handlers.clear()

# 创建一个控制台日志处理器
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# 记录一些日志
logger.info("这是一个信息日志")
logger.warning("这是一个警告日志")
logger.error("这是一个错误日志")


import streamlit as st
from authlib.integrations.requests_client import OAuth2Session

# Google的OAuth设置

AUTH_URL = 'https://accounts.google.com/o/oauth2/auth'
TOKEN_URL = 'https://accounts.google.com/o/oauth2/token'

AUTH0_DOMAIN = st.secrets["auth_domain"]

CLIENT_ID = st.secrets["client_id"]  # Google Client ID
CLIENT_SECRET = st.secrets["client_secret"]  # Google Client Secret
REDIRECT_URI = st.secrets["redirect_url"]


SCOPES = ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile']




session = OAuth2Session(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scope=SCOPES, redirect_uri=REDIRECT_URI)
uri, state = session.create_authorization_url(AUTH_URL)

st.write('请点击下方链接使用Google登录:')
st.markdown(f'[登录]({uri})', unsafe_allow_html=True)

# 处理重定向回调
state = st.text_input('粘贴重定向后的URL中的state参数值：')
code = st.text_input('粘贴重定向后的URL中的code参数值：')
if state and code:
    token = session.fetch_token(TOKEN_URL, authorization_response=f'{REDIRECT_URI}?state={state}&code={code}', client_secret=CLIENT_SECRET)
    resp = session.get('https://www.googleapis.com/oauth2/v1/userinfo')
    user_info = resp.json()
    st.write('用户信息：', user_info)



# Streamlit 应用界面
st.title("日志记录测试")
st.write("检查 Streamlit Cloud 的日志文件以查看记录的日志。")

prompt = st.chat_input("What is up?")

# React to user input
if prompt:
    # Display user message in chat message container
    logger.info(f"user prompt log: {prompt}")
