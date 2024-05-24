import streamlit as st
import logging

# 创建一个列表来存储日志消息
log_messages = []

class StreamlitHandler(logging.Handler):
    def emit(self, record):
        log_messages.append(self.format(record))

# 创建一个 Streamlit 日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
st_handler = StreamlitHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
st_handler.setFormatter(formatter)
logger.addHandler(st_handler)

# 在需要的地方记录日志
logger.info("这是一个信息日志")
logger.warning("这是一个警告日志")
logger.error("这是一个错误日志")

prompt = st.chat_input("hello")
logger.info(f"this is user prompt: {prompt}")

# 在 Streamlit 应用中显示日志
st.text_area("日志", "\n".join(log_messages), height=400)
