import streamlit as st

# 用于存储上传的图片
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None
    
if 'image_sent' not in st.session_state:
    st.session_state.image_sent = False



# 右侧 Chat 输入组件
message = st.chat_input("发送消息")

# 侧边栏文件上传组件
uploaded_file = st.sidebar.file_uploader("上传图片", type=["jpg", "png", "jpeg"])

# 如果有文件上传，则保存到 session state
if uploaded_file is not None:
    st.session_state.uploaded_image = uploaded_file
    st.session_state.image_sent = False

if message:
    # 显示聊天消息
    with st.chat_message("user"):
        st.write(message)
        # 如果有上传的图片，并且这是第一次发送消息，显示图片
        if st.session_state.uploaded_image is not None and not st.session_state.image_sent:
            st.image(st.session_state.uploaded_image)
            st.session_state.image_sent = True
            st.session_state.uploaded_image = None
    

    # 显示回复消息
    st.chat_message("assistant").write("这是你的回复消息。")
