import os

import moviepy.editor as pyedit
import streamlit as st
from modules.utils import add_bg_from_local, local_css, set_page_config


def main():
    set_page_config()

    local_css()

    background_img_path = os.path.join(
        "static", "background", "Toolbox Logo.png"
    )
    sidebar_background_img_path = os.path.join(
        "static", "background", "Lila Gradient.png"
    )
    page_markdown = add_bg_from_local(
        background_img_path=background_img_path,
        sidebar_background_img_path=sidebar_background_img_path,
    )
    st.markdown(page_markdown, unsafe_allow_html=True)

    st.markdown(
        """<h1 style='text-align: center; color: black; font-size: 40px;'> Welcome to Video Editor 🎬 </h1> \
        <br>""",
        unsafe_allow_html=True,
    )

    video = st.file_uploader(
        "Choose a video to edit",
        type=["mp4", "mov", "avi"],
        accept_multiple_files=False,
    )
    if video is None:
        return

    st.write(video.name)
    edited_video = pyedit.VideoFileClip(video.name)
    with st.sidebar:
        _, center_col, _ = st.columns(3)
        center_col.header("Settings")

        speed = st.slider("Speed up the video", 1, 5)
        edited_video = edited_video.speedx(speed)

        edited_video.write_videofile("video.mp4")

    st.video("video.mp4")


if __name__ == "__main__":
    main()
