import streamlit as st
import os
from pytube import YouTube
import subprocess

GA_JS = """
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXX');
</script>
"""


def inject_ga():
    index_path = os.path.join(os.path.dirname(st.__file__), 'static', 'index.html')

    try:
        with open(index_path, 'r') as f:
            html = f.read()
    except FileNotFoundError:
        print("index.html not found")
        return

    if '<head>' in html:
        new_html = html.replace('<head>', '<head>\n' + GA_JS)
        with open(index_path, 'w') as f:
            f.write(new_html)
    else:
        print("Could not find '<head>' tag in index.html")

inject_ga()



index_path = os.path.join(os.path.dirname(st.__file__), 'static','index.html')
with open(index_path) as f:
	index_content = f.read()
	
st.markdown('index.html content')
st.write(index_content)


file_path = os.path.dirname(st.__file__)
st.markdown(f"file path: {file_path}")






with st.sidebar:
	st.markdown("# test sidebar layout")
	option = st.selectbox(
    "Select GPT model",
    ("gpt-4o", "gpt-4-0613", "Mobile phone"))



st.title("This is title")
st.write(f"Your option: {option}")


youtube_url = st.text_area(label="input youtube url")


download_button = st.button("Download video")


def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"Downloaded {percentage_of_completion}%")

def youtube_download(video_url):
    yt = YouTube(video_url, on_progress_callback=progress_function)

    # 获取视频标题
    video_title = yt.title
    print(f"Downloading video: {video_title}")

    stream = yt.streams.get_highest_resolution()
    # 获取视频流的默认文件名
    default_filename = stream.default_filename.replace(' ','_')

    stream.download(filename=default_filename)

    return default_filename



if youtube_url:
	if download_button:
		youtube_video = youtube_download(youtube_url)
		st.video(youtube_video)
else:
	st.warning('input youtube url first!')
