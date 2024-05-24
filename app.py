import streamlit as st
import logging

# 配置日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建一个控制台日志处理器
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# 记录一些日志
logger.info("这是一个信息日志")
logger.warning("这是一个警告日志")
logger.error("这是一个错误日志")

# Streamlit 应用界面
st.title("日志记录测试")
st.write("检查 Streamlit Cloud 的日志文件以查看记录的日志。")


prompt = st.chat_input("What is up?")

# React to user input
if prompt:
	# Display user message in chat message container
	logger.info(f"user prompt log: {prompt}")
