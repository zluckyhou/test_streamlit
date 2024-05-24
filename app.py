# import streamlit as st

# # 用于存储上传的图片
# if 'uploaded_image' not in st.session_state:
#     st.session_state.uploaded_image = None
    
# if 'image_sent' not in st.session_state:
#     st.session_state.image_sent = False



# # 右侧 Chat 输入组件
# message = st.chat_input("发送消息")

# # 侧边栏文件上传组件
# uploaded_file = st.sidebar.file_uploader("上传图片", type=["jpg", "png", "jpeg"])

# # 如果有文件上传，则保存到 session state
# if uploaded_file is not None:
#     st.session_state.uploaded_image = uploaded_file
#     st.session_state.image_sent = False

# if message:
#     # 显示聊天消息
#     with st.chat_message("user"):
#         st.write(message)
#         # 如果有上传的图片，并且这是第一次发送消息，显示图片
#         if st.session_state.uploaded_image is not None and not st.session_state.image_sent:
#             st.image(st.session_state.uploaded_image)
#             st.session_state.image_sent = True
#             st.session_state.uploaded_image = None
    

#     # 显示回复消息
#     st.chat_message("assistant").write("这是你的回复消息。")


# import streamlit as st
# from PIL import Image
# import io

# # 初始化一个状态用于存储上传的图片
# if 'uploaded_image' not in st.session_state:
#     st.session_state['uploaded_image'] = None

# # 初始化一个状态，当消息发送后变为True
# if 'message_sent' not in st.session_state:
#     st.session_state['message_sent'] = False

# # 侧边栏的文件上传组件
# uploaded_file = st.sidebar.file_uploader("上传图片", type=['jpg', 'jpeg', 'png'])


# # 主页面的chat input组件
# user_message = st.text_input("发送消息", key="chat_input")

# # 当用户发送消息的时候
# if user_message:
#     if uploaded_file is not None:
#         image_data = uploaded_file.getvalue()
#         st.session_state['uploaded_image'] = image_data
#         # 有新图片上传时重置消息发送状态
#         st.session_state['message_sent'] = False
#     # 显示用户的消息
#     st.write(f"用户: {user_message}")

#     # 如果这是用户上传图片后的第一次消息，并且有图片被上传
#     if not st.session_state['message_sent'] and st.session_state['uploaded_image'] is not None:
#         # 使用Pillow库来打开图片
#         img = Image.open(io.BytesIO(st.session_state['uploaded_image']))
#         st.image(img, caption='上传的图片', use_column_width=True)
        
#         # 标记消息已经发送，下次发送时不再附加图片
#         st.session_state['message_sent'] = True
#         # 以便下次发送消息时不再附带图片
#         st.session_state['uploaded_image'] = None

import streamlit as st

placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder.container():
    st.write("This is one element")
    st.write("This is another")

# Clear all those elements:
placeholder.empty()
